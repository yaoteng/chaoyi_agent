---
平台: Hacker News（Show HN）
最佳发布时间: D1 北京时间 23:00 / 美西 08:00（踩 HN 早高峰）
标题: Show HN: Chaoyi Agent – open-source Skills to give small communities a "digital volunteer"
---

I maintain a couple of small OSS projects and the thing that burns me out isn't coding — it's the ops: triaging issues, writing release notes, localizing docs, thanking contributors. So I built a small open-source Skill library that turns a community into a lightweight agent-assisted operation.

Chaoyi Agent ships 5 ready-to-use Skills:
- community-onboarding
- issue-triage
- release-notes
- doc-localization
- contributor-recognition

They're plain SKILL.md + templates, MIT-licensed, zero-dependency, and compatible with both the Skills 1.0 spec and MCP 0.4 — so they run in Claude Code, Cursor, WorkBuddy, Codex, etc.

There's a full worked example (a fictional-but-reproducible Rust tooling library) showing how monthly ops dropped from ~40h to ~6h.

Honest scope: this is NOT another agent framework. It's a focused toolkit for "how do I make my existing community agent-assisted without building infra." Feedback and PRs very welcome — especially the 6th vertical Skill.

https://github.com/yaoteng/chaoyi_agent
