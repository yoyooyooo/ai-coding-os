# Agent Legibility and Decision Control Plane

> Derived architecture view. It visualizes relationships already owned by [Suite Topology](suite-topology.md), [Architecture Decision System](architecture-decision-system.md), and [Skill Evaluation And Evolution](skill-evaluation-and-evolution.md); it is not a separate Current Authority.

## 总体结构

```text
Product / SSoT / Standards / ADR / Contracts
                    │ normative map
                    ▼
        Federated Semantic Owners
                    │
        ┌───────────┴────────────┐
        ▼                        ▼
Local Architecture         Project/Source Grounding
Decision IR                schema / code / runtime
        │                        │
        └───────────┬────────────┘
                    ▼
       Agent planning and implementation
                    │
                    ▼
       Harness / Test / Runtime Evidence
                    │
                    ▼
Conflict / Gap / Drift / Assumption / Probe
                    │
          update owning Current Home
```

AI Coding OS 是认知与决策控制面，不是执行 Loop 控制器。Agent 自己选择策略、工具、并行度与局部 Harness；Suite 提供正确的语义 Owner、局部上下文、决策权、Commitment Boundary 与 Proof obligation。

## Federated Ownership

```text
$product-definition                  产品含义和产品 Unknown
$evolvable-application-architecture  Fact Authority、Use Case、Port、Evolution
$frontend-architecture               State / Intent / Projection / Reconciliation
$effect-best-practices               Service / Layer / Runtime / Scope
$architecture-decision-system        跨 Owner 的局部决策图与对账
$docs-governance                     文档 Current Home、Route、freshness、cleanup
Harness Skills                       经验 Probe、Observation 与 Claim Ceiling
$skill-evaluation-system             Skill 行为实验和 held-out Evidence
$ai-coding-os-evolution              Suite Capability Epoch 与发布治理
```

Unknown 不集中收口。`$architecture-decision-system` 只处理架构问题如何表达、组合、对账和闭合；产品 Unknown、运行 Unknown 与安全/法律决定仍留在其 Authority。

## Project Autonomy

安全自主推进不要求整个项目 Unknown-Free。对当前 Slice，Agent 需要判断：

```text
settled meanings and constraints
material residual unknowns
agent decision rights
allowed bounded assumptions
commitment and stop lines
smallest useful probes
proof obligations and claim ceiling
```

这些内容可以即时形成，不要求每次落盘或展示固定模板。长任务、跨 Agent、跨语言、迁移和不可逆行为才可能 Earn 一个 Autonomy Envelope。

## Suite Self-evolution

```text
Capability change
  -> capability hypotheses
  -> fresh-context reviews
  -> failure attribution
  -> Current / Candidate / Minimal / No-Suite rollout
  -> hierarchical gates
  -> staged release and rollback
```

语义宪法慢变；能力脚手架中速变；Eval 与 Tooling 快速变。任何候选都不能仅凭作者或目标模型的自我评价获得 Current Authority。
