# 潮驿 Agent · 一周冲 1000 Star 战术战略书

> ✅ **定位确认（2026-09-06）**：chaoyi（潮驿/炒意）是**直播社区类品牌**，本项目即其 **agent 化工具箱**，定位「直播社区运营 agent 化」。本作战书的**渠道 / 节奏方法论可沿用**，hook 与素材统一为「直播社区 / 数字社工」（如：主播入驻、直播策划、互动运营、内容风控、观众增长）。下文已按此口径改写；详细转向记录见《决策确认与执行记录》第六节。

> 配套《潮驿项目重新定位方案》《潮驿Agent项目竞品分析》。本作战书沿用此前直播方向的**渠道与节奏方法论**，但 hook 与素材全部替换为「直播社区运营 agent 化」。

## 0. 战略支点

**一句话定位（hook）**：
> 「让每一个直播社区，都能拥有自己的数字社工。」
> 一套 MIT 开源、跨宿主（Claude Code / WorkBuddy / Cursor）、即插即用的**直播社区运营智能体技能库**。

**为什么能冲星**：
- Agent/Skill 是 2026 最大确定性赛道，但「直播社区运营 agent 化」是蓝海（竞品分析已确认：无统治级开源项目）。
- 我们首发就是**可运行、可复制的 5 个直播社区 Skills + MCP 网关 + 模板 + 索引**，不是 PPT。
- 复用已验证打法：你方直播社区 / 美食直播经验、掘金过审长文、跨端工程经验。
- 中文优先 + 标准兼容（Skills 1.0 / MCP 0.4）→ 同时吃中文直播 / 社区运营从业者与海外 agent 生态两波流量。

**可量化卖点（写进 README/About）**：
- 5 个即用 Skill：主播入驻 / 直播策划 / 互动运营 / 内容风控 / 观众增长
- 跨宿主：Claude Code · WorkBuddy · Cursor · Codex
- 标准：Skills 1.0 + MCP 0.4
- 许可：MIT，自由二次开发

## 1. D-1 发布前准备（必须做完）

| 项 | 说明 | 负责 |
|---|---|---|
| 仓库名 | `chaoyi_agent`（建议独立 repo，与归档的直播代码解耦） | 你 |
| Repo Topics | `ai-agents`, `skills`, `mcp`, `open-source`, `livestreaming`, `community`, `llm`, `automation`, `chinese`, `agent-framework` | 你 |
| About | 「让每一个直播社区都拥有数字社工 · 跨宿主开源 Skill 库（Skills 1.0 + MCP）· MIT」 | 你 |
| Release | `v0.1.0`：5 Skills + 模板 + README + 索引 | 你 |
| 预埋 Issue | 3–5 个「good first issue」（如：新增某垂类直播社区 Skill、补英文 README） | 你 |
| Discussions | 开「想被 agent 化的直播社区场景」投票帖，引 UGC | 你 |
| 截图/GIF | 一个 30 秒 demo：把 streamer-onboarding Skill 接入 WorkBuddy 跑一遍 | 你 |

## 2. 七日作战日历

| 日 | 主阵地 | 动作 | 预估新增 star |
|---|---|---|---|
| D0 | 掘金 + 开源中国 + 知乎 | 长文《我把直播社区最重复的 5 件事，做成了开源 Skill》+ 帖 | 120–220 |
| D1 | Show HN + Reddit r/selfhosted + Dev.to | "Chaoyi Agent: open-source skill library to agent-ify your live-streaming community" | 150–300 |
| D2 | X(Twitter) 线程 + 微信公众号 | 中英双语线程 + 公众号解读；@ 相关 OSS 维护者 | 100–200 |
| D3 | B 站 / YouTube | 3 分钟 demo：社区运营的一天被 5 个 Skill 接管 | 80–160 |
| D4 | GitHub Trending 窗口 + 互动 | 集中回复 Issue/Discussions，AMA；提交 awesome-agents 列表 PR | 120–250 |
| D5 | 小红书 + Product Hunt | 「打工人也能给直播社区配数字社工」+ PH launch | 90–180 |
| D6 | 收尾 + KOL 转发 | 汇总战报、致谢贡献者、邀约合作社区 | 60–140 |

**合计区间：720–1450**，进取执行 + 踩中 Trending 可稳过 1000。

## 3. 渠道要点（浓缩）

- **掘金/知乎**：重「方法论 + 代码可跑」，放完整 README 与 demo 链接，附 GitHub。
- **Show HN / Reddit**：重「why + 开源 + 自托管」，强调 MIT / 跨宿主 / 标准兼容。
- **X 线程**：钩子用「你的直播社区需要一个数字社工吗？这 5 个开源 Skill 免费给你」。
- **B 站/YouTube**：可视化 demo 是转化关键，30 秒看完想 star。
- **Product Hunt**：tagline 限 60 字，突出「live-streaming community agent toolkit, open-source」。

## 4. 内容弹药清单（10 条，可提前备好）

1. 《为什么直播社区最需要 agent，却最用不起》
2. 《5 个 Skill 拆解：入驻/策划/互动/风控/增长怎么省下 80% 运营时间》
3. 《Skills 1.0 与 MCP 到底什么关系（一文讲清跨宿主）》
4. 《我把 streamer-onboarding 接入 WorkBuddy 的完整过程》
5. 《直播社区 agent 化的 30 天路线（附模板）》
6. 《中文开源项目如何吃海外 agent 流量》
7. 《从 0 到 1000 star：我们的渠道日历》
8. 《一个 Skill 的标准写法（_template 讲解）》
9. 《为什么我们选 MIT 而不是 AGPL》
10. 《招募：你最想被 agent 化的直播社区场景》

## 5. KPI 看板（每日盯）

- 日新增 star / fork / Issue / Discussions 数
- 各渠道 referral（GitHub Insights → traffic）
- Issue 首次响应时长（验证「我们真在做社区」）

## 6. 应急

- **首日低迷**：把 hook 从「框架」改成「具体痛点」（如「新主播入驻 21 天？这个开源 Skill 帮你 9 天搞定」）。
- **被质疑「又是个套壳」**：强调 5 个 Skill 全可运行 + 标准兼容 + MIT，附 demo。
- **海外冷启动慢**：优先攻 r/selfhosted + Show HN，这两处对「开源自托管工具」最友好。

## 7. 合规红线（与既有文档一致）

- 开源代码分发**不需要**直播类牌照；本方向是运营工具箱，不实际运营无牌公开直播服务。
- Skill **不得**含绕过直播/平台合规（未成年人保护、打赏限额、版权、内容安全）、伪造直播/观众数据、刷量等能力（见 `skills/README.md` 红线）。
- 不替用户执行破坏性动作，所有对外动作 HITL。

> 注：本作战书的渠道/节奏继承自已归档的《潮驿直播一周千星战术战略书》，仅替换定位与素材；原文档存于 `archive/` 供参考。
