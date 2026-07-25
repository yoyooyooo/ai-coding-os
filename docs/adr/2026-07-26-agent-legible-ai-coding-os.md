# ADR: Agent-legible AI Coding OS

- Status: accepted
- Date: 2026-07-26
- Scope: Suite product and knowledge-network doctrine

## Context

更强 Agent 的瓶颈逐渐从局部编码能力转向项目对齐、Authority、Unknown、上下文发现和验证。与此同时，为旧模型积累的长规则、重复示例和固定 Workflow 可能开始限制新模型判断能力。

## Decision

将 AI Coding OS 定位为**面向 Agent 的项目认知、决策与验证基础设施**，遵守：

```text
Agent-legible project, not Agent-scripted workflow
Strong invariants, weak choreography
Minimal context, maximal legibility
No silent material assumption
Commitment-aware autonomy
Evidence over confidence
Earned persistence
Preserve semantics; re-earn scaffolding
```

目标不是清除所有 Unknown，而是不存在未识别、未归属、未约束却足以改变结果的 Unknown。普通可逆技术判断留给 Agent；高承诺边界前闭合相应决定。

## Alternatives

- 继续增加完整规则和固定流程：拒绝，会将高能力 Agent 降级为脚本执行器。
- 完全依赖模型判断而移除 Authority 和 Evidence：拒绝，模型智力不能决定人类未对齐的语义。
- 建立中央 Unknown Registry：拒绝，Unknown 继续由各语义 Owner 处理。

## Consequences

- 主 Skill 变薄，References、Tools 和 Evidence 按需加载。
- Instruction 也必须通过不变量或 Protected Failure Earn。
- Decision Closure 分阶段，不以所有前置问题都解决为开工条件。
- Context cost、错误升级和 Claim Overreach 成为 Suite 健康指标。

## Evidence And Claim Ceiling

本 ADR 定义产品与设计方向，不证明任意模型在真实项目中的自主性提升。该效果需要 `$skill-evaluation-system` 的 Model-run Evidence。

## Revisit Conditions

当模型/Agent 能力、Context 机制、Tool/Harness 或实际失败分布发生显著变化时，由 `$ai-coding-os-evolution` 重新评估脚手架，而不是自动改写语义不变量。
