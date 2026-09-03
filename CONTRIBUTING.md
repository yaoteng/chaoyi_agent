# 贡献指南（Contributing）

欢迎为 **潮驿 Agent** 贡献 Skill、示例与文档。我们尤其欢迎来自真实社群的「agent 化」改造记录。

## 如何新增一个 Skill

1. 复制脚手架：
   ```bash
   cp -r skills/_template skills/your-skill-name
   ```
2. 编辑 `skills/your-skill-name/SKILL.md`：
   - `name`：kebab-case，全局唯一；
   - `description`：**写清触发场景（when to use）**——这是宿主判断是否加载该 Skill 的唯一依据；
   - 正文用「When to use / Steps / Output / Guardrails」四段式；
   - 建议补充 `version` / `license` / `compatible_hosts` / `standards`。
3. 在 `skills/README.md` 的表格中加一行。
4. **实测**：复制到宿主路径（`~/.workbuddy/skills/`、`~/.claude/skills/`、` .cursor/skills/` 之一），用自然语言触发验证。
5. 提 PR。

## 合规红线（硬性，违反即拒）

Skill **不得**包含以下能力：
- 绕过社区行为准则（CoC）或平台规则；
- 伪造、篡改贡献记录或统计数据；
- 自动化刷 star / issue / PR 等操纵行为；
- 未经同意抓取或外泄社区成员隐私；
- 替代人工执行对外发言 / 合并 / 封禁等破坏性动作（应只出草稿，必须 HITL）。

详见 [skills/README.md](skills/README.md) 的「合规红线」一节。

## 行为准则

本社区遵循 Contributor Covenant：友好、包容、就事论事。不欢迎任何形式的骚扰或歧视。
