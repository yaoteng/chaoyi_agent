# 潮驿 Chaoyi Agent

> 面向开源社区的 **Agent / Skill 工具箱 + 改造方法论**。
> 让每一个小社群，都能拥有自己的「数字社工 / 数字志愿者」。

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/yaoteng/chaoyi_agent?style=social)](https://github.com/yaoteng/chaoyi_agent)
[![Skills 1.0](https://img.shields.io/badge/standard-Skills%201.0-blue.svg)](https://agentskills.io)
[![MCP](https://img.shields.io/badge/protocol-MCP%200.4-blue.svg)](https://modelcontextprotocol.io)

---

## 这是什么

**潮驿**不再是一个直播产品，而是一个**帮助社区完成 agent 化改造**的开源项目。

我们观察到：2026 年是「智能体上岗元年」，但大部分开源 / 开发者 / 兴趣社群**没有能力、也没有预算**去搭建自己的智能体。大厂平台（如 Coze）闭源、不可自托管；通用框架（LangChain / Dify）太重、不解决「社群日常运营」这个具体场景。

潮驿把社群最重复的运营动作，封装成一套**可即插即用、可自托管、跨宿主运行**的 Skills：

| Skill | 它替社群做什么 |
|---|---|
| `community-onboarding` | 设计贡献者入驻流程、good first issue 流水线、欢迎话术 |
| `issue-triage` | 自动标记 / 优先级 / 去重 / 起草回复 GitHub·GitLab 议题 |
| `release-notes` | 从 conventional commits 生成发布说明与 changelog |
| `doc-localization` | 多语言文档翻译协调：抽取、派发、跟踪、产出 PR-ready diff |
| `contributor-recognition` | 聚合贡献数据、起草致谢、生成贡献者荣誉墙 |

> 这 5 个就是「数字社工」的雏形——它们解决的是社群**人少事多、传承难、新人留不住**的真实痛点。

## 为什么不同

- **场景聚焦**：只做「社区 agent 化」，不做通用 AGI。
- **标准兼容**：所有 Skill 遵循 [Skills 1.0](https://agentskills.io) 规范，并可通过 MCP 0.4 暴露工具；**跨宿主运行**——Claude Code / WorkBuddy / Cursor / Codex 直接加载。
- **中文优先**：文档、示例、话术默认中文，补齐海外项目的空白。
- **方法论即产品**：配套《30 天社区 agent 化》手册，不只给工具，给路径。
- **MIT 开源**：自由使用、二次开发、再分发。

## 快速开始

把某个 Skill 接入你的智能体（以 WorkBuddy / Claude Code 为例）：

```bash
# 方式一：直接放入宿主的 skills 目录
cp -r skills/issue-triage ~/.workbuddy/skills/        # WorkBuddy（用户级）
# 或 cp -r skills/issue-triage .claude/skills/        # Claude Code
# 或 cp -r skills/issue-triage .cursor/skills/        # Cursor

# 方式二（规划中）：通过 MCP 网关统一加载
# mcp-server 读取 skills/ 下全部 SKILL.md，按需注入上下文
```

导入后，对智能体说「帮我把本周的 issue 分类并起草回复」，它就会调用 `issue-triage` 技能。

## 示例：社区 agent 化改造

想知道这些 Skill 落到真实社群是什么样？看 [examples/reference-community](examples/reference-community/README.md)——一个 2.3k star 的 Rust 工具库社区，用潮驿 5 个 Skill 把月度运营工时从约 40h 压到约 6h 的完整记录（含 before/after 与可直接复制的 Skill 调用话术）。

## 仓库结构

```
chaoyi_agent/
├─ README.md                     # 本文件
├─ LICENSE                       # MIT
├─ skills/                       # ★ Skills 库（首发 5 个）
│  ├─ README.md                  # 技能索引与接入说明
│  ├─ _template/                 # 新技能脚手架模板
│  ├─ community-onboarding/
│  ├─ issue-triage/
│  ├─ release-notes/
│  ├─ doc-localization/
│  └─ contributor-recognition/
├─ 潮驿项目重新定位方案.md        # 战略定位（为何从直播转向 agent）
├─ 潮驿Agent项目竞品分析.md      # 竞品分析（Agent/Skill 赛道）
├─ 潮驿Agent一周千星战术战略书.md # 开源推广作战书
├─ 决策确认与执行记录.md          # 5 项关键决策与执行落点
└─ archive/                      # 早期「直播方向」文档（已归档，仅供参考）
```

## 仓库（已上线）

🔗 **https://github.com/yaoteng/chaoyi_agent** —— 公开仓库，代码 / MIT License / v0.1.0 Release 均已上线。

> ⚠️ 若你看到仓库**描述（description）为空、没有 Topics 标签**，在本地项目目录跑下面这条补齐（只需一次，需 `gh auth login`）：
>
> ```bash
> gh repo edit yaoteng/chaoyi_agent \
>   --description "面向开源社区的 Agent/Skill 工具箱 + 社区 agent 化改造方法论。5 个开箱即用社群 Skill，兼容 Skills 1.0 + MCP 0.4，跨宿主运行，MIT。" \
>   --homepage "https://github.com/yaoteng/chaoyi_agent" \
>   --add-topic ai-agents --add-topic skills --add-topic mcp --add-topic open-source \
>   --add-topic community --add-topic developer-tools --add-topic llm --add-topic automation \
>   --add-topic chinese --add-topic agent-framework --add-topic self-hosted
> ```
>
> 这样 GitHub 搜索与社媒卡片才能正确曝光——**发帖冲星前务必先执行**。

或重跑发布脚本（已对「仓库已存在」做健壮处理，会自动补 description + topics）：`bash scripts/publish_to_github.sh`。

## 路线图

- [x] **Skills 库首发**（5 个社群技能 + 模板）
- [ ] MCP 网关：把 skills 暴露为统一工具协议
- [ ] Agents 多角色模板（入驻向导 / 议题管家 / 翻译协调员 / 致谢官）
- [ ] 《30 天社区 agent 化》手册
- [x] 参考改造样例（首个被 agent 化的开源社群）→ [examples/reference-community](examples/reference-community/README.md)

## 冲星战役（发布后执行）

想要一周冲 1000 star？仓库发布后，按 [`launch/`](launch/README.md) 执行：
- [`launch/runbook.md`](launch/runbook.md) —— 每日作战手册（D-1 → D0~D6）
- [`launch/posts/`](launch/posts/) —— 10 篇各平台现成发帖文案（掘金/V2EX/知乎/Show HN/Reddit/Dev.to/X/公众号/小红书/Product Hunt）
- [`launch/demo-script.md`](launch/demo-script.md) —— 30 秒演示视频分镜
- [`launch/kpi-tracker.md`](launch/kpi-tracker.md) —— 每日 KPI 追踪表

## 贡献

见 [CONTRIBUTING](CONTRIBUTING.md)（含合规红线与新增 Skill 流程）与 `skills/_template/`。

## 许可证

[MIT](LICENSE) —— 可自由使用、二次开发、再分发。
