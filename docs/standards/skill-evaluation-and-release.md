# Skill Evaluation And Release Standard

## Owns

- Skill/Suite 候选的行为评估、数据完整性、分层 Gate、Checkpoint、发布和回滚规则。

## Must Not Own

- Product、Architecture 或 Docs 语义本身；Evaluator 分数不能偷换这些 Authority。

## Evaluation Subject

每次运行冻结：

```text
current Suite/source SHA
candidate lineage
Agent Capability Profile
Eval corpus manifest and case-family split
Harness / Oracle / permissions / budgets
protected failures and release authority
```

## Failure Attribution Before Edit

失败不自动等于 Skill defect。必须区分 execution、routing、retrieval、Tool、project knowledge、semantic owner、Evaluator、model capability 和 noise。错误 Oracle 必须修 Evaluator，不能训练 Skill 去迎合。

## Data Integrity

- Discovery/Train 可供 optimizer 反思；Selection 只做候选 Gate；Sealed Test 不参与选择；Transfer/Canary 证明泛化。
- 同源 case family 不跨 Split。
- 记录谁看过任务、reference、答案和反馈。
- 发现污染后该 Split 的 Claim 失效，必须轮换或降级。

## Bounded Update

变更预算按语义半径，而不是 Markdown edit 数量：

```text
E0 prose / duplicate / local route
E1 one-Skill executive strategy
E2 router / description / cross-Skill handoff
E3 shared contract / owner map / doctrine
E4 semantic constitution / compatibility / release contract
```

E2 以上需要对应 Composition、Owner 和 Release review。

## Hierarchical Gate

Evaluation Integrity、Mechanical Integrity、Constitutional Invariants 和 Critical Protected Regression 是 veto。Behavioral Utility、Context Cost 与 Transfer 只能在前述 Gate 通过后比较。

默认对照：Current、Candidate、Minimal Kernel、No Suite。必要时增加 Previous Capability Profile 或 Compatibility Overlay。最后一个候选不等于最佳 Checkpoint。

## Adoption

Candidate 先 Stage，保留 source/eval hashes、accepted/rejected changes、not_evaluated、rollback anchor 和 Claim Ceiling。没有干净 held-out Gate、Checkpoint、Rollback 和 Release Authority，不允许自动采纳。

## Current Claim Ceiling

`suite_audit.py` 只提供离线机械 Evidence。独立模型行为结果必须作为版本化 sidecar 明确记录 `model`, `harness`, `corpus`, `seed/run`, `observed`, `supports`, `does_not_decide`, `not_proven`。
