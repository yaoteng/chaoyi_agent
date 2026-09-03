---
name: contributor-recognition
description: 聚合开源项目的贡献数据（commit/PR/Issue/Review），起草致谢文案并生成贡献者荣誉墙，用于 Release 致谢、月度榜单或社区活动。当社区想提升贡献者留存、公开表彰却苦于统计繁琐时使用。
version: 1.0.0
license: MIT
compatible_hosts: [Claude Code, WorkBuddy, Cursor, Codex]
standards: [Skills 1.0, MCP 0.4]
---

# 贡献致谢（Contributor Recognition）

## When to use
- 发版时想写致谢段，但统计贡献者繁琐。
- 想做「本月贡献者」榜单提升留存。
- 社区活动 / 周年庆需要表彰名单。

## Steps
1. **采集贡献**：通过 MCP（GitHub 等）拉取指定时间窗内的 PR、Issue、Review、合并情况。
2. **去重归并**：按作者去重，区分「代码 / 文档 /  Issue 报告 / 评审」等贡献类型。
3. **排名与分组**：给出 Top 贡献者（可多选维度），并标注各类贡献的「幕后英雄」（如大量 review 但少 PR 的人）。
4. **起草致谢**：生成一段真诚、具体的致谢文案（点名 + 贡献类型 + 影响），避免套话。
5. **荣誉墙**：输出 Markdown / HTML 表格，含头像链接（如平台提供）、贡献类型、数量。

## Output
- 致谢文案（可直接贴 Release / 公众号）。
- 贡献者荣誉墙（Markdown 表格，按类型分组）。
- 「幕后英雄」特别名单（review / 文档类）。

## Guardrails
- 数据须基于真实记录，**不得虚构或夸大**任何贡献。
- 隐私：仅在贡献者已公开其身份的前提下点名；如不确定，用 @handle 而非真名。
- 不自动发帖、不自动改 README 荣誉墙，产出后由人确认。

## Notes
- 与 `release-notes` 联动：本期致谢名单可自动并入发布说明。
- 长期运行可形成「贡献者图谱」，帮助识别潜在维护者（Maintainer 梯队）。
