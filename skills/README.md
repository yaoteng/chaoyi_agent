# 潮驿 Skills 库

一套面向**分销 / 快消 / 渠道业务**的即用型智能体技能（Skills）。
每个目录是一个独立 Skill，遵循 [Skills 1.0](https://agentskills.io) 规范，可直接被支持该规范的宿主加载。

> 这些 Skill 是「潮驿 Agent」项目分发 SaaS（经销商多渠道触达系统）能力的 agent 化切片——
> 把经销商入驻、多渠道触达、渠道巡检、订单库存对账、拜访计划这些重复又吃人的活，交给可编排的 Skill。

## 已发布（首发 5 个）

| 目录 | 名称 | 用途 |
|---|---|---|
| `distributor-onboarding/` | 经销商入驻引导 | 签约→资质→系统开通→培训→首单的标准化流水线 |
| `reach-campaign/` | 多渠道触达编排 | 微信/企微/短信/电话多波次触达的节奏与话术编排 |
| `channel-inspection/` | 渠道健康巡检 | 动销/库存/回款/窜货指标打分、异常定位与处置建议 |
| `order-inventory-reconcile/` | 订单库存对账 | 订单/出库/库存/回款四流对账，找差异、缺货、坏账风险 |
| `visit-plan/` | 拜访计划编排 | 按优先级/地理/产出排业务员拜访路线与话术要点 |

## 接入方式

宿主将 Skill 目录放入其 skills 路径即可：

```bash
# WorkBuddy（用户级）
cp -r reach-campaign ~/.workbuddy/skills/

# Claude Code
cp -r reach-campaign ~/.claude/skills/

# Cursor
cp -r reach-campaign .cursor/skills/
```

放入后，用自然语言描述意图（如「给华东区欠账 60 天以上的经销商排一轮回款催办触达」）即可触发对应 Skill。
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
- 保持**人在回路（HITL）**：涉及对外发送、改账、清退等动作，Skill 只产出草稿/建议，由人确认。

## 合规红线（贡献前必读）

Skill **不得**包含以下能力：
- 绕过短信 / 外呼合规（频次、退订、时段）或平台规则；
- 伪造、篡改经营 / 财务 / 触达数据；
- 自动化刷量、骚扰式群发等操纵行为；
- 未经同意抓取或外泄客户隐私（联系方式、地址、资质）。

违反上述任一条的 Skill 将被拒绝合并并从库移除。
