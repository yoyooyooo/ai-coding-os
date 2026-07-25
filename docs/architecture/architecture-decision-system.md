# Architecture Decision System

## Purpose

`$architecture-decision-system` 是跨架构 Owner 的横向决策基础设施。它不替 EAA、Frontend、Effect、Product 或 Docs Governance 重新定义语义，而是把当前问题所需的 Claim、Source、Evidence、Unknown、Decision 和失效条件组织为最小可推理工作集。

## ADIR

Architecture Decision IR（ADIR）冻结为：

> 一个局部、部分可表达、来源可追溯、Evidence 有边界的 decision-bearing graph。

它不是完整项目 DSL，也不是强制 YAML。默认只存在于 Agent 当前上下文中。

```text
persistent Authorities / Source / Evidence
                │  按当前问题检索
                ▼
        Local Architecture ADIR
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
      decision  implementation  proof obligations
                │
                ▼
       only earned results persist
```

## Planes

| Plane | Questions |
| --- | --- |
| Normative | 应该是什么，哪个决定/Standard 当前绑定 |
| Observed | 源码、Schema、运行和部署实际是什么 |
| Epistemic | accepted、observed、source-derived、inferred、assumed、unknown、not-proven |
| Decision | Conflict、Ambiguity、Gap、Assumption、Hypothesis、Drift、Risk |
| Evidence | 哪个 Proof Surface 支持哪个 Claim，哪些不决定或仍未证明 |

这些轴不能压成单一 `status`。

## Decision Calculus

底层是 owner-scoped rule forest。规则接口逐步统一为：

```text
applies_when
asks
requires
forbids
agent_may_decide_when
assumption_allowed_when
escalate_when
probes
proof_focus
```

用户看到的 Decision Tree 只是针对当前问题即时生成的局部视图。

## Material Unknown And False Known

问题只有在足以改变产品语义、权限、事实 Authority、公共契约、持久数据、迁移、不可逆外部行为或证明结论时，才成为 material issue。

先做 Scope normalization，再区分：

```text
Conflict / Ambiguity / Gap / Assumption / Hypothesis
Drift / Violation / Evidence Gap / Risk / External Dependency
Migration Debt / Over-abstraction
```

False Known 通过 Map–Territory reconciliation 转化为 stale claim、wrong authority、current/target confusion、drift 或 evidence gap。

## Commitment-aware Autonomy

```text
Exploration Readiness
Reversible Implementation Readiness
Commitment Closure
Claim Closure
```

复杂 Slice 可以派生 Autonomy Envelope：settled facts、residual material unknowns、decision rights、allowed assumptions、stop lines、proof obligations 和 safe-to-proceed boundary。普通任务不生成该模板。

## Architecture Health

Health 是以下输入的点时派生结果：

```text
accepted architecture
+ observed source/runtime
+ applicable rules
+ evidence
+ residual unknowns and assumption age
```

至少按 Authority Integrity、Decision Closure、Map–Territory Alignment、Assumption Hygiene、Evidence Adequacy、Evolution Integrity、Agent Legibility 和 Knowledge Freshness 分维度报告。`unknown != unhealthy`，`not_proven != failed`，不得默认汇总成一个分数。

## Earned IR

```text
L0 Implicit Slice IR
L1 Decision Trace
L2 Durable Architecture Slice
L3 Project Architecture Model
L4 Machine-validated IR
```

持久化位置继续由 `$docs-governance` 决定：Current architecture 进入 `docs/architecture`，决策原因进入 ADR，强规则进入 Standards，点时 Health 进入 Reports，迁移顺序进入 Roadmap。
