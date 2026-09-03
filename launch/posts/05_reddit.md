---
平台: Reddit（r/selfhosted + r/opensource；若样例用 Rust 可加 r/rust）
最佳发布时间: D1 与 Show HN 同窗口
注意: 遵守各 subreddit 规则，勿跨版重复刷；用"分享+求助"语气而非广告
---

**Title: I turned my OSS community's monthly ops from ~40h to ~6h with a set of open-source Skills (MIT)**

Like many small maintainers, I was drowning in busywork: triaging issues, writing release notes, translating docs, thanking contributors. Not the fun coding part — the ops.

So I built **Chaoyi Agent**: a small, MIT-licensed library of cross-host Skills meant to make an existing community "agent-assisted" without building any infra.

What's inside (first release):
- `community-onboarding` – contributor onboarding flow
- `issue-triage` – label, draft replies, flag good-first-issues
- `release-notes` – structured release notes from commits
- `doc-localization` – multi-language doc sync
- `contributor-recognition` – thank-you wall

They're plain `SKILL.md` + templates, compatible with Skills 1.0 and MCP 0.4, so they load in Claude Code / Cursor / WorkBuddy / Codex. The repo includes a full worked example (a fictional Rust tooling lib) showing the 40h → 6h math.

Repo: https://github.com/yaoteng/chaoyi_agent

Genuinely curious: what's the ONE ops task in your community you'd automate first? I'll try to sketch a Skill for the top comments.
