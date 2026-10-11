# Mental Modeling Skills (思维建模与认知脚手架技能集)

> **基于认知科学与毛选《实践论》的领域思维建模与 AI 对抗训练技能库。**  
> 专为 Cursor / Codex / Claude Code / Antigravity 等 AI Agent 设计。帮助你告别“看了 AI 总结以为懂了，一上手全忘”的假象，建立真正属于自己的高维认知网络与实战直觉。

---

## 为什么需要这套 Skills？

在 AI 时代，我们学一个新领域的典型困境是：
1. **直接要框架**：让 AI 列入门全景图，AI 5 秒钟给出完美清单。
2. **以为掌握了**：看着逻辑整齐的词条，产生“我已经懂了”的流畅性错觉。
3. **遇到现实一片空白**：几天后真要做判断时，脑子依然一片茫然。

认知心理学对此有着极深刻的机理解释：
- **AI 给予的只是“陈述性知识（Declarative Knowledge）”**，而解决复杂问题靠的是**心理模型（Mental Models - Johnson-Laird）**与**程序性直觉（Procedural Knowledge - ACT-R）**。
- **孤立的名词没有力量**：大脑记忆是高维语义网络（Collins & Loftus 激活扩散理论），决定顿悟和反应速度的是概念之间连接线的导电性与格栅结构（Latticework）。
- **真正的认识无法外包**：AI 是最强大的脚手架（Scaffolding），但脚手架存在的唯一目的是被拆除（Fading）。

---

## 技能矩阵 (Skills Index)

| 目录编号 | 技能名称 | 核心定位与认知科学原理 | 适用场景 |
| :--- | :--- | :--- | :--- |
| **01** | [`01-ontology-extraction`](./skills/01-ontology-extraction/SKILL.md) | **本体抽取与概念降维**<br>· 认知负荷控制与图式理论<br>· 剥离黑话，抓取 3~5 个不可简化底层实体 | 面对陌生复杂领域感到信息混乱、无从下手时 |
| **02** | [`02-relational-topology`](./skills/02-relational-topology/SKILL.md) | **知识网络与四种关联建模**<br>· 奥苏贝尔层级锚定（找父节点）<br>· 根特纳结构映射同构（跨界借脑）<br>· 拮抗对偶（张力平衡）与动力因果回路 | 概念零散、记不住、需要建立高维直觉网络时 |
| **03** | [`03-falsification-probing`](./skills/03-falsification-probing/SKILL.md) | **反例证伪与红队压力测试**<br>· 约翰逊-莱尔德反例推理理论<br>· 皮亚杰认知顺应与边界标定 | 验证模型有效性、破除教条、寻找极端反例时 |
| **04** | [`04-procedural-sparring`](./skills/04-procedural-sparring/SKILL.md) | **程序性编译与两难交互沙盒**<br>· 安德森 ACT-R 产生式（IF-THEN）编译<br>· 认知学徒制两难情境实战对练 | 理论都懂但不会操作、需要高密度实战决断时 |
| **05** | [`05-domain-modeling-master`](./skills/05-domain-modeling-master/SKILL.md) | **领域思维建模全流程总控**<br>· 串联 01~04 阶段，引导端到端突破新领域 | 从零进入全新行业/学科，需要 AI 全程脚手架引导时 |

---

## 快速使用指引

### 方式一：直接作为 AI 对话 Prompt 使用
直接复制对应技能目录中 `SKILL.md` 的【核心 Prompt 模板】，将【目标领域】替换为您当前正在研究的学科或行业，直接输入给 ChatGPT / Claude / DeepSeek / Gemini 等任何大模型。

### 方式二：在 Cursor / Windsurf 中作为 Rules 使用
将本仓库的 `skills/` 目录复制到项目的 `.cursor/skills/` 或 `.cursor/rules/` 中，并在提问时直接召唤：
- `@01-ontology-extraction 帮我抽取 Rust 异步运行时的核心本体`
- `@02-relational-topology 帮我建立交易流动性与订单簿的因果网络`
- `@03-falsification-probing 对我总结的这个认知模型找反例`
- `@04-procedural-sparring 考考我分布式事务的两难决策`

### 方式三：在 Codex / Antigravity / Claude Code 中使用
本仓库遵循标准 Agent Skill 规范（包含 YAML frontmatter 与 Markdown 工作流），可直接由智能体通过 `view_file` 或 `use_skill` 动态激活。

---

## 经典实操走查（以“认知心理学”为例）

本技能库的底层方法已在以下实战案例中完成完整验证：

1. **本体抽取**：提炼出 **注意（Attention）**、**工作记忆（Working Memory）**、**图式（Schema）**、**产生式（Production Rules）** 4 个硬实体。
2. **四种连线**：
   - **层级锚定**：向上锚定到控制论与信息论（有限带宽下的信息调度与负反馈）。
   - **结构映射**：1:1 映射到计算机操作系统（注意力=CPU时间片调度，工作记忆=内存RAM，图式=硬盘数据库，焦虑死机=内存泄漏）。
   - **拮抗对偶**：自下而上感知（数据驱动） vs 自上而下预期（概念驱动）。
   - **因果回路**：消极图式 $\to$ 注意力窄化 $\to$ 收集负面证据 $\to$ 加固图式的恶性正反馈。
3. **程序性对练**：在面对公开批评的灰度情境中，调动多模型决断并纠偏。

---

## 认知哲学基石

> “理性认识是一棵树，它必须扎根在感性认识的土壤里才能活。” —— 毛泽东《实践论》  
> “你的知识如果只是孤立的散点，你根本无法使用它们；你必须把经验悬挂在由多个模型组成的格栅网络上。” —— 查理·芒格  
> “认识是一切改变的开始。而真实的认识，是无法外包的。”

---

## 开源协议

本项目采用 [MIT License](./LICENSE) 开源协议。欢迎 Star、Fork 与贡献更多领域的建模案例！
