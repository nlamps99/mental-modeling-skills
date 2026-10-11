# Mental Modeling Skills (思维建模与认知脚手架技能集)

> **基于认知科学与毛选《实践论》的领域思维建模、学习进度追踪与 AI 对抗训练技能库。**  
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
- **进度必须可视化沉淀**：真正的学习需要持续的反馈与闭环，缺少可追踪的认知画布，探索很容易在半途迷失。

---

## 技能矩阵 (Skills Index)

| 目录编号 | 技能名称 | 核心定位与认知科学原理 | 适用场景 |
| :--- | :--- | :--- | :--- |
| **01** | [`01-ontology-extraction`](./skills/01-ontology-extraction/SKILL.md) | **本体抽取与概念降维**<br>· 认知负荷控制与图式理论<br>· 剥离黑话，抓取 3~5 个不可简化底层实体 | 面对陌生复杂领域感到信息混乱、无从下手时 |
| **02** | [`02-relational-topology`](./skills/02-relational-topology/SKILL.md) | **知识网络与四种关联建模**<br>· 奥苏贝尔层级锚定（找父节点）<br>· 根特纳结构映射同构（跨界借脑）<br>· 拮抗对偶（张力平衡）与动力因果回路 | 概念零散、记不住、需要建立高维直觉网络时 |
| **03** | [`03-falsification-probing`](./skills/03-falsification-probing/SKILL.md) | **反例证伪与红队压力测试**<br>· 约翰逊-莱尔德反例推理理论<br>· 皮亚杰认知顺应与边界标定 | 验证模型有效性、破除教条、寻找极端反例时 |
| **04** | [`04-procedural-sparring`](./skills/04-procedural-sparring/SKILL.md) | **程序性编译与两难交互沙盒**<br>· 安德森 ACT-R 产生式（IF-THEN）编译<br>· 认知学徒制两难情境实战对练 | 理论都懂但不会操作、需要高密度实战决断时 |
| **05** | [`05-domain-modeling-master`](./skills/05-domain-modeling-master/SKILL.md) | **领域思维建模全流程总控**<br>· 串联 01~04 阶段，引导端到端突破新领域 | 从零进入全新行业/学科，需要 AI 全程脚手架引导时 |
| **06** | [`06-progress-tracker`](./skills/06-progress-tracker/SKILL.md) | **认知进度追踪与画布审计**<br>· Dreyfus 成长模型与 ACT-R 状态审计<br>· 诊断认知卡点，规划针对性对练冲刺 | 定期复盘、追踪认知模型演化与实战进度时 |

---

## 从零吃透一个新领域的 14 天完整落地方案

配合本项目提供的 [《领域认知画布模板 (COGNITIVE_CANVAS.md)》](./templates/COGNITIVE_CANVAS.md)，建议按以下 5 个阶段推进：

```
[Day 1~2: 感性浸润] ──► [Day 3~4: 实体抽取] ──► [Day 5~7: 拓扑编织] ──► [Day 8~10: 红队打靶] ──► [Day 11~14+: 对抗对练与现实褪除]
  (找5个极端案例)       (抽3-5个硬实体)       (四维连线通电)        (寻找3个致命反例)        (沙盒两难抉择 & 记录预测误差)
```

1. **Phase 1: 感性浸润（Day 1~2）**：别急着要大纲。让 AI 讲 5 个行业最极端的争议与案例，在真实泥土里打滚。
2. **Phase 2: 实体提炼（Day 3~4）**：运行 `01-ontology-extraction`，在纸上画下最初 3~5 个零件。
3. **Phase 3: 拓扑编织（Day 5~7）**：运行 `02-relational-topology`，向上找父节点、横向跨界借脑、寻找制约死对头、跑通因果闭环。
4. **Phase 4: 红队打靶（Day 8~10）**：运行 `03-falsification-probing`，让 AI 抛出极端反例，标定失效禁区。
5. **Phase 5: 对抗编译与现实褪除（Day 11~14+）**：运行 `04-procedural-sparring` 跑通 3 个灰度实战情境；随后拆除 AI 脚手架，在现实工作中用认知画布记录“预测误差”。

---

## 快速使用指引

### 方式一：配合认知画布在本地维护
1. 复制 [`templates/COGNITIVE_CANVAS.md`](./templates/COGNITIVE_CANVAS.md) 到你的工作目录，重命名为你的目标领域（如 `RUST_ASYNC_CANVAS.md`）。
2. 调用对应技能的 Prompt 模板与 AI 对话，将提炼出的实体、拓扑、反例和产生式持续沉淀在画布中。
3. 每隔几天，调用 `06-progress-tracker` 让 AI 审计当前画布的成熟度与盲区。

### 方式二：在 Cursor / Windsurf 中使用
将本仓库的 `skills/` 目录复制到项目的 `.cursor/skills/` 或 `.cursor/rules/` 中，并在提问时直接召唤：
- `@01-ontology-extraction 帮我抽取该领域的底层硬实体`
- `@02-relational-topology 帮我建立知识网络与对偶张力`
- `@03-falsification-probing 对我的模型寻找极端反例`
- `@04-procedural-sparring 开启两难实战考官对练`
- `@06-progress-tracker 审计我当前的认知画布并指出盲区`

### 方式三：在 Codex / Antigravity / Claude Code 中使用
本仓库遵循标准 Agent Skill 规范（包含 YAML frontmatter 与 Markdown 工作流），可直接由智能体通过 `view_file` 或 `use_skill` 动态激活。

---

## 开源协议

本项目采用 [MIT License](./LICENSE) 开源协议。欢迎 Star、Fork 与提交 PR 分享你在各个领域的实战认知画布！
