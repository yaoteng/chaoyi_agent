---
平台: Reddit（r/selfhosted + r/opensource；可加 r/Twitch 等直播社区，勿刷）
最佳发布时间: D1 与 Show HN 同窗口
注意: 遵守各 subreddit 规则，勿跨版重复刷；用"分享+求助"语气而非广告
---

**Title: I turned my live-streaming community's monthly ops from ~40h to ~6h with a set of open-source Skills (MIT)**

Like many small community operators, I was drowning in busywork: onboarding streamers, planning shows, running live-room interactions, moderating content, and growing the audience. Not the fun "sign a big streamer" part — the ops.

So I built **Chaoyi Agent**: a small, MIT-licensed library of cross-host Skills meant to make an existing live-streaming community "agent-assisted" without building any infra.

What's inside (first release):
- `streamer-onboarding` – signup → KYC/qualification → stream setup → first-show plan → training
- `live-show-plan` – topic library, show calendar, script skeleton, multi-platform distribution
- `live-room-ops` – chat/gift/lucky-draw/co-stream/fan-club interaction scripts, talking points, incident SOP
- `community-moderation` – violation rules, 5-tier graduated enforcement, report handling, live compliance red lines
- `audience-growth` – user segmentation, retention/win-back, event ops, live-data retrospective

They're plain `SKILL.md` + templates, compatible with Skills 1.0 and MCP 0.4, so they load in Claude Code / Cursor / WorkBuddy / Codex. The repo includes a full worked example (a fictional food live-streaming community, "Shiguang Live") showing the 40h → 6h math.

Repo: https://github.com/yaoteng/chaoyi_agent

Genuinely curious: what's the ONE ops task in your community you'd automate first? I'll try to sketch a Skill for the top comments.
