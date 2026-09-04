# 潮驿 Agents · 多角色模板

单有「能力卡片」（Skills）还不够——一个社群真正需要的是**若干个常驻的数字社工**，
各自认领一段运营职责，按节奏自动运转。本目录提供 4 个可直接落地的 **Agent 角色模板**，
每个角色**编排一个或多个 Skill**，并给出「何时上岗 / 日常循环 / 动作 / 红线」。

> 与 Skill 的关系：**Skill 是动词（能做什么），Agent 是名词（谁来做）**。
> 例如 `issue-triage` 是「议题管家」这个 Agent 的核心能力；Agent 还额外规定了对接人、节奏与汇报方式。

## 角色清单

| 角色 | 目录 | 编排的 Skill | 一句话职责 |
|---|---|---|---|
| 入驻向导 | [`onboarding-guide/`](onboarding-guide/AGENT.md) | `community-onboarding` | 让新人第一小时就「被接住」 |
| 议题管家 | [`issue-steward/`](issue-steward/AGENT.md) | `issue-triage` | 让 issue 不堆积、响应不滞后 |
| 翻译协调员 | [`translation-coordinator/`](translation-coordinator/AGENT.md) | `doc-localization` | 让文档自然多语言生长 |
| 致谢官 | [`kudos-officer/`](kudos-officer/AGENT.md) | `contributor-recognition` | 让贡献被看见、被记住 |

## 怎么用

1. **直接作为 prompt**：把某个 `AGENT.md` 全文交给你的智能体，说「按这个角色上岗」。
2. **配合 MCP 网关**：先按 [`../mcp-server/README.md`](../mcp-server/README.md) 接入网关，Agent 通过 MCP 调用对应 Skill，无需把 Skill 文件塞进宿主目录。
3. **组合成团队**：4 个角色可同时上线，构成一个最小可行的「社区运营班组」，覆盖「招人 → 管事 → 翻译 → 感谢」全链路。

## 红线（所有角色通用）

- 只出草稿 / 建议，**不**直接执行对外发言、合并、封禁等破坏性动作（必须 HITL）。
- 不绕过社区 CoC / 平台规则；不伪造或篡改任何数据；不刷量。
- 隐私数据仅用于本次任务，不外泄。
