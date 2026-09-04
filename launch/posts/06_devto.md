---
平台: Dev.to（可同步 Medium）
最佳发布时间: D1（与 Reddit 同天，海外开发者流量）
标题: Stop Drowning in Distribution Ops: 5 Open-Source Skills That Gave My Team a "Digital Field Worker"
标签: #opensource #ai #agents #distribution #productivity
---

# Stop Drowning in Distribution Ops: 5 Open-Source Skills That Gave My Team a "Digital Field Worker"

Running a small fast-moving consumer goods (FMCG) distribution business is mostly not selling. It's ops.

- Onboarding a growing list of dealers
- Blasting policy / promotion / payment reminders
- Inspecting channel health before accounts churn
- Reconciling orders, outbound, inventory, and receivables every month-end
- Planning rep visits by gut feel

For a 1–3 person channel team, that's ~40 hours a month of low-leverage work.

## What I built

**Chaoyi Agent** is a small, MIT-licensed library of cross-host Skills designed to make an existing distribution team agent-assisted — no infra, no new platform.

First release ships 5 Skills:

```text
skills/
├── distributor-onboarding/   # dealer onboarding pipeline
├── reach-campaign/           # multi-channel reach cadence + scripts
├── channel-inspection/       # channel health scoring
├── order-inventory-reconcile/# order/inventory/receivables reconciliation
└── visit-plan/               # rep visit routing + talking points
```

Each is a plain `SKILL.md` + template. They're compatible with **Skills 1.0** and **MCP 0.4**, so they run in Claude Code, Cursor, WorkBuddy, and Codex.

## How you'd use it

Point your agent at the `skills/` directory and say:

> "Plan a 3-wave payment-dunning reach for East-China dealers over 60 days overdue — per-channel scripts, dedupe same channel within 24h."

The agent calls `reach-campaign`, and returns a copy-paste-ready schedule.

## Why not "just use LangChain/Dify"?

Those help you *build* agents. Chaoyi helps you *agent-ize the distribution team you already have*. It's a narrower, more practical wedge: scenario-focused (distribution only), standard-compatible, Chinese-first, and the methodology **is** the product.

## Try it

The repo includes a full worked example (`examples/reference-distribution/`) — a fictional-but-reproducible FMCG distributor, "Yunzhan Distribution" — showing the 40h → 6h breakdown.

👉 https://github.com/yaoteng/chaoyi_agent

MIT licensed. Fork it, add your 6th vertical Skill, send a PR.
