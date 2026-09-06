# 潮驿 Skills 库

一套面向**直播社区运营**的即用型智能体技能（Skills）。
每个目录是一个独立 Skill，遵循 [Skills 1.0](https://agentskills.io) 规范，可直接被支持该规范的宿主加载。

> 这些 Skill 是「潮驿 Agent」项目（直播社区品牌 chaoyi 的 agent 化工具箱）能力的切片——
> 把主播入驻、直播策划、直播间互动、内容风控、观众运营这些重复又吃人的活，交给可编排的 Skill。

## 已发布（首发 5 个）

| 目录 | 名称 | 用途 |
|---|---|---|
| `streamer-onboarding/` | 主播入驻引导 | 签约→实名资质→推流配置→首播策划→开播培训的标准化流水线 |
| `live-show-plan/` | 直播内容策划与排期 | 选题库 / 直播排期 / 脚本骨架 / 多平台分发计划 |
| `live-room-ops/` | 直播间互动运营 | 弹幕 / 礼物 / 抽奖 / 连麦 / 粉丝团的互动脚本、话术与应急 SOP |
| `community-moderation/` | 社区内容审核与风控 | 违规判定 / 五档分级处置 / 举报闭环 / 直播合规红线 |
| `audience-growth/` | 观众运营与数据复盘 | 用户分层 / 留存召回 / 活动运营 / 直播数据复盘报告 |

## 接入方式

宿主将 Skill 目录放入其 skills 路径即可：

```bash
# WorkBuddy（用户级）
cp -r streamer-onboarding ~/.workbuddy/skills/

# Claude Code
cp -r streamer-onboarding ~/.claude/skills/

# Cursor
cp -r streamer-onboarding .cursor/skills/
```

放入后，用自然语言描述意图（如「给新签的 3 个美食主播按 streamer-onboarding 生成入驻阶梯，并衔接首播排期」）即可触发对应 Skill。
也可通过 [`../mcp-server/`](../mcp-server/) 网关统一加载，Agent 经 MCP 调用，无需逐个复制目录。

## 新技能脚手架

复制 `_template/` 并按其 `SKILL.md` 的字段说明改写：

```bash
cp -r _template my-new-skill
# 编辑 my-new-skill/SKILL.md 的 name / description / 正文
```

## 规范要点

- `SKILL.md` 顶部 YAML frontmatter **必须**包含 `name` 与 `description`；建议补充 `version` / `license` / `compatible_hosts` / `standards`。
- `description` 要写清**触发场景**（when to use），这是宿主决定是否注入该 Skill 的依据。
- 正文用「When to use / Steps / Output / Guardrails」四段式，便于人和模型都读懂。
- 保持**人在回路（HITL）**：涉及对外发送、封禁、清退等动作，Skill 只产出草稿/建议，由人确认。

## 合规红线（贡献前必读）

Skill **不得**包含以下能力：
- 绕过直播 / 平台合规（未成年人保护、打赏限额、版权曲库、内容安全审核）；
- 伪造、篡改直播数据（观看 / 互动 / 转化 / 礼物）；
- 自动化刷量、骚扰式群发、诱导非理性消费等操纵行为；
- 未经同意抓取或外泄主播 / 观众隐私（实名、联系方式、画像）。

违反上述任一条的 Skill 将被拒绝合并并从库移除。
