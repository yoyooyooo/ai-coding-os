# Plan Optimality Ledger: Goal Proof DAG Frontier Plan

## Meta

```yaml
target: docs/goal-proof/sources/2026-05-31-goal-proof-dag-frontier-view-proposal.md
targets:
  - docs/goal-proof/sources/2026-05-31-goal-proof-dag-frontier-view-proposal.md
  - docs/goal-proof/README.md
source_kind: file-plan
reviewers:
  - A1-structure-purity
  - A2-token-economy
  - A3-dominance-alternatives
  - A4-objective-function
round_count: 2
challenge_scope: open
consensus_status: achieved
```

## Bootstrap

```yaml
target_complete: true
alignment_gate:
  policy: auto
  status: inferred
  resolved_points:
    - 用户明确要求使用 `$plan-optimality-loop` 打磨当前未提交提案文档。
    - 用户明确允许多 reviewer / subagents 挑战并收敛方案。
    - 用户要求主 agent 吸收原问题，从上层主导分析，最终把提案转成可实施方案。
    - 本轮不开始实现 CLI，只修改提案本体和 review ledger。
  open_questions: []
  confirmation_basis: >
    用户给出目标工件、skill、challenge 意图、write policy 和 stop condition：
    持续打磨直到多方对齐。
review_contract:
  artifact_kind: implementation-plan
  review_goal: implementation-ready
  target_claim: >
    将未提交提案收敛成可实施方案：定义只读 goal-proof DAG ready frontier view，
    保持 relations.links 作为 verified relation evidence，不把 pending dependency 塞进
    relations check，并明确 structured blockers 的 schema/CLI/docs/test 更新路径。
  target_refs:
    - docs/goal-proof/sources/2026-05-31-goal-proof-dag-frontier-view-proposal.md
    - docs/goal-proof/README.md
    - packages/cli/src/goal-proof.ts
    - packages/cli/src/render-goal-relations.ts
    - packages/cli/src/lib/goal-pack.ts
    - packages/cli/test/goal-relations-cli.test.ts
    - packages/cli/test/check-goal-pack.test.ts
    - skills/goal/goal-proof-system/references/cli.md
    - skills/goal/goal-proof-system/references/goal-relations.md
    - skills/goal/goal-proof-system/references/checker-rules.md
    - skills/goal/goal-proof-system/templates/progress.yaml
  non_default_overrides:
    alignment_policy: auto
    scope_fence: >
      可以挑战 command surface、schema 分层、实施顺序、验收门和目标函数；
      不开始实现代码；不引入第二套 workflow、第二类 ledger、scheduler 或 stored graph。
    stop_condition: consensus
    write_policy: >
      reviewer 不改文件；主 agent 可改目标提案、docs/goal-proof/README.md 和本 ledger。
review_object_manifest:
  source_inputs:
    - docs/goal-proof/sources/2026-05-31-goal-proof-dag-frontier-view-proposal.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/workflow.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/ledger-schema.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/reviewer-prompts.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/reviewer-views.md
  materialized_targets:
    - docs/goal-proof/sources/2026-05-31-goal-proof-dag-frontier-view-proposal.md
    - docs/review-plan/runs/2026-05-31-goal-proof-dag-frontier-plan-review.md
  authority_target: docs/goal-proof/sources/2026-05-31-goal-proof-dag-frontier-view-proposal.md
  bound_docs:
    - docs/goal-proof/README.md
    - docs/review-plan/runs/2026-05-31-goal-proof-dag-frontier-plan-review.md
  derived_scope:
    artifact_kind: implementation-plan
    review_goal: implementation-ready
  allowed_classes:
    - CLI public surface
    - structured blocker schema
    - relation evidence boundary
    - DAG/frontier JSON contract
    - implementation waves
    - verification backlog
    - rollback and non-goals
  blocker_classes:
    - unresolved schema ownership
    - relations/blocker semantic mixing
    - stored graph or second edge authority
    - scheduler/queue/worklist semantics
    - future evidence id in pending blockers
    - unsealed verification gate
  ledger_target: docs/review-plan/runs/2026-05-31-goal-proof-dag-frontier-plan-review.md
challenge_scope: open
reviewer_set:
  - A1
  - A2
  - A3
  - A4
active_advisors:
  - A4
activation_reason: >
  open scope 且目标涉及 CLI public surface、schema boundary、Goal Relations 和长期治理，
  按默认启用 A4。
max_reviewer_count: 4
kernel_council:
  - Ramanujan
  - Kolmogorov
  - Godel
dominance_axes:
  - concept-count
  - public-surface
  - compat-budget
  - migration-cost
  - proof-strength
  - future-headroom
stop_rule: >
  全部 reviewer 对最新 proposal 和 freeze record 返回无 unresolved findings；
  目标 proposal 已保存；本 ledger 写入 adopted candidate、rejected alternatives、
  residual risk 和 consensus 状态。
reopen_bar: >
  只有能证明 adopted candidate 仍会引入第二 edge authority、scheduler 语义、
  schema/apply 破坏风险，或能在 dominance axes 上严格支配，才允许 reopen。
ledger_path: docs/review-plan/runs/2026-05-31-goal-proof-dag-frontier-plan-review.md
writable: true
```

## Round 1

phase: challenge

### Findings

| id | severity | class | summary | status |
| --- | --- | --- | --- | --- |
| F-001 | blocker | invalidity | structured blockers 被写成后续增强，但 pending blocking edges 又依赖它。 | adopted |
| F-002 | blocker | invalidity | `relations.dag.predecessor_goal_ids` / `successor_goal_ids` 会形成第二套 graph authority。 | adopted |
| F-003 | high | ambiguity | JSON 里的 `nodes[].status` 混淆 stored status 和 derived frontier state。 | adopted |
| F-004 | high | ambiguity | `ok/errors/warnings` policy 未定义，missing predecessor、cycle、raw blocker 等无法实施。 | adopted |
| F-005 | high | invalidity | pending blocker 预写未来 `E999`，制造假稳定 evidence id。 | adopted |
| F-006 | high | invalidity | `unblocks.status/next_action` 把状态迁移塞进 blocker，重复 evidence/apply 状态机。 | adopted |
| F-007 | medium | ambiguity | bound surface 未完整列出 `index.ts`、package README、help/docs tests。 | adopted |
| F-008 | medium | controversy | `--include verified,blocking,hint` 污染既有 read-output `--include fields` 语义。 | adopted |
| F-009 | medium | ambiguity | `related_to` / `supersedes` 是否进入 readiness edge 未封口。 | adopted |

### Counter Proposals

| id | summary | why_better | dominance | status |
| --- | --- | --- | --- | --- |
| CP-001 | Schema-first frontier：先冻结 blocker union，再实现只读 DAG frontier。 | pending edge 有 authority，CLI 不从展示倒推语义。 | proof-strength / future-headroom dominate | adopted |
| CP-002 | 删除 stored edge hints，只允许 `relations.links` 和 structured blockers 产生 edge。 | 一个 edge fact 一个 owner。 | concept-count / Godel gate dominate | adopted |
| CP-003 | 保留 top-level `goal-proof dag`，但 contract 写成 frontier-first。 | 满足自然语言入口，同时不污染 `relations` evidence surface。 | public-surface neutral, proof-strength improves | adopted |
| CP-004 | pending blocker 用 predicate，不写 future `E999`，不写 `unblocks`。 | 不伪造 ledger id，不创建第二状态机。 | compat-budget / proof-strength dominate | adopted |
| CP-005 | JSON 使用 `goal_status` / `progress_status` / `frontier_state`。 | 保留事实与派生判断边界。 | proof-strength dominate | adopted |
| CP-006 | MVP 不新增 edge-kind flags，后续如需要用 `--edge-kind`。 | 不复用 `--include` 的既有字段恢复语义。 | public-surface / compat-budget dominate | adopted |

### Resolution Delta

- 目标文件改为 adopted implementation plan。
- 保留 `goal-proof dag`，但定义为 read-only thread frontier projection。
- structured blockers 升格为 W1，而不是后续可选增强。
- 删除 `relations.dag.predecessor_goal_ids` / `successor_goal_ids`。
- 删除 blocker `unblocks`。
- pending goal blocker 改为 `goal_completion + predicate.completion_satisfied`，不预写 `E999`。
- 新增 edge admission、frontier classification、JSON contract、error/warning policy。
- 实施顺序改为 W1 blocker union schema -> W2 DAG command -> W3 docs/skill sync。

## Adoption

adopted_candidate: schema-first-read-only-dag-frontier

lineage:

- A1 `ALT-A1-01`
- A1 `ALT-A1-02`
- A2 `ALT-2`
- A2 `ALT-3`
- A3 `A3-ALT-1`
- A4 `ALT-1`
- A4 `ALT-3`

rejected_alternatives:

- `relations graph as frontier`: rejected because it overloads relation metadata graph with pending readiness.
- `relations frontier`: rejected because it moves readiness into the relations namespace and weakens the evidence boundary.
- `stored relations.dag edge hints`: rejected because it creates shadow graph authority.
- `MVP with pending edges but no blocker schema`: rejected because implementation would depend on free text or unstable parser behavior.
- `opaque-only blocker MVP`: deferred because it is smaller but does not satisfy the target claim for machine-readable pending edges.
- `future E999 in blockers`: rejected because pending waits must not claim future ledger ids.
- `unblocks in blockers`: rejected because state transitions are owned by evidence/apply.

### Freeze Record

adopted_summary: >
  Implement `goal-proof dag` as a read-only, frontier-first projection over one
  Goal Thread. First freeze a compatible `progress.blockers` union schema, then
  render readiness from stored Goal Pack state, verified relations, and structured
  blockers. Do not add stored graph hints, scheduler semantics, or second state
  authority.

kernel_verdict:

- Ramanujan: one fact has one owner; edge authority is reduced to relations evidence or blocker wait condition.
- Kolmogorov: public surface adds one command and one small blocker union; no extra mode, scheduler, stored graph, or flag family.
- Godel: no second workflow, no second ledger, no second graph authority, no duplicate status transition system.

frozen_decisions:

- `goal-proof dag [target] --thread <id> [--json]` is adopted.
- `--thread` is required in MVP.
- `goal-proof dag` is read-only.
- `relations.links` remains verified relation evidence.
- `relations check` continues failing on missing hard predecessor evidence.
- `progress.blockers` owns pending wait conditions.
- structured blockers are first implementation slice.
- string blockers remain compatible but opaque.
- no free-text blocker parsing.
- no `relations.dag.predecessor_goal_ids` / `successor_goal_ids`.
- no `unblocks` inside blockers.
- no future `E999` inside pending blockers.
- JSON nodes use `goal_status`, `progress_status`, and `frontier_state`.
- readiness edges admit only `successor_of` / `depends_on` verified dependencies and structured `goal_completion` blockers.
- `related_to` and `supersedes` stay out of readiness edge admission.

non_goals:

- scheduler, queue, worklist, auto-run command, stored graph, thread lifecycle, thread registry.
- automatic unblock when predecessor completes.
- natural-language parsing of blockers.
- changing Goal Pack completion unit semantics.

allowed_reopen_surface:

- A strictly smaller command name can reopen only if it preserves the relations/frontier boundary.
- A smaller blocker schema can reopen only if it still supports machine-readable goal completion and decision blockers.
- Any proposal reintroducing stored edge hints, future evidence ids, or `unblocks` fails the reopen bar.

proof_obligations:

- Converge review must return no unresolved findings.
- Target proposal must stay saved as implementation-ready plan.
- Ledger must end with consensus achieved.
- Final diff must show no code implementation started.

delta_from_previous_round:

- Candidate proposal became adopted implementation plan.
- Structured blockers moved before DAG renderer.
- Edge authority and JSON contract are frozen.

## Round 2

phase: converge

input_residual:

- Verify stored edge hints / shadow DAG authority are removed.
- Verify structured blockers are first implementation slice.
- Verify no future `E999` or `unblocks` remains in pending blocker authority.
- Verify JSON contract separates stored state and derived frontier state.
- Verify bound implementation surface and test gates are complete.

findings:

| reviewer | verdict | residual risk |
| --- | --- | --- |
| A1 | 无 unresolved findings | YAML object blocker parser/serializer and `apply` preservation remain implementation risk. |
| A2 | 无 unresolved findings | W1 -> W2 -> W3 order must be kept to avoid schema/view coupling failures. |
| A3 | 无 unresolved findings | Parser/serializer remains the main W1 risk, already covered by tests. |
| A4 | 无 unresolved findings | Implementation risk remains in object blocker preservation, not in plan structure. |

counter_proposals:

- none

resolution_delta:

- No reopen.
- Freeze record kept.
- Target proposal remains saved as implementation-ready plan.

## Consensus

status: achieved

residual_risk:

- Parser/serializer details for structured YAML objects still require careful implementation.
- The first implementation Goal Pack should keep W1 and W2 separate enough to bisect failures.

final_verdict: >
  Consensus achieved. The proposal is implementation-ready as a schema-first,
  read-only DAG frontier plan. Remaining risk is implementation-local and covered
  by W1 parser/serializer/apply preservation tests.
