# 潮驿 Agents · 多角色模板

单有「能力卡片」（Skills）还不够——一个分销团队真正需要的是**若干个常驻的数字业务社工**，
各自认领一段业务职责，按节奏自动运转。本目录提供 4 个可直接落地的 **Agent 角色模板**，
每个角色**编排一个或多个 Skill**，并给出「何时上岗 / 日常循环 / 动作 / 红线」。

> 与 Skill 的关系：**Skill 是动词（能做什么），Agent 是名词（谁来做）**。
> 例如 `reach-campaign` 是「触达管家」这个 Agent 的核心能力；Agent 还额外规定了对接人、节奏与汇报方式。

## 角色清单

| 角色 | 目录 | 编排的 Skill | 一句话职责 |
|---|---|---|---|
| 入驻向导 | [`onboarding-guide/`](onboarding-guide/AGENT.md) | `distributor-onboarding` | 让新经销商从签约到首单不靠人盯 |
| 触达管家 | [`reach-steward/`](reach-steward/AGENT.md) | `reach-campaign` | 把政策 / 活动 / 催办编排成多波次触达 |
| 渠道巡检员 | [`channel-inspector/`](channel-inspector/AGENT.md) | `channel-inspection` + `order-inventory-reconcile` | 给渠道做体检、对账、排风险处置 |
| 拜访统筹 | [`visit-coordinator/`](visit-coordinator/AGENT.md) | `visit-plan` | 把业务员路线排满产出、备好话术 |

## 怎么用

1. **直接作为 prompt**：把某个 `AGENT.md` 全文交给你的智能体，说「按这个角色上岗」。
2. **配合 MCP 网关**：先按 [`../mcp-server/README.md`](../mcp-server/README.md) 接入网关，Agent 通过 MCP 调用对应 Skill，无需把 Skill 文件塞进宿主目录。
3. **组合成班组**：4 个角色可同时上线，构成一个最小可行的「分销运营班组」，覆盖「招新 → 触达 → 巡检对账 → 拜访」全链路。

## 红线（所有角色通用）

- 只出草稿 / 建议，**不**直接执行对外发送、改账、清退等破坏性动作（必须 HITL）。
- 不绕过平台合规（短信 / 外呼频次、退订）；不伪造或篡改任何经营 / 财务数据。
- 客户隐私（联系方式、地址、资质）仅用于本次任务，不出域、不留存。
