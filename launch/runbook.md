# 潮驿 Agent · 一周千星作战 Runbook（执行版）

> 本文是 `潮驿Agent一周千星战术战略书.md` 的**可操作执行版**。战略书讲"为什么 / 打法"，本文讲"每天具体做什么、发什么、盯什么指标"。
> 仓库发布后，按 D-1 → D0~D6 顺序执行。**所有发帖文案见 `launch/posts/`**。

---

## 0. 发布前置 Gate（务必先过）

| 检查项 | 命令 / 动作 | 状态 |
|---|---|---|
| `gh` 已登录 | `gh auth status` → 显示 `Logged in to github.com` | ☐ |
| git 身份已设 | `git config user.name` / `user.email` 非空 | ☐ |
| 仓库已发布 | 运行 `bash scripts/publish_to_github.sh`，得到 `https://github.com/yaoteng/chaoyi_agent` | ☐ |
| 仓库元信息 | About 文案 + 12 Topics + Release v0.1.0 已建 | ☐ |
| 一张主图 | `docs/screenshot.png`（README 顶部示意图）已放 | ☐ |
| 一个 demo | 30 秒演示视频/动图（见 `demo-script.md`）已录 | ☐ |

> 若 `gh` 在本机未登录：先 `gh auth login`（浏览器授权，选 **Public repo** 权限）。发布脚本会自动 `git init`+提交+建仓+打 tag+发 Release。

---

## 1. 每日节奏总览

| 日 | 主战场 | 核心动作 | 当日 star 目标 | 累计目标 |
|---|---|---|---|---|
| D-1 | 备料 | 终稿 README/主图/demo；把 `posts/` 10 篇复制到各平台草稿箱 | — | — |
| D0 | 中文技术圈 | 掘金长文 + V2EX + 知乎 | 120–220 | 120–220 |
| D1 | 海外 HN/Reddit | Show HN + Reddit(r/selfhosted,r/opensource) + Dev.to | 180–320 | 300–540 |
| D2 | X / 公众号 | X 长线程 + 微信公众号 | 120–230 | 420–770 |
| D3 | 视频 | B站 30 秒 demo + 评论区置顶链接 | 80–170 | 500–940 |
| D4 | 互动 + 扩散 | 回复所有评论 / AMA / 提交 awesome 清单 | 100–180 | 600–1120 |
| D5 | 小红书 / PH | 小红书图文 + Product Hunt 预热 | 60–130 | 660–1250 |
| D6 | 收尾 | 感谢帖 + 数据复盘 + 邀请贡献 | 50–100 | **710–1350** |

> 区间来自战略书测算；进取执行 + 内容质量高，D6 累计可破 1000。

---

## 2. D-1 备料清单（发布当天之前做完）

- [ ] README 顶部放一张架构/场景示意图（`docs/screenshot.png`），让访客 3 秒看懂。
- [ ] 录制 30 秒 demo（RustyCache 样例跑通 5 个 Skill，见 `demo-script.md`），导出 `demo.mp4` + 抽一帧做封面。
- [ ] 把 `posts/` 下 10 篇**各复制到对应平台草稿箱**，只差"点发布"，避免当天手忙脚乱。
- [ ] 准备 3 条"钩子"短视频脚本（15s/30s/60s 各一），D3 用。
- [ ] 列一份"潜在助力名单"（好友 / 同行 KOL / 社区群），D0–D1 私信请他们来 star（**不要刷量，真实邀请**）。
- [ ] 设好 KPI 追踪表（`kpi-tracker.md`），每日 22:00 填一次。

---

## 3. 每日动作（D0–D6）

### D0 · 中文技术圈（早晨 9–11 点发，踩通勤流量）
1. **掘金**：发 `posts/01_juejin.md`（长文，带图 3–5 张）。同步到"首页推荐"靠标题 + 首图。
2. **V2EX**：发 `posts/02_v2ex.md` 到「分享创造 / 程序员」节点。
3. **知乎**：发 `posts/03_zhihu.md` 回答"有哪些值得推荐的开源 AI Agent 项目？"或自问自答。
4. 当晚：在掘金/知乎评论区主动回复前 20 条，引导到仓库。

### D1 · 海外 HN / Reddit（北京时间晚 23 点 / 美西早 8 点，踩 HN 高峰）
1. **Show HN**：发 `posts/04_showhn.md`。
2. **Reddit**：`r/selfhosted` + `r/opensource` + `r/rust`（若样例用 Rust）各发 `posts/05_reddit.md`，遵守各版规则（勿跨版重复刷）。
3. **Dev.to**：发 `posts/06_devto.md`（可同步 Medium）。
4. 关键：在 HN/Reddit 评论里**真诚回答技术细节**，不 defend、不刷。

### D2 · X / 公众号
1. **X（推特）**：发 `posts/07_x_thread.md` 长线程（5–8 条），带 `#OpenSource #AIagents` 标签，@ 相关开源大佬（别 spam）。
2. **微信公众号**：发 `posts/08_wechat.md`（可配 demo 动图）。
3. 把 D0/D1 的高赞评论截图，作为"社区反馈"发 X 置顶。

### D3 · 视频
1. 发 B站 `posts/demo-script.md` 对应的 30 秒视频，标题带关键词"开源 Agent / 社群智能体"。
2. 视频简介 + 评论区置顶仓库链接。
3. 同一视频截 15s 版发小红书（D5）、X（D2 已发文字，可补视频）。

### D4 · 互动 + 扩散
1. **回复全部评论**（GH Issues/讨论区 + 各平台），重点问题转成 Issue/FAQ。
2. 在 r/selfhosted 等做轻量 AMA（"Ask Me Anything"）。
3. 向 `awesome-agents`、`awesome-mcp`、`awesome-selfhosted` 等清单提 PR（附中文说明）。

### D5 · 小红书 / Product Hunt
1. **小红书**：发 `posts/09_xiaohongshu.md` 图文（年轻化、emoji、步骤感）。
2. **Product Hunt**：发 `posts/10_producthunt.md`（标题 + 一句话 + 首图 + 早期支持者点赞）。

### D6 · 收尾
1. 发一条"一周小结"感谢帖（X + 掘金），公布 star 数、Top 贡献者、下一步路线图。
2. 把高频问题整理进 README 的 FAQ / Discussions。
3. 邀请 3–5 位贡献者认领 `good first issue`。

---

## 4. 应急方案

| 情况 | 应对 |
|---|---|
| D0 流量低于期望 | 追加 2–3 个垂类社区（如"少数派""HelloGitHub"），发精简版；私信名单全力请 star |
| HN 被沉 | 改投 `r/opensource` 精选 + Dev.to 置顶；次日二刷 Show HN |
| 被质疑"又是套壳" | 直接贴 `skills/` 源码截图 + 与 Dify/LangChain 差异表，开源透明最硬 |
| 出现刷量/水军嫌疑 | 立即声明"拒绝刷量"，只认真实贡献；宁可慢不可脏 |
| star 卡在 ~600 | 启动"贡献者激励计划"：前 10 位提 PR 者进 README 贡献墙 |

---

## 5. 合规红线（贯穿全程）
- 开源代码分发**不需要**直播类牌照；但**不得以开源为名实际运营无牌公开直播服务**（本项目已彻底归档直播代码，无此风险）。
- Skill 内容不得含绕过社区行为准则、伪造贡献、自动化刷量等能力（见 `CONTRIBUTING.md`）。
- 所有数据/截图须脱敏，不得泄露用户隐私。

---

## 6. 发布后必做（工程侧）
- 开 `Discussions` 作为"社区 agent 化"问答区。
- 建 `good first issue` 若干（翻译某 Skill、补一个垂类 Skill）。
- 每周发一个 patch Release，保持活跃度（GitHub 活跃度影响 Trending）。
