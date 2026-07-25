# Core Doctrine

这些原则是 AI Coding OS 当前的慢变语义宪法。它们可以被新 Evidence 和正式 ADR 挑战，但不能因为一个模型在某个 Benchmark 上分数更高就自动删除。

## Project Authority First

项目已接受的 Product、SSoT、Standard、ADR、Contract 与真实 Evidence，优先于未采用的通用 Skill、Preset 或模型猜测。`AGENTS.md` 约束 Agent 行动，但不会自动拥有产品含义、协议或运行事实。

## Question-scoped Ownership

不存在一份文件对所有问题都最高。Product meaning、Fact authority、Documentation authority、Source observation、Runtime evidence、Execution status 与 Release decision 按 claim 类型拥有各自 Authority。

## One Scoped Meaning, One Current Home

同一 claim、representation、scope 和 temporal plane 只保留一个 canonical Current Home。Router、索引、ADIR 和报告链接到它，不复制第二份当前真相。

## Source Is Not Decision

源码证明当前实现结构和静态属性；它可能是 accepted implementation、implementation gap、unaccepted implementation 或 stale source。源码存在不等于产品和架构已经决定如此。

## No Silent Material Assumption

足以改变 Product meaning、Authority、durable data、public compatibility、permissions、migration 或 irreversible behavior 的 Unknown，不能被静默变成实现假设。Incidental、低风险、可逆细节由 Agent 自主判断。

## Evidence Bounds Claims

```text
observed != inferred != accepted
not_proven != failed
fake proof != real-adapter proof
static proof != runtime proof
command success != product completion
```

Claim 必须受实际 Proof Surface、dependency reality、observation 和 claim ceiling 约束。

## Route Is an Edge, Not a Sequence

Router 和 docs index 提供发现边，不规定统一阅读、规划、Ticket 或实施顺序。只有真实状态机、事务、安全协议、迁移和外部协议可以拥有必要的顺序。

## Strong Invariants, Weak Choreography

Skill 应明确稳定语义边界、决策权、Stop Line 与 Proof limit，同时把普通可逆策略留给高能力 Agent。不要用固定 Workflow 替代判断。

## Minimal Context, Maximal Legibility

核心入口保持轻量；高保真 Reference、Source、Schema、Test 与 Harness 按当前问题 Progressive Disclosure。更多文本不等于更可理解。

## Commitment-aware Autonomy

```text
Exploration Readiness
Reversible Implementation Readiness
Commitment Closure
Claim Closure
```

Agent 可以带着有界 Unknown 探索或进行可回滚实现；在跨越 durable/public/permission/destructive/irreversible Commitment 前，相关决定必须闭合；在声称完成前，Evidence 必须闭合。

## Earned Persistence

ADIR、Autonomy Envelope、registry、schema、partition、Compatibility Overlay、固定 Harness 与长期记录都只在跨 Agent、长期迁移、审计、机器消费或重复压力下持久化。

## Preserve Semantics; Re-earn Scaffolding

模型、工具和 Harness 能力变化后，稳定语义继续保留；固定输出模板、详细步骤、重复提醒、静态决策树和兼容脚手架需要通过 Ablation 和 held-out Eval 重新证明价值。
