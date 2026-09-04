---
平台: Hacker News（Show HN）
最佳发布时间: D1 北京时间 23:00 / 美西 08:00（踩 HN 早高峰）
标题: Show HN: Chaoyi Agent – open-source Skills that give a distribution/sales team a "digital field worker"
---

I run a small fast-moving consumer goods (FMCG) distribution operation, and the thing that burns me out isn't selling — it's the ops: onboarding dealers, chasing policy/payment reminders, inspecting channel health, reconciling orders vs. inventory vs. receivables, and planning rep visits. So I built a small open-source Skill library that turns a distribution team into a lightweight agent-assisted operation.

Chaoyi Agent ships 5 ready-to-use Skills:
- distributor-onboarding
- reach-campaign
- channel-inspection
- order-inventory-reconcile
- visit-plan

They're plain SKILL.md + templates, MIT-licensed, zero-dependency, and compatible with both the Skills 1.0 spec and MCP 0.4 — so they run in Claude Code, Cursor, WorkBuddy, Codex, etc.

There's a full worked example (a fictional-but-reproducible FMCG distributor, "Yunzhan Distribution") showing how monthly ops dropped from ~40h to ~6h.

Honest scope: this is NOT another agent framework. It's a focused toolkit for "how do I make my existing distribution team agent-assisted without building infra." Feedback and PRs very welcome — especially the 6th vertical Skill.

https://github.com/yaoteng/chaoyi_agent
