---
平台: 开源中国（OSChina）
最佳发布时间: D0 10:30
形式: ① 提交开源项目到「开源项目」库（oschina.net/project）② 同步发一篇博客长文
标题建议: 我把一个直播社区的月运营工时，从 40h 压到了 6h（开源 Skill 库）
---

最近把直播社区的运营杂活（主播入驻、直播策划、直播间互动、内容风控、观众运营）用一组开源 Skill 自动化了，月运营工时从 ~40h 降到 ~6h。

项目叫 **潮驿 Agent（Chaoyi Agent）**，定位不是又一个 Agent 框架，而是"帮直播社区低成本 agent 化"的工具箱：

- 首发 5 个直播社区 Skill：主播入驻引导 / 直播内容策划 / 直播间互动运营 / 社区内容风控 / 观众运营复盘
- 兼容 Skills 1.0 + MCP 0.4，Claude Code / Cursor / WorkBuddy / Codex 都能直接跑
- 纯 SKILL.md + 模板，MIT，零依赖，fork 即改
- 自带一个完整样例（虚构美食直播社区"食光小馆直播社区"），演示怎么把运营工时压下来

仓库：https://github.com/yaoteng/chaoyi_agent

欢迎在「开源项目」里点个收藏 / 推荐，也欢迎提 PR 加第六个垂类直播社区 Skill。
