# 潮驿 Skills 库

一套面向**开源 / 开发者 / 兴趣社群**的即用型智能体技能（Skills）。
每个目录是一个独立 Skill，遵循 [Skills 1.0](https://agentskills.io) 规范，可直接被支持该规范的宿主加载。

## 已发布（首发 5 个）

| 目录 | 名称 | 用途 |
|---|---|---|
| `community-onboarding/` | 贡献者入驻 | 设计入驻流程、good first issue 流水线、欢迎话术 |
| `issue-triage/` | 议题管家 | 标记 / 优先级 / 去重 / 起草回复议题 |
| `release-notes/` | 发布说明 | 从 conventional commits 生成 release notes 与 changelog |
| `doc-localization/` | 文档本地化 | 多语言翻译协调：抽取 / 派发 / 跟踪 / 产出 PR |
| `contributor-recognition/` | 贡献致谢 | 聚合贡献数据、起草致谢、生成荣誉墙 |

## 接入方式

宿主将 Skill 目录放入其 skills 路径即可：

```bash
# WorkBuddy（用户级）
cp -r issue-triage ~/.workbuddy/skills/

# Claude Code
cp -r issue-triage ~/.claude/skills/

# Cursor
cp -r issue-triage .cursor/skills/
```

放入后，用自然语言描述意图（如「把本周 issue 分类并起草回复」）即可触发对应 Skill。

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
- 保持**人在回路（HITL）**：涉及对外发言、合并、封禁等动作，Skill 只产出草稿/建议，由人确认。

## 合规红线（贡献前必读）

Skill **不得**包含以下能力：
- 绕过社区行为准则（CoC）或平台规则；
- 伪造、篡改贡献记录或统计数据；
- 自动化刷 star / 刷 issue / 刷 PR 等操纵行为；
- 未经同意抓取或外泄社区成员隐私。

违反上述任一条的 Skill 将被拒绝合并并从库移除。
