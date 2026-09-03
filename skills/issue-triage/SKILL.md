---
name: issue-triage
description: 自动对开源仓库的议题（issue/PR）进行分类、打标签、定优先级、识别重复项并起草维护者回复。当社区议题堆积、响应慢、重复问题多，需要把「议题管家」自动化时使用。
version: 1.0.0
license: MIT
compatible_hosts: [Claude Code, WorkBuddy, Cursor, Codex]
standards: [Skills 1.0, MCP 0.4]
---

# 议题管家（Issue Triage）

## When to use
- 仓库 Issue / PR 数量多、响应滞后。
- 同一问题被反复提出，缺乏去重。
- 维护者希望统一标签体系与回复口径。

## Steps
1. **拉取待处理议题**：通过 MCP（如 GitHub MCP）读取 open issues / PRs，按更新时间排序。
2. **分类打标**：依据内容判断类型（bug / feature / docs / question / duplicate），建议标签；新仓库可先给出标签体系建议。
3. **优先级**：按「影响面 × 紧急度」定 P0–P3；安全/数据丢失类自动升 P0。
4. **去重检测**：与已有 Issue 标题/正文做语义比对，标 `duplicate` 并附原 Issue 链接。
5. **起草回复**：对 question 类给标准解答模板；对 bug 类请补环境信息；对 feature 类请补使用场景。
6. **汇总看板**：输出当日待处理清单（链接 + 建议标签 + 优先级 + 草案状态）。

## Output
- 每则议题一行：`<链接> | 建议标签 | 优先级 | 重复于<链接>? | 回复草案状态`。
- 标签体系建议（新仓库）。
- 需维护者确认的动作清单（HITL）。

## Guardrails
- 只产草案，**不**直接改标签、不**直接**发评论，需要人确认或显式授权。
- 不得关闭争议性议题、不得标记「wontfix」等终态，除非用户明确要求。
- 去重须给出依据，误标会伤害贡献者，宁可漏标不误标。

## Notes
- 与 `community-onboarding` 协同：good first issue 的维护可交给本 Skill。
- 高频 question 应反向沉淀进 `CONTRIBUTING.md` / FAQ，形成闭环。
