# D0 三连首发执行包（掘金 / 开源中国 / 知乎）

> 本文件用于 D0 当天快速复制粘贴。所有正文均来自 `launch/posts/01~03.md`，已对齐直播社区口径。

---

## 前置：推送代码

在本地执行（沙箱无法访问 github.com，需你手动 push）：

```bash
cd chaoyi_agent
git pull --rebase origin main   # 若远程有更新先合并
git push origin main
```

推送后确认仓库文件都在：
- `launch/demo.mp4` — 30 秒 demo 视频
- `launch/demo_cover.png` — demo 封面
- `launch/social-preview.png` — GitHub 社交预览图（1280×640）

GitHub 设置路径：Settings → General → Social preview → Upload `social-preview.png`。

---

## 通用素材

- 仓库地址：`https://github.com/yaoteng/chaoyi_agent`
- Slogan：潮驿 Agent：5 个开源 Skill，让直播社区月运营工时从 40h 降到 6h。
- 关键词：开源、AI Agent、直播、直播社区、MCP、社区运营
- 合规红线：未成年人保护 / 打赏限额 / 版权曲库 / 内容安全审核

---

## ① 掘金（D0 09:30）

**文件**：`launch/posts/01_juejin.md`

- **标题**：我把一个直播社区的月运营工时，从 40h 压到了 6h
- **标签**：开源、AI-Agent、直播、直播社区、MCP、社区运营
- **类型**：长文
- **配图建议**（3–5 张）：
  1. `social-preview.png` 作为头图
  2. `skills/README.md` 里的 5 Skill 表格截图
  3. `demo_cover.png` 作为 demo 封面
  4. 文中终端命令那块可配 `demo.mp4` 的 GIF/视频
- **摘要**：不是靠招人，也不是靠外包，而是给直播社区装了一套“数字社工”——一组开源 Skill。

正文直接复制 `launch/posts/01_juejin.md` 第 8–57 行。

---

## ② 开源中国 OSChina（D0 10:30）

**文件**：`launch/posts/02_oschina.md`

分两步：

### 2a) 提交开源项目库

- 项目名：潮驿 Agent（Chaoyi Agent）
- 一句话描述：5 个开源 Skill，让直播社区月运营工时从 40h 降到 6h
- 项目地址：`https://github.com/yaoteng/chaoyi_agent`
- 标签/分类：开源、AI Agent、直播、社区运营、MCP
- Logo：可先用 `social-preview.png` 裁剪左侧区域，或直接上传 `demo_cover.png`

### 2b) 同步发博客长文

- **标题**：我把一个直播社区的月运营工时，从 40h 压到了 6h（开源 Skill 库）
- **正文**：复制 `launch/posts/02_oschina.md` 第 8–20 行
- **配图**：`social-preview.png` + `demo_cover.png`

---

## ③ 知乎（D0 14:00）

**文件**：`launch/posts/03_zhihu.md`

- **形式**：搜索问题“有哪些值得推荐的开源 AI Agent 项目？”，在该问题下回答；也可自问自答。
- **回答标题/首句**：推荐一个可能被低估的：潮驿 Agent（Chaoyi Agent）。
- **话题标签**：开源、人工智能、AI Agent、直播、社区运营
- **正文**：复制 `launch/posts/03_zhihu.md` 第 6–33 行
- **配图**：`social-preview.png` 放首图，`demo_cover.png` 放末尾 CTA

---

## D0 时间线（参考）

| 时间 | 动作 |
|---|---|
| 09:30 | 掘金长文发布 |
| 10:30 | 开源中国提交项目库 + 博客发布 |
| 14:00 | 知乎回答发布 |
| 15:00 | 把三处链接汇总到 `kpi-tracker.md`，并截图留存 |
| 晚间 | 在三平台回复评论，重点回应“和 Coze/Dify 区别”“MCP 怎么用”类问题 |

---

## 发布后 30 分钟必做

1. 在三篇内容下各留一条置顶评论：仓库地址 + “demo 视频在 `launch/demo.mp4`”。
2. 把 `kpi-tracker.md` 的 D0 行填上真实 star/阅读/互动数字。
3. 截三张发布页的图，存到 `launch/screenshots/d0/` 备后续复盘。
