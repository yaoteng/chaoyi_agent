# 潮驿 Agents · 多角色模板

单有「能力卡片」（Skills）还不够——一个直播社区真正需要的是**若干个常驻的数字社工**，
各自认领一段社区运营职责，按节奏自动运转。本目录提供 4 个可直接落地的 **Agent 角色模板**，
每个角色**编排一个或多个 Skill**，并给出「何时上岗 / 日常循环 / 动作 / 红线」。

> 与 Skill 的关系：**Skill 是动词（能做什么），Agent 是名词（谁来做）**。
> 例如 `live-room-ops` 是「直播间运营官」这个 Agent 的核心能力；Agent 还额外规定了对接人、节奏与汇报方式。

## 角色清单

| 角色 | 目录 | 编排的 Skill | 一句话职责 |
|---|---|---|---|
| 主播入驻向导 | [`onboarding-guide/`](onboarding-guide/AGENT.md) | `streamer-onboarding` | 让新主播从签约到首播不靠人盯 |
| 直播策划师 | [`show-planner/`](show-planner/AGENT.md) | `live-show-plan` | 把选题 / 排期 / 脚本 / 分发排成有节奏的内容供给 |
| 直播间运营官 | [`room-operator/`](room-operator/AGENT.md) | `live-room-ops` | 让每场直播的互动有节奏、有管控、可复制 |
| 社区守护者 | [`community-warden/`](community-warden/AGENT.md) | `community-moderation` + `audience-growth` | 一手管内容风控、一手管观众增长 |

## 怎么用

1. **直接作为 prompt**：把某个 `AGENT.md` 全文交给你的智能体，说「按这个角色上岗」。
2. **配合 MCP 网关**：先按 [`../mcp-server/README.md`](../mcp-server/README.md) 接入网关，Agent 通过 MCP 调用对应 Skill，无需把 Skill 文件塞进宿主目录。
3. **组合成班组**：4 个角色可同时上线，构成一个最小可行的「直播社区运营班组」，覆盖「入驻 → 策划 → 互动 → 风控与增长」全链路。

## 红线（所有角色通用）

- 只出草稿 / 建议，**不**直接执行对外发送、封禁、清退等破坏性动作（必须 HITL）。
- 不绕过平台合规（未成年人保护、打赏限额、版权、内容安全）；不伪造或篡改任何直播 / 观众数据。
- 主播 / 观众隐私（实名、联系方式、画像）仅用于本次任务，不出域、不留存。
