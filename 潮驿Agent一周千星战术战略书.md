# 潮驿 Agent · 一周冲 1000 Star 战术战略书

> ⚠️ **定位更新（2026-09-05）**：本项目已从「开源社区 agent 化工具箱」转向「**分销业务 agent 化工具箱**」。本作战书的**渠道 / 节奏方法论仍可沿用**，但所有 hook 与素材需把「社群 / 数字社工」替换为「**分销团队 / 数字业务社工**」（如：经销商入驻、多渠道触达、渠道巡检、订单对账、拜访排程）。下文仍保留原措辞，发布前请按 `launch/posts/` 的新版分销文案口径统一替换；详细转向记录见《决策确认与执行记录》第五节。

> 配套《潮驿项目重新定位方案》《潮驿Agent项目竞品分析》。本作战书沿用此前直播方向的**渠道与节奏方法论**，但 hook 与素材全部替换为「分销业务 agent 化」。

## 0. 战略支点

**一句话定位（hook）**：
> 「让每一个分销团队，都能拥有自己的数字业务社工。」
> 一套 MIT 开源、跨宿主（Claude Code / WorkBuddy / Cursor）、即插即用的**分销业务智能体技能库**。

**为什么能冲星**：
- Agent/Skill 是 2026 最大确定性赛道，但「分销业务 agent 化」是蓝海（竞品分析已确认：无统治级开源项目）。
- 我们首发就是**可运行、可复制的 5 个分销 Skills + MCP 网关 + 模板 + 索引**，不是 PPT。
- 复用已验证打法：你方 FMCG 分销 SaaS 冲 1000 star、掘金过审长文、四端工程经验。
- 中文优先 + 标准兼容（Skills 1.0 / MCP 0.4）→ 同时吃中文分销 / 快消从业者社群与海外 agent 生态两波流量。

**可量化卖点（写进 README/About）**：
- 5 个即用 Skill：入驻 / 议题 / 发布 / 翻译 / 致谢
- 跨宿主：Claude Code · WorkBuddy · Cursor · Codex
- 标准：Skills 1.0 + MCP 0.4
- 许可：MIT，自由二次开发

## 1. D-1 发布前准备（必须做完）

| 项 | 说明 | 负责 |
|---|---|---|
| 仓库名 | `chaoyi_agent`（建议独立 repo，与归档的直播代码解耦） | 你 |
| Repo Topics | `ai-agents`, `skills`, `mcp`, `open-source`, `community`, `developer-tools`, `llm`, `automation`, `chinese`, `agent-framework` | 你 |
| About | 「让每一个小社群都拥有数字社工 · 跨宿主开源 Skill 库（Skills 1.0 + MCP）· MIT」 | 你 |
| Release | `v0.1.0`：5 Skills + 模板 + README + 索引 | 你 |
| 预埋 Issue | 3–5 个「good first issue」（如：新增某社群 Skill、补英文 README） | 你 |
| Discussions | 开「想被 agent 化的社群场景」投票帖，引 UGC | 你 |
| 截图/GIF | 一个 30 秒 demo：把 issue-triage Skill 接入 WorkBuddy 跑一遍 | 你 |

## 2. 七日作战日历

| 日 | 主阵地 | 动作 | 预估新增 star |
|---|---|---|---|
| D0 | 掘金 + V2EX + 知乎 | 长文《我把社群最重复的 5 件事，做成了开源 Skill》+ 帖 | 120–220 |
| D1 | Show HN + Reddit r/selfhosted + Dev.to | “Chaoyi Agent: open-source skill library to agent-ify your community” | 150–300 |
| D2 | X(Twitter) 线程 + 微信公众号 | 中英双语线程 + 公众号解读；@ 相关 OSS 维护者 | 100–200 |
| D3 | B 站 / YouTube | 3 分钟 demo：社区维护者的一天被 5 个 Skill 接管 | 80–160 |
| D4 | GitHub Trending 窗口 + 互动 | 集中回复 Issue/Discussions，AMA；提交 awesome-agents 列表 PR | 120–250 |
| D5 | 小红书 + Product Hunt | 「打工人也能给社群配数字社工」+ PH launch | 90–180 |
| D6 | 收尾 + KOL 转发 | 汇总战报、致谢贡献者、邀约合作社群 | 60–140 |

**合计区间：720–1450**，进取执行 + 踩中 Trending 可稳过 1000。

## 3. 渠道要点（浓缩）

- **掘金/知乎**：重「方法论 + 代码可跑」，放完整 README 与 demo 链接，附 GitHub。
- **Show HN / Reddit**：重「why + 开源 + 自托管」，强调 MIT / 跨宿主 / 标准兼容。
- **X 线程**：钩子用「你的社群需要一个数字社工吗？这 5 个开源 Skill 免费给你」。
- **B 站/YouTube**：可视化 demo 是转化关键，30 秒看完想 star。
- **Product Hunt**：tagline 限 60 字，突出「community agent toolkit, open-source」。

## 4. 内容弹药清单（10 条，可提前备好）

1. 《为什么小社群最需要 agent，却最用不起》
2. 《5 个 Skill 拆解：入驻/议题/发布/翻译/致谢怎么省下 80% 运营时间》
3. 《Skills 1.0 与 MCP 到底什么关系（一文讲清跨宿主）》
4. 《我把 issue-triage 接入 WorkBuddy 的完整过程》
5. 《社群 agent 化的 30 天路线（附模板）》
6. 《中文开源项目如何吃海外 agent 流量》
7. 《从 0 到 1000 star：我们的渠道日历》
8. 《一个 Skill 的标准写法（_template 讲解）》
9. 《为什么我们选 MIT 而不是 AGPL》
10. 《招募：你最想被 agent 化的社群场景》

## 5. KPI 看板（每日盯）

- 日新增 star / fork / Issue / Discussions 数
- 各渠道 referral（GitHub Insights → traffic）
- Issue 首次响应时长（验证「我们真在做社区」）

## 6. 应急

- **首日低迷**：把 hook 从「框架」改成「具体痛点」（如「GitHub Issue 堆成山？这个开源 Skill 帮你 triage」）。
- **被质疑「又是个套壳」**：强调 5 个 Skill 全可运行 + 标准兼容 + MIT，附 demo。
- **海外冷启动慢**：优先攻 r/selfhosted + Show HN，这两处对「开源自托管工具」最友好。

## 7. 合规红线（与既有文档一致）

- 开源代码分发**不需要**直播类牌照；本方向本就不涉经营资质。
- Skill **不得**含绕过 CoC、伪造贡献、刷量等能力（见 `skills/README.md` 红线）。
- 不替用户执行破坏性动作，所有对外动作 HITL。

> 注：本作战书的渠道/节奏继承自已归档的《潮驿直播一周千星战术战略书》，仅替换定位与素材；原文档存于 `archive/` 供参考。
