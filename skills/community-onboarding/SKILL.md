---
name: community-onboarding
description: 为开源社区设计并自动化贡献者入驻流程——从 good first issue 标记、新人任务引导到欢迎机器人话术。当社区维护者想降低贡献者流失率、搭建标准化的入驻流水线或设计欢迎流程时使用。
version: 1.0.0
license: MIT
compatible_hosts: [Claude Code, WorkBuddy, Cursor, Codex]
standards: [Skills 1.0, MCP 0.4]
---

# 贡献者入驻（Community Onboarding）

## When to use
- 社区新人「想贡献但不知道从哪下手」。
- 维护者希望系统化运营 good first issue。
- 想用欢迎机器人 / Issue 模板降低首次贡献门槛。

## Steps
1. **盘点入口**：读取仓库的 `CONTRIBUTING.md`、Issue 标签、现有 good first issue 数量，识别「新人不友好」的堵点。
2. **设计入驻阶梯**：把贡献路径拆成 3 级——① 文档/翻译类（零门槛）→ ② good first issue（小代码）→ ③ 进阶任务（需 review）。
3. **生成 good first issue 清单**：基于未分配、低复杂度、有清晰验收标准的 Issue，建议打标 `good first issue` 并配上手指南模板。
4. **起草欢迎话术**：给「首次提交 PR」「首次提 Issue」两种场景写欢迎机器人回复（中文优先，含下一步指引与导师 @）。
5. **产出接入清单**：列出需要维护者手动确认/配置的项（如机器人 Webhook、标签体系、导师名单）。

## Output
- 一份《入驻阶梯》Markdown（含各级示例任务）。
- 一组建议打 `good first issue` 的 Issue 链接 + 理由。
- 两段欢迎话术（PR / Issue）。
- 一份「待维护者确认」清单（HITL）。

## Guardrails
- 只出草稿与建议，**不**自动改仓库标签、不自动发帖，需维护者确认。
- 导师匹配涉及真人分工，必须人确认，不得臆造导师可用性。
- 尊重社区 CoC，欢迎话术不得诱导、骚扰或承诺无法兑现的回报。

## Notes
- 可配合 `issue-triage` 联动：入驻阶梯的 Issue 由议题管家持续维护。
- 适用于 GitHub / GitLab / Gitee，按平台差异调整标签名与模板语法。
