---
平台: Dev.to（可同步 Medium）
最佳发布时间: D1（与 Reddit 同天，海外开发者流量）
标题: Stop Drowning in Live-Community Ops: 5 Open-Source Skills That Gave My Community a "Digital Community Worker"
标签: #opensource #ai #agents #livestreaming #community
---

# Stop Drowning in Live-Community Ops: 5 Open-Source Skills That Gave My Community a "Digital Community Worker"

Running a small live-streaming community is mostly not signing streamers. It's ops.

- Onboarding a growing list of streamers (KYC, stream setup, first-show prep)
- Planning shows by gut feel — topic clashes, missing trailers, no clips
- Running live-room interactions on the fly — cold chat, high-value viewers ignored
- Moderating content by hand — reports go unanswered, no real-time live risk control
- Growing the audience but only gaining followers, not conversions

For a 1–3 person community team, that's ~40 hours a month of low-leverage work.

## What I built

**Chaoyi Agent** is a small, MIT-licensed library of cross-host Skills designed to make an existing live-streaming community agent-assisted — no infra, no new platform.

First release ships 5 Skills:

```text
skills/
├── streamer-onboarding/    # streamer signup pipeline
├── live-show-plan/         # show planning & calendar
├── live-room-ops/          # live-room interaction ops
├── community-moderation/   # content moderation & risk control
└── audience-growth/        # audience ops & retrospective
```

Each is a plain `SKILL.md` + template. They're compatible with **Skills 1.0** and **MCP 0.4**, so they run in Claude Code, Cursor, WorkBuddy, and Codex.

## How you'd use it

Point your agent at the `skills/` directory and say:

> "For the 3 new food streamers we just signed, generate the onboarding ladder via streamer-onboarding and衔接 their first-show plan."

The agent calls `streamer-onboarding`, and returns a copy-paste-ready ladder.

## Why not "just use LangChain/Dify"?

Those help you *build* agents. Chaoyi helps you *agent-ize the live community you already have*. It's a narrower, more practical wedge: scenario-focused (live-community only), standard-compatible, Chinese-first, and the methodology **is** the product.

## Try it

The repo includes a full worked example (`examples/reference-livestream/`) — a fictional-but-reproducible food live-streaming community, "Shiguang Live" — showing the 40h → 6h breakdown.

👉 https://github.com/yaoteng/chaoyi_agent

MIT licensed. Fork it, add your 6th vertical Skill, send a PR.
