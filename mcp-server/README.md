# 潮驿 MCP 网关（Agent 运行时）

把 [`../skills/`](../skills/) 下所有符合 Skills 1.0 规范的 SKILL.md，加载为**标准 MCP 工具**，
让 Claude Code / Cursor / 任意 MCP 客户端在**不改动宿主**的前提下，按需调用这些「数字社工」技能。

> 这是潮驿的 **agent 运行时**：Skill 是「能力卡片」，MCP 网关是「把能力卡片接进任何智能体的插头」。
> 与纯 `cp -r` 把 Skill 塞进宿主 skills 目录不同，MCP 方式**不污染宿主目录、可集中升级、可同时被多个宿主共享**。

## 特性

- **零依赖**：仅用 Python 标准库，无需 `pip install`，开箱即跑。
- **协议对齐**：实现 MCP 最小可用子集（`initialize` / `tools/list` / `tools/call`），stdio + JSON-RPC 2.0 的 `Content-Length` 分帧，与官方 SDK 互通。
- **自动发现**：启动时扫描 `skills/`，每个 Skill 自动成为一个工具，新增 Skill 无需改网关代码。
- **只读暴露**：网关只把 Skill 的指令文本返回给模型，本身**不执行任何对外动作**；破坏性操作仍由宿主 / 人在回路（HITL）控制——与 [`../CONTRIBUTING.md`](../CONTRIBUTING.md) 的合规红线一致。

## 运行

```bash
# 在项目根目录执行
python mcp-server/server.py
```

进程会阻塞在 stdio 上，等待 MCP 客户端连接。正常情况你看不到输出——那是协议帧，不是日志。

## 接入宿主

### Claude Code

在项目根创建 `.mcp.json`（或写入用户级 `~/.claude.json` 的 `mcpServers`）：

```json
{
  "mcpServers": {
    "chaoyi-agent": {
      "command": "python",
      "args": ["mcp-server/server.py"]
    }
  }
}
```

> 若 `python` 不在 PATH，把 `command` 换成解释器绝对路径，`args` 第一项改为网关的绝对路径。

### Cursor

`Settings → MCP → Add new MCP server`，类型选 `stdio`，命令填：

```
python /绝对路径/chaoyi_agent/mcp-server/server.py
```

接入后，对智能体说「帮我把本周的 issue 分类并起草回复」，它会通过 MCP 调用 `issue-triage` 工具，
拿到技能正文作为执行指引。

## 工具清单（自动生成）

每个工具名 = 对应 Skill 的 `name`；工具描述 = 该 Skill frontmatter 的 `description`；
调用后返回该 Skill 的完整正文（When to use / Steps / Output / Guardrails）。

| 工具名 | 对应 Skill |
|---|---|
| `community-onboarding` | 贡献者入驻 |
| `issue-triage` | 议题管家 |
| `release-notes` | 发布说明 |
| `doc-localization` | 文档本地化 |
| `contributor-recognition` | 贡献致谢 |

## 本地自测

不依赖任何 MCP 客户端，直接用脚本喂协议帧验证：

```bash
python - <<'PY'
import json, subprocess
def frame(o):
    p=json.dumps(o,ensure_ascii=False).encode(); return b"Content-Length: %d\r\n\r\n"%len(p)+p
inp=frame({"jsonrpc":"2.0","id":1,"method":"initialize","params":{}})+ \
    frame({"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}})
out=subprocess.run(["python","mcp-server/server.py"],input=inp,capture_output=True).stdout
# 解析 Content-Length 分帧
i=0
while i<len(out):
    if out[i:i+15].lower().startswith(b"content-length:"):
        e=out.find(b"\r\n\r\n",i); n=int(out[i+15:e].strip()); print(json.loads(out[e+4:e+4+n])); i=e+4+n
    else: i+=1
PY
```

应看到 `initialize` 返回 `serverInfo`，`tools/list` 返回 5 个工具。

## 路线图中的位置

- [x] MCP 网关：把 skills 暴露为统一工具协议 ← **本目录**
- [ ] Agents 多角色模板（见 [`../agents/`](../agents/)）
- [ ] 《30 天社区 agent 化》手册
