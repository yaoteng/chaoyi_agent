---
平台: Reddit（r/selfhosted + r/opensource；可加 r/Frugal 等偏快消社区，勿刷）
最佳发布时间: D1 与 Show HN 同窗口
注意: 遵守各 subreddit 规则，勿跨版重复刷；用"分享+求助"语气而非广告
---

**Title: I turned my FMCG distributor's monthly ops from ~40h to ~6h with a set of open-source Skills (MIT)**

Like many small distribution operators, I was drowning in busywork: onboarding dealers, blasting policy/payment reminders, inspecting channel health, reconciling orders vs. inventory, and planning rep visits. Not the fun selling part — the ops.

So I built **Chaoyi Agent**: a small, MIT-licensed library of cross-host Skills meant to make an existing distribution team "agent-assisted" without building any infra.

What's inside (first release):
- `distributor-onboarding` – dealer signup → qualification → system activation → training → first order
- `reach-campaign` – multi-wave reach via WeChat/SMS/calls with cadence + scripts
- `channel-inspection` – scores sell-through/inventory/receivables/cross-selling, flags anomalies
- `order-inventory-reconcile` – reconciles orders/outbound/inventory/receivables, finds gaps & bad-debt risk
- `visit-plan` – routes rep visits by priority/geo/output with talking points

They're plain `SKILL.md` + templates, compatible with Skills 1.0 and MCP 0.4, so they load in Claude Code / Cursor / WorkBuddy / Codex. The repo includes a full worked example (a fictional FMCG distributor, "Yunzhan Distribution") showing the 40h → 6h math.

Repo: https://github.com/yaoteng/chaoyi_agent

Genuinely curious: what's the ONE ops task in your distribution/sales team you'd automate first? I'll try to sketch a Skill for the top comments.
