#!/usr/bin/env python3
"""潮驿 Chaoyi Agent · MCP 网关（agent 运行时）

把 skills/ 下所有符合 Skills 1.0 规范的 SKILL.md 加载为 **MCP 工具**，
让 Claude Code / Cursor / 任意 MCP 客户端在「不改动宿主」的前提下，
按需调用这些「数字社工」技能。

设计原则：
- **零依赖**：仅用 Python 标准库（无需 pip install）。
- **协议对齐**：实现 MCP 的最小可用子集（initialize / tools/list / tools/call），
  使用 stdio + 换行分隔的 JSON-RPC 2.0 消息（与官方 SDK 互通）。
- **只读暴露**：网关只把 Skill 的指令文本返回给模型，本身不执行任何对外动作，
  破坏性操作仍由宿主/人在回路（HITL）控制——与 Skill 的 Guardrails 一致。

运行：
    python mcp-server/server.py

接入（以 Claude Code 为例，在 .mcp.json / settings 中声明）：
    {
      "mcpServers": {
        "chaoyi-agent": { "command": "python", "args": ["mcp-server/server.py"] }
      }
    }
"""
import io
import json
import os
import sys

# ---- 路径 ----
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_HERE)
_SKILLS_DIR = os.path.join(_REPO_ROOT, "skills")

# MCP 协议版本（与主流客户端兼容的快照版本号）
PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "chaoyi-agent-mcp"
SERVER_VERSION = "0.1.0"

REQUIRED_FIELDS = ["name", "description", "version", "license", "compatible_hosts", "standards"]
_SKIP_DIRS = {"_template"}


def _parse_frontmatter(text: str):
    """解析 SKILL.md 顶部 YAML frontmatter（仅支持本仓库用到的简单结构）。"""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_raw = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    data = {}
    for line in fm_raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [i.strip().strip('"').strip("'") for i in inner.split(",") if i.strip()]
        else:
            data[key] = val.strip().strip('"').strip("'")
    return data, body


def load_skills():
    """扫描 skills/ 目录，返回 [{name, description, body, raw}] 列表。"""
    skills = []
    if not os.path.isdir(_SKILLS_DIR):
        return skills
    for name in sorted(os.listdir(_SKILLS_DIR)):
        d = os.path.join(_SKILLS_DIR, name)
        if not os.path.isdir(d) or name in _SKIP_DIRS:
            continue
        skill_md = os.path.join(d, "SKILL.md")
        if not os.path.isfile(skill_md):
            continue
        with open(skill_md, encoding="utf-8") as f:
            text = f.read()
        fm, body = _parse_frontmatter(text)
        skills.append({
            "name": fm.get("name", name),
            "description": fm.get("description", ""),
            "body": body,
            "raw": text,
            "frontmatter": fm,
        })
    return skills


_SKILLS = load_skills()


# ---- JSON-RPC / MCP stdio framing ----
def _read_message(stream: io.BufferedReader) -> dict | None:
    """Read one newline-delimited JSON-RPC message from an MCP stdio stream."""
    line = stream.readline()
    if not line:
        return None
    try:
        message = json.loads(line.decode("utf-8", "replace"))
    except json.JSONDecodeError:
        return None
    if not isinstance(message, dict):
        return None
    return message


def _write_message(stream: io.BufferedWriter, msg: dict):
    payload = json.dumps(msg, ensure_ascii=False).encode("utf-8")
    stream.write(payload + b"\n")
    stream.flush()


def _tool_list():
    tools = []
    for s in _SKILLS:
        tools.append({
            "name": s["name"],
            "description": s["description"],
            "inputSchema": {
                "type": "object",
                "properties": {
                    "task": {
                        "type": "string",
                        "description": "要交给「%s」处理的具体任务描述（如：把本周 issue 分类并起草回复）" % s["name"],
                    }
                },
                "required": ["task"],
            },
        })
    return tools


def _dispatch(method: str, params: dict):
    """返回 (result, is_error)。"""
    if method == "initialize":
        return {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        }, False

    if method == "tools/list":
        return {"tools": _tool_list()}, False

    if method == "tools/call":
        name = (params or {}).get("name")
        skill = next((s for s in _SKILLS if s["name"] == name), None)
        if skill is None:
            return {
                "content": [{"type": "text", "text": "未知技能：%s" % name}],
                "isError": True,
            }, True
        body = skill["body"].strip() or skill["raw"]
        return {
            "content": [{"type": "text", "text": body}],
            "isError": False,
        }, False

    if method == "ping":
        return {}, False

    # 未实现的方法：返回标准错误，避免客户端挂起
    raise _MethodNotFound(method)


class _MethodNotFound(Exception):
    def __init__(self, method):
        self.method = method


def main():
    stdin = sys.stdin.buffer
    stdout = sys.stdout.buffer
    while True:
        msg = _read_message(stdin)
        if msg is None:
            break
        method = msg.get("method")
        msg_id = msg.get("id")
        params = msg.get("params", {}) or {}

        # 通知（无 id）不回复
        if msg_id is None:
            continue

        try:
            result, _ = _dispatch(method, params)
            _write_message(stdout, {"jsonrpc": "2.0", "id": msg_id, "result": result})
        except _MethodNotFound as e:
            _write_message(stdout, {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": "Method not found: %s" % e.method},
            })
        except Exception as e:  # noqa: BLE001
            _write_message(stdout, {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32603, "message": "Internal error: %s" % e},
            })


if __name__ == "__main__":
    main()
