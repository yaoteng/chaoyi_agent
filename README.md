# 潮驿 Chaoyi Agent

> 面向**分销 / 快消 / 渠道业务**的 **Agent / Skill 工具箱 + 改造方法论**。
> 让每一个分销团队，都能拥有自己的「数字业务社工」。

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/yaoteng/chaoyi_agent?style=social)](https://github.com/yaoteng/chaoyi_agent)
[![Skills 1.0](https://img.shields.io/badge/standard-Skills%201.0-blue.svg)](https://agentskills.io)
[![MCP](https://img.shields.io/badge/protocol-MCP%200.4-blue.svg)](https://modelcontextprotocol.io)

---

## 这是什么

**潮驿**不再是一个直播产品，而是一个**帮助分销业务完成 agent 化改造**的开源项目。

我们观察到：2026 年是「智能体上岗元年」，但大部分分销 / 快消 / 渠道团队**没有能力、也没有预算**去搭建自己的智能体。大厂平台（如 Coze）闭源、不可自托管；通用框架（LangChain / Dify）太重、不解决「经销商入驻、多渠道触达、渠道巡检、订单对账、拜访排程」这些具体又吃人的日常运营。

潮驿把分销最重复的运营动作，封装成一套**可即插即用、可自托管、跨宿主运行**的 Skills：

| Skill | 它替分销团队做什么 |
|---|---|
| `distributor-onboarding` | 经销商签约→资质→系统开通→培训→首单的标准化流水线 |
| `reach-campaign` | 微信 / 企微 / 短信 / 电话的多波次触达节奏与话术编排 |
| `channel-inspection` | 动销 / 库存 / 回款 / 窜货指标打分、异常定位与处置建议 |
| `order-inventory-reconcile` | 订单 / 出库 / 库存 / 回款四流对账，找差异、缺货、坏账风险 |
| `visit-plan` | 按优先级 / 地理 / 产出排业务员拜访路线与话术要点 |

> 这 5 个就是「数字业务社工」的雏形——它们解决的是分销团队**人少事多、客户易流失、对账扯皮、拜访凭感觉**的真实痛点。

## 为什么不同

- **场景聚焦**：只做「分销业务 agent 化」，不做通用 AGI。每个 Skill 都来自真实分销场景。
- **标准兼容**：所有 Skill 遵循 [Skills 1.0](https://agentskills.io) 规范，并可通过 MCP 0.4 暴露工具；**跨宿主运行**——Claude Code / WorkBuddy / Cursor / Codex 直接加载。
- **零依赖运行时**：`mcp-server/` 用纯 Python 标准库实现，无需安装任何第三方包，契合轻量自托管。
- **中文优先 + 业务语料**：文档、示例、话术默认中文，且用分销术语而非通用 AI 黑话。
- **方法论即产品**：配套《30 天分销 agent 化》手册，不只给工具，给落地路径。
- **MIT 开源**：自由使用、二次开发、再分发。

## 快速开始

把某个 Skill 接入你的智能体（以 WorkBuddy / Claude Code 为例）：

```bash
# 方式一：直接放入宿主的 skills 目录
cp -r skills/reach-campaign ~/.workbuddy/skills/        # WorkBuddy（用户级）
# 或 cp -r skills/reach-campaign .claude/skills/        # Claude Code
# 或 cp -r skills/reach-campaign .cursor/skills/        # Cursor

# 方式二（推荐，不污染宿主目录）：通过 MCP 网关统一加载
# 见 mcp-server/README.md：在宿主的 mcp 配置里指向 python mcp-server/server.py
# 网关自动把 skills/ 下全部 SKILL.md 暴露为 MCP 工具，按需注入上下文
```

导入后，对智能体说「给华东区账期超 60 天的经销商排一轮回款催办触达」，它就会调用 `reach-campaign` 技能。

## 示例：分销业务 agent 化改造

想知道这些 Skill 落到真实分销团队是什么样？看 [examples/reference-distribution](examples/reference-distribution/README.md)——一家 1,200 家下游门店的快消分销商，用潮驿 5 个 Skill 把月度运营工时从约 40h 压到约 6h 的完整记录（含 before/after 与可直接复制的调用话术）。

## 仓库结构

```
chaoyi_agent/
├─ README.md                     # 本文件
├─ LICENSE                       # MIT
├─ skills/                       # ★ Skills 库（首发 5 个分销技能）
│  ├─ README.md                  # 技能索引与接入说明
│  ├─ _template/                 # 新技能脚手架模板
│  ├─ distributor-onboarding/    # 经销商入驻引导
│  ├─ reach-campaign/            # 多渠道触达编排
│  ├─ channel-inspection/        # 渠道健康巡检
│  ├─ order-inventory-reconcile/ # 订单库存对账
│  └─ visit-plan/                # 拜访计划编排
├─ mcp-server/                   # ★ Agent 运行时：零依赖 MCP 网关，把 Skills 暴露为工具
│  ├─ server.py                  # 纯标准库实现（initialize / tools/list / tools/call）
│  └─ README.md                  # 运行与接入（Claude Code / Cursor）
├─ agents/                       # ★ 多角色 Agent 模板（编排 Skills 成常驻数字业务社工）
│  ├─ README.md                  # 角色索引
│  ├─ onboarding-guide/          # 入驻向导 → distributor-onboarding
│  ├─ reach-steward/             # 触达管家 → reach-campaign
│  ├─ channel-inspector/         # 渠道巡检员 → channel-inspection + order-inventory-reconcile
│  └─ visit-coordinator/         # 拜访统筹 → visit-plan
├─ examples/                     # 真实改造样例（活文档 / demo）
│  └─ reference-distribution/    # 一家快消分销商的 agent 化 before/after
├─ scripts/                      # 发布脚本 + Skills 格式校验
├─ 潮驿项目重新定位方案.md        # 战略定位（为何从直播转向 agent）
├─ 潮驿Agent项目竞品分析.md      # 竞品分析（Agent/Skill 赛道）
├─ 潮驿Agent一周千星战术战略书.md # 开源推广作战书
├─ 决策确认与执行记录.md          # 关键决策与执行落点（含 2026-09-05 分销定位转向）
└─ archive/                      # 早期「直播方向」文档（已归档，仅供参考）
```

## 已上线

🔗 **https://github.com/yaoteng/chaoyi_agent** —— 公开仓库，代码 / MIT License / v0.1.0 Release 均已上线，已配置 11 个 Topics 与仓库描述。

### 架构一览

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 230" width="100%" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">
  <text x="10" y="26" font-size="15" font-weight="700" fill="#1f2328">潮驿 Chaoyi Agent · 分销业务 agent 化链路</text>

  <rect x="10" y="50" width="150" height="110" rx="10" fill="#e3f2fd" stroke="#1976d2" stroke-width="1.5"/>
  <text x="85" y="76" font-size="13" font-weight="700" fill="#0d47a1" text-anchor="middle">分销团队</text>
  <text x="85" y="98" font-size="11" fill="#37474f" text-anchor="middle">人少事多</text>
  <text x="85" y="116" font-size="11" fill="#37474f" text-anchor="middle">客户易流失</text>
  <text x="85" y="134" font-size="11" fill="#37474f" text-anchor="middle">对账靠手工</text>

  <rect x="180" y="50" width="150" height="110" rx="10" fill="#e8f5e9" stroke="#388e3c" stroke-width="1.5"/>
  <text x="255" y="76" font-size="13" font-weight="700" fill="#1b5e20" text-anchor="middle">潮驿 Agent</text>
  <text x="255" y="98" font-size="11" fill="#37474f" text-anchor="middle">Skills 库</text>
  <text x="255" y="116" font-size="11" fill="#37474f" text-anchor="middle">改造方法论</text>
  <text x="255" y="134" font-size="11" fill="#37474f" text-anchor="middle">《30 天》手册</text>

  <rect x="350" y="40" width="150" height="130" rx="10" fill="#fff3e0" stroke="#f57c00" stroke-width="1.5"/>
  <text x="425" y="64" font-size="13" font-weight="700" fill="#e65100" text-anchor="middle">5× 数字业务社工</text>
  <text x="425" y="84" font-size="10.5" fill="#37474f" text-anchor="middle">distributor-onboarding</text>
  <text x="425" y="102" font-size="10.5" fill="#37474f" text-anchor="middle">reach-campaign</text>
  <text x="425" y="120" font-size="10.5" fill="#37474f" text-anchor="middle">channel-inspection</text>
  <text x="425" y="138" font-size="10.5" fill="#37474f" text-anchor="middle">order-inventory-reconcile</text>
  <text x="425" y="156" font-size="10.5" fill="#37474f" text-anchor="middle">visit-plan</text>

  <rect x="520" y="40" width="150" height="130" rx="10" fill="#f3e5f5" stroke="#7b1fa2" stroke-width="1.5"/>
  <text x="595" y="64" font-size="13" font-weight="700" fill="#4a148c" text-anchor="middle">宿主即跑</text>
  <text x="595" y="84" font-size="10.5" fill="#37474f" text-anchor="middle">Claude Code</text>
  <text x="595" y="102" font-size="10.5" fill="#37474f" text-anchor="middle">WorkBuddy</text>
  <text x="595" y="120" font-size="10.5" fill="#37474f" text-anchor="middle">Cursor</text>
  <text x="595" y="138" font-size="10.5" fill="#37474f" text-anchor="middle">Codex</text>

  <g fill="#90a4ae">
    <path d="M161 105 l14 0 l0 -4 l8 8 l-8 8 l0 -4 l-14 0 z"/>
    <path d="M331 105 l14 0 l0 -4 l8 8 l-8 8 l0 -4 l-14 0 z"/>
    <path d="M501 105 l14 0 l0 -4 l8 8 l-8 8 l0 -4 l-14 0 z"/>
  </g>

  <text x="10" y="208" font-size="11" fill="#607d8b">已落地：MCP 0.4 网关（mcp-server/，零依赖）把 Skills 统一暴露为工具，跨宿主按需注入上下文。</text>
</svg>

### 校验 Skills 格式

仓库内置格式校验，确保每一个 Skill 都符合 Skills 1.0 frontmatter 规范（缺字段会直接报错）：

```bash
python scripts/validate_skills.py
```

或重跑发布脚本：`bash scripts/publish_to_github.sh`。

## 路线图

- [x] **Skills 库首发**（5 个分销技能 + 模板）
- [x] **MCP 网关**：零依赖运行时，把 skills 暴露为统一 MCP 工具 → [mcp-server/](mcp-server/README.md)
- [x] **Agents 多角色模板**（入驻向导 / 触达管家 / 渠道巡检员 / 拜访统筹）→ [agents/](agents/README.md)
- [ ] 《30 天分销 agent 化》手册
- [x] 参考改造样例（首个被 agent 化的分销业务）→ [examples/reference-distribution](examples/reference-distribution/README.md)

## 冲星战役（发布后执行）

想要一周冲 1000 star？仓库发布后，按 [`launch/`](launch/README.md) 执行：
- [`launch/runbook.md`](launch/runbook.md) —— 每日作战手册（D-1 → D0~D6）
- [`launch/posts/`](launch/posts/) —— 10 篇各平台现成发帖文案（掘金/V2EX/知乎/Show HN/Reddit/Dev.to/X/公众号/小红书/Product Hunt）
- [`launch/demo-script.md`](launch/demo-script.md) —— 30 秒演示视频分镜
- [`launch/kpi-tracker.md`](launch/kpi-tracker.md) —— 每日 KPI 追踪表

## 贡献

见 [CONTRIBUTING](CONTRIBUTING.md)（含合规红线与新增 Skill 流程）与 `skills/_template/`。

## 许可证

[MIT](LICENSE) —— 可自由使用、二次开发、再分发。
