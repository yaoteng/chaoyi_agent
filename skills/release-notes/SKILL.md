---
name: release-notes
description: 基于 git 提交历史（推荐 conventional commits）自动生成结构化发布说明与 changelog。当项目要发版、需要把散落的 commit 整理成用户可读的更新日志时使用。
version: 1.0.0
license: MIT
compatible_hosts: [Claude Code, WorkBuddy, Cursor, Codex]
standards: [Skills 1.0, MCP 0.4]
---

# 发布说明（Release Notes）

## When to use
- 准备发版（打 tag / 发 GitHub Release）。
- 维护 `CHANGELOG.md` 需要增量更新。
- 想把技术 commit 翻译成用户 / 贡献者能读懂的变更摘要。

## Steps
1. **确定范围**：读取从上一个 tag（或指定 commit）到 HEAD 的全部提交。
2. **解析类型**：按 conventional commits 归类 `feat / fix / docs / perf / refactor / chore` 等。
3. **提炼要点**：每条 feat/fix 转成一句用户视角的说明，去掉内部实现细节。
4. **生成双产物**：
   - `release_notes.md`：面向用户/贡献者，按「✨ 新功能 / 🐛 修复 / 📚 文档 / ⚡ 性能」分组，含升级提示与致谢。
   - `CHANGELOG` diff：追加 `[x.y.z] - YYYY-MM-DD` 段落到现有文件。
5. **风险提示**：若有 breaking change，单独高亮并在升级提示中强调。

## Output
- 一段可直接贴进 Release 的 Markdown。
- `CHANGELOG.md` 的 PR-ready diff（追加段落）。
- 若有 breaking change，列出迁移步骤清单。

## Guardrails
- 不编造未发生的变更；只基于真实 commit。
- 不替用户打 tag、不替用户发 Release，产出后由人确认执行。
- 贡献者致谢名单应基于真实提交/PR，避免遗漏或虚构。

## Notes
- 若未用 conventional commits，退化为按关键词/目录推断，并在输出注明「非标准提交，分类可能不准」。
- 可与 `contributor-recognition` 联动，自动生成本期致谢名单。
