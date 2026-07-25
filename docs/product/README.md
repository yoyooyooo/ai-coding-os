# Product

## Owns

- AI Coding OS 的产品定位、目标用户和长期价值。
- “项目对 Agent 可读”这一核心结果，而不是固定执行 Workflow。
- Skills、Docs、Architecture Decision IR、Harness、Skill evaluation 与 Suite evolution 的产品关系。

## Must Not Own

- 某个项目的产品语义、事实 Writer、技术栈或执行状态。
- 单个 Skill 的实现规则、Schema 字段或 Benchmark 分数。

## Current Positioning

AI Coding OS 是面向 AI Coding Agent 的**项目认知、决策与验证基础设施**。它通过严密但可渐进披露的知识网络，让项目本身能够告诉 Agent：

```text
什么是当前有效事实
谁拥有当前问题的语义与决定权
哪些只是源码观察、候选或未证明主张
哪里可以自主判断和可逆推进
哪里需要先探测、获得外部决定或停止
怎样证明结果，以及哪些相邻结论仍不能声称
```

它追求的是：

> **Agent-legible project, not Agent-scripted workflow。**

不是替 Agent 规划每一步，而是提供足够清楚的世界、强不变量、决策边界和验证接口，使更强模型能够在更大的自主空间内正确推进。

## User Value

```text
可知  正确 Authority、Source、Evidence 和失效条件可发现
可判  普通技术选择、可接受假设、外部决定和 Stop Line 可区分
可做  在剩余不确定性被约束后，Agent 可自主规划和实施
可证  Claim 由匹配的 Proof Surface 和 Evidence 支持
可演进  项目知识与 Skill Suite 都能在变化后重新收敛
```

## Unknown And Alignment

目标不是虚假的 Unknown-Free，而是消除**静默的关键假设**：任何足以改变产品语义、权限、持久数据、公共契约、事实 Authority、迁移或不可逆外部行为的未知，都必须被识别、归属并获得处理方式。

更危险的是 False Known：旧文档、已有源码、通过的局部测试或未经验证的目标设计，被错误地当作当前事实。Suite 因此持续区分 Authority、knowledge basis、temporal plane 和 evidence state。

## Product Principles

```text
Project Authority First
Strong invariants, weak choreography
Minimal context, maximal legibility
No silent material assumption
Commitment-aware autonomy
Evidence over confidence
Earned persistence
Preserve semantics; re-earn scaffolding
```

## Non-goals

AI Coding OS 不拥有：

- 统一 Ticket、Tracker、发布或多 Agent Workflow；
- 所有项目必须填写的中央架构数据库；
- 全局 Unknown Registry；
- 自动替人决定产品、安全、法律或不可逆业务语义；
- 未经留出集 Gate、Checkpoint 和发布 Authority 的自我改写。

## Routes

- [当前事实](../ssot/README.md)
- [Suite 架构](../architecture/README.md)
- [核心 Doctrine 与发布标准](../standards/README.md)
- [关键决策](../adr/README.md)
