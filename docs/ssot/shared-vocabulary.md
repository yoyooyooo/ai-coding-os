# Shared Vocabulary

本表冻结跨 Skill 使用的精确英文拼写和一句话含义。详细因果与边界仍由对应 Owner 持有；本文件不是中央业务词典或机器 Registry。

| Canonical term / phrase | 压缩含义 | Owner |
| --- | --- | --- |
| `Accepted Meaning` | 有权角色当前接受的产品或工程含义 | `$product-definition` / applicable authority |
| `Source Reality` | 当前源码、Schema、配置和依赖表达的实现现实 | source / architecture |
| `Observed Reality` | 一次真实执行在特定条件下产生的观察 | `$product-harness-system` |
| `Quality Boundary` | 产品必须达到的底线、可接受粗糙度与剩余风险 Authority | `$product-definition` |
| `Claim Ceiling` | 当前 Evidence 最多允许声称到哪里 | `$product-harness-system` |
| `Current Home` | 某 scoped current meaning 的唯一权威知识位置 | `$docs-governance` |
| `Freshness` | 一项知识依赖什么，以及什么会让它失效 | `$docs-governance` |
| `Earned Shape` | 由真实压力证明有必要的结构或持久化形态 | owning Skill / `$ai-coding-os-evolution` |
| `Portable Default` | 项目沉默时使用、可被 coherent override 覆盖的稳定默认 | owning Skill |
| `ETC / Easier to Change` | 用真实变化是否更局部、可理解、可验证和可恢复来审视设计，不是单一评分器 | `$evolvable-application-architecture` |
| `DRY` | 同一知识、规则或意图有一个明确 Authority，不等于消灭所有字面重复 | owning semantic Owner / `$docs-governance` |
| `Orthogonality` | 独立变化轴不应被迫一起移动 | `$evolvable-application-architecture` |
| `Reversibility` | 让当前选择可被找到、隔离、替换、迁移和恢复，而不是预测全部未来 | `$evolvable-application-architecture` |
| `Agent-Legible Change Surface` | 新上下文安全改变一个能力所需的最小完整关系面 | `$evolvable-application-architecture` |
| `Final Materialization Authority` | 一致性范围内接受并最终写入某事实的 Authority | `$evolvable-application-architecture` |
| `Candidate` | 尚未被 governed use case 接受的提案、观察或外部结果 | `$evolvable-application-architecture` |
| `Port` | 应用拥有的能力契约，而不是 Provider 形状的别名 | `$evolvable-application-architecture` |
| `Composition Root` | 选择 live implementation、构造资源并拥有关闭路径的 Host 入口 | `$evolvable-application-architecture` |
| `Intent` | 用户希望发生的动作，不是已经发生的事实 | `$frontend-architecture` |
| `Projection` | Accepted Fact 的远端或本地可读视图，不是最终 Writer | `$frontend-architecture` |
| `State Role` | intent、proposal、projection、interaction、navigation、continuity 等不同状态职责 | `$frontend-architecture` |
| `Unknown Outcome` | 外部效果可能已发生，但本地未获得确定结果 | `$effect-best-practices` / EAA |
| `Scope` | 能解释资源或 child work 为什么存在以及何时结束的生命周期 Owner | `$effect-best-practices` |
| `Dependency Reality` | fixture、fake、replay、local-real、external-real 的真实性层次 | `$product-harness-system` |
| `First Wrong State` | 因果链中最早偏离契约或不变量的状态 | `$product-harness-system` / EAA |
| `Feedback Horizon` | 从行动到可信反馈、停止与恢复的安全照距 | `$product-harness-system` |
| `Prototype` | 为回答少数问题而构建、预期丢弃的学习实验 | `$product-definition` |
| `Tracer` | 薄但真实、可保留并继续生长的端到端路径 | `$product-definition` / EAA |
