---
name: doc-localization
description: 协调开源项目文档的多语言翻译——抽取待译段落、派发任务、跟踪进度并产出 PR-ready 的 diff。当项目要出海、需要把中文/英文文档翻译成多语言版本却缺翻译流程时使用。
version: 1.0.0
license: MIT
compatible_hosts: [Claude Code, WorkBuddy, Cursor, Codex]
standards: [Skills 1.0, MCP 0.4]
---

# 文档本地化（Doc Localization）

## When to use
- 想把文档从中文扩到英文 / 日文 / 其它语言。
- 已有多语言目录但翻译严重滞后、缺跟踪。
- 希望用「源文档变更 → 自动标出待译段落」的流水线。

## Steps
1. **建立映射**：约定语言目录结构（如 `docs/zh/`、`docs/en/`），识别源语言与待译语言。
2. **抽取待译**：比对源文件与目标文件，找出新增/变更的章节与段落，输出「待译清单」（文件路径 + 行号 + 原文摘要）。
3. **翻译草稿**：对每段生成目标语言译文，保留代码块 / 专有名词 / 链接原样。
4. **派发建议**：按篇幅把清单拆成若干 PR 任务，给出建议认领说明（可直接用于「招募译者」Issue）。
5. **产出 diff**：生成目标语言文件的 PR-ready 修改（新增/更新段落），并附「译后需人工校对」提示。

## Output
- 待译清单（Markdown 表格：文件 | 行号 | 原文摘要 | 篇幅）。
- 译文草稿（按文件组织，代码块原样）。
- 一个「招募译者」Issue 模板（含任务拆分）。
- PR-ready diff（需人 review 后提交）。

## Guardrails
- 机器译文须标注「待人工校对」，不得伪装为终稿。
- 代码、命令、API 名、品牌名保持原样，不翻译。
- 不自动开 PR、不自动合并；由人 review 后提交。

## Notes
- 可与 `community-onboarding` 协同：把翻译任务作为 good first issue 派发给新贡献者（低门槛、易上手）。
- 大型文档建议分批，避免单次 diff 过大。
