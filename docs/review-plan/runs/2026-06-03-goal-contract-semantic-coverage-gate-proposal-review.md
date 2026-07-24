# Goal Contract Claim Coverage Review Proposal Ledger

## Meta

```yaml
target: docs/goal-proof/inbox/2026-06-03-goal-contract-semantic-coverage-gate-proposal.md
targets:
  - docs/goal-proof/inbox/2026-06-03-goal-contract-semantic-coverage-gate-proposal.md
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
    - 用户明确调用 `$plan-optimality-loop` review 目标 proposal。
    - 用户目标是把既有 proposal 打磨成可实施方案。
    - 允许多 reviewer / subagents 挑战目标函数、字段落点、checker 边界和实施顺序。
    - 本轮不开始实现 CLI 或 skill 代码，只修订 proposal 和 review ledger。
  open_questions: []
  confirmation_basis: >
    用户给出目标文件、review skill、写入目标和期望产物。
review_contract:
  artifact_kind: implementation-plan
  review_goal: implementation-ready
  target_claim: >
    将 inbox proposal 收敛为可实施方案：为 Goal Proof 增加 owner-local claim
    coverage review，防止 objective 暗示的 multi-stage / real-runtime / authority
    范围被过宽 required_evidence 或 completion review 漏掉；第一波优先
    skill guidance、templates 和 completion review guidance，后续才考虑 CLI checker。
  target_refs:
    - docs/goal-proof/inbox/2026-06-03-goal-contract-semantic-coverage-gate-proposal.md
    - docs/goal-proof/README.md
    - docs/README.md
    - docs/standards/docs-governance.md
    - skills/goal/goal-contracts/SKILL.md
    - skills/goal/finding-proof-step/SKILL.md
    - skills/goal/proof-step-implementation/SKILL.md
    - skills/goal/goal-proof-system/SKILL.md
    - skills/goal/goal-proof-system/templates/evidence.jsonl
    - skills/goal/goal-proof-system/references/checker-rules.md
    - packages/cli/src/lib/goal-pack.ts
  non_default_overrides:
    alignment_policy: auto
    scope_fence: >
      不开始实现代码；不新增第二套 workflow、第二套 ledger、第二类 Goal Pack
      contract；保持 v2 Goal Pack schema 兼容。
    stop_condition: consensus
    write_policy: reviewer 不改文件；主 agent 合成后改目标 proposal、索引和本 ledger。
review_object_manifest:
  source_inputs:
    - docs/goal-proof/inbox/2026-06-03-goal-contract-semantic-coverage-gate-proposal.md
    - docs/goal-proof/README.md
    - docs/review-plan/README.md
    - plan-optimality-loop references/workflow.md
    - plan-optimality-loop references/ledger-schema.md
    - plan-optimality-loop references/reviewer-prompts.md
  materialized_targets:
    - docs/goal-proof/inbox/2026-06-03-goal-contract-semantic-coverage-gate-proposal.md
    - docs/review-plan/runs/2026-06-03-goal-contract-semantic-coverage-gate-proposal-review.md
  authority_target: docs/goal-proof/inbox/2026-06-03-goal-contract-semantic-coverage-gate-proposal.md
  bound_docs:
    - docs/goal-proof/README.md
    - docs/review-plan/README.md
  derived_scope:
    artifact_kind: implementation-plan
    review_goal: implementation-ready
  allowed_classes:
    - Goal Proof authoring guidance
    - completion review guidance
    - semantic risk trigger
    - claim coverage review
    - proof level boundary
    - existing v2 evidence surfaces
    - checker phase boundary
    - implementation waves
    - verification backlog
  blocker_classes:
    - new top-level goal/progress coverage field in wave 1
    - second proof modality enum
    - token naming DSL
    - semantic parser claim
    - ready gate formula rewrite
    - unbounded mandatory matrix for every goal
  ledger_target: docs/review-plan/runs/2026-06-03-goal-contract-semantic-coverage-gate-proposal-review.md
challenge_scope: open
reviewer_set:
  - A1
  - A2
  - A3
  - A4
active_advisors:
  - A4
activation_reason: >
  open scope plus public contract / schema-adjacent Goal Proof method change
  requires target-function challenge.
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
  只有能证明 adopted candidate 仍引入第二系统、checker overclaim、schema 破坏，
  或在 dominance axes 上严格支配，才允许 reopen。
ledger_path: docs/review-plan/runs/2026-06-03-goal-contract-semantic-coverage-gate-proposal-review.md
writable: true
```

## Assumptions

| id | summary | status | resolution_basis |
| --- | --- | --- | --- |
| A-001 | 语义覆盖必须靠新增矩阵字段表达。 | overturned | 全部 reviewer 认为现有 v2 surfaces 足够承载第一波。 |
| A-002 | proof modality 需要新增全局 enum。 | overturned | 复用现有 proof ladder 和 harness/project owner-local vocabulary 更稳。 |
| A-003 | required_evidence token 名称越长越诚实。 | overturned | 诚实性来自 claim/evidence/proof-level/gap 映射，不来自字符串 DSL。 |
| A-004 | ready gate 应新增 semantic audit 公式。 | overturned | ready 公式保持 stable contract + proof_step within claim_limit。 |
| A-005 | checker 可以第一波判断 objective semantic coverage。 | overturned | 第一波无 CLI 变化；后续最多 structural lint。 |
| A-006 | 每个 objective 关键词都应落点。 | overturned | 只审 claim-bearing axes。 |

## Round 1

phase: challenge

### Findings

| id | severity | class | summary | status |
| --- | --- | --- | --- | --- |
| F-001 | critical | invalidity | canonical home 未冻结，方案在 goal/progress/E999/字段之间分叉。 | adopted |
| F-002 | high | invalidity | trigger 范围未冻结，可能把所有 Goal Pack 变成矩阵流程。 | adopted |
| F-003 | high | invalidity | proof modality enum 会制造第二套 proof-level taxonomy。 | adopted |
| F-004 | high | invalidity | token 命名规则会变成字符串 DSL。 | adopted |
| F-005 | high | invalidity | ready gate 被扩成新 semantic audit phase。 | adopted |
| F-006 | medium | ambiguity | ready-time exclusion 和 completion-time exclusion 混用。 | adopted |
| F-007 | medium | controversy | Objective Coverage Matrix 名称会和 Harness Coverage Matrix 混淆。 | adopted |
| F-008 | medium | ambiguity | checker 后续边界过宽，容易伪装自然语言理解。 | adopted |
| F-009 | low | invalidity | target refs 有 stale path 且漏 `finding-proof-step`。 | adopted |

### Counter Proposals

| id | summary | why_better | dominance | status |
| --- | --- | --- | --- | --- |
| CP-001 | Existing-surface claim coverage review。 | 一个 invariant 贯穿现有 v2 lifecycle，无新增 contract。 | dominates | adopted |
| CP-002 | Semantic-risk trigger。 | 防住高风险 overclaim，不污染小目标。 | dominates | adopted |
| CP-003 | Reuse proof ladder。 | 避免第二套 proof taxonomy。 | dominates | adopted |
| CP-004 | Checker-later structural lint。 | 保留自动化空间，不承诺 parser。 | partial | adopted |
| CP-005 | Rename matrix to claim coverage review。 | 避免和 Harness Coverage Matrix 形成 artifact 混淆。 | partial | adopted |

### Resolution Delta

- 目标从 `Goal Contract Semantic Coverage Gate` 改为 `Triggered Claim Coverage Review`。
- canonical home 冻结为 E999 completion review；goal/progress 只放 authoring / proof-step guidance。
- 删除第一波新增字段、proof modality enum、token naming DSL、ready formula rewrite。
- 新增 semantic risk trigger 和 claim-bearing axes。
- 第一波实施路径改为 skills / templates / docs，无 CLI parser 变化。
- future checker 限定为 opt-in structural lint。

## Adoption

adopted_candidate: triggered-claim-coverage-review

lineage:

- A1 `ALT-A1-existing-surface-envelope`
- A1 `ALT-A2-triggered-gate`
- A1 `ALT-A3-proof-level-reuse`
- A2 `A2-ALT1`
- A2 `A2-ALT2`
- A2 `A2-ALT3`
- A3 `A3-ALT-1`
- A3 `A3-ALT-2`
- A3 `A3-ALT-3`
- A4 `ALT-001`
- A4 `ALT-002`
- A4 `ALT-003`

rejected_alternatives:

- New `semantic_coverage_notes` or `proof_modality_by_path` field: rejected because it creates a second goal/progress contract in wave 1.
- Global proof modality enum: rejected because existing proof ladder and harness vocabularies already own proof levels.
- Token naming DSL: rejected because checker cannot honestly parse proof semantics from token names.
- Ready gate formula rewrite: rejected because semantic coverage failure should trigger goal-contract repair or completion stop, not a sixth phase.
- Default mandatory matrix for every Goal Pack: rejected because it adds no proof value for small goals and makes the method disproportionate.
- Natural-language semantic checker: rejected because it overclaims CLI capability.

### Freeze Record

adopted_summary: >
  Implement a triggered claim coverage review using existing v2 Goal Pack
  surfaces. High-risk semantic goals must map claim slices to required evidence,
  evidence refs, proof level, and not_claimed / remaining_gaps in E999 completion
  review. First wave changes guidance and templates only; no CLI parser or
  schema behavior changes.

kernel_verdict:

- Ramanujan: removes new field, enum, DSL, and ready phase; one claim coverage home remains.
- Kolmogorov: shorter public surface; future checker is structural and opt-in.
- Godel: no second workflow, no second ledger, no second contract, no semantic parser overclaim.

frozen_decisions:

- The adopted name is `Triggered Claim Coverage Review`.
- First wave uses existing v2 surfaces only.
- E999 completion review is the canonical home for final claim coverage mapping.
- `goal.yaml` and `progress.yaml` get guidance, not new top-level fields.
- Semantic risk trigger gates mandatory use.
- Claim-bearing axes replace objective keyword extraction.
- Proof levels reuse existing proof ladder and owner-local harness vocabulary.
- `not_in_scope` is not introduced; use `non_goals` / `claim_limit` before run and `not_claimed` / `remaining_gaps` after run.
- First wave has no CLI parser/checker behavior change.
- Future checker can only be opt-in structural lint.

non_goals:

- Natural-language semantic parser.
- New Goal Pack schema field.
- New proof modality enum.
- Token naming convention enforcement.
- Mandatory matrix for every small goal.
- CLI implementation in this review turn.

allowed_reopen_surface:

- A strictly smaller first-wave patch set may reopen only if it still updates goal-contracts, proof-step, run, completion, and E999 template guidance.
- A stronger checker proposal may reopen only if it remains structural, opt-in, and does not parse objective natural language or token names.
- Any proposal adding wave-1 schema fields, second taxonomy, or ready formula rewrite fails reopen bar.

proof_obligations:

- Revised proposal saved.
- Ledger saved.
- Converge reviewers return no unresolved findings or residuals are captured.
- Static verification confirms no CLI implementation started.

delta_from_previous_round:

- Open questions closed.
- File-level patch contract added.
- Acceptance trace and future checker boundary sharpened.

## Round 2

phase: converge

input_residual:

- Verify F-001 to F-009 are closed by the revised proposal and freeze record.
- Verify adopted candidate is not directly dominated by a smaller stronger proposal.

### Findings

| reviewer | verdict | residual risk |
| --- | --- | --- |
| A1 | 无 unresolved findings。 | 后续实现仍需守住第一波不改 CLI parser / schema behavior，并用验证命令确认。 |
| A2 | 无 unresolved findings。 | 若后续把 structural lint 扩成 objective parser 或 token 命名检查，需要 reopen。 |
| A3 | 无 unresolved findings。 | 实施时仍需守住 guidance / templates / docs only，避免顺手改 CLI / schema 行为。 |
| A4 | 无 unresolved findings。 | 实施时仍需按验收项证明无 CLI parser / checker 行为变化，并跑 `bun run check` / `git diff --check`。 |

### Resolution Delta

- All round-1 findings remain closed.
- Adopted candidate was not directly dominated.
- No stale round result was used.

## Consensus

```yaml
status: achieved
adopted_candidate: triggered-claim-coverage-review
frozen_decisions_saved: true
target_saved: true
ledger_saved: true
stale_results_excluded: true
unresolved_findings: []
residual_risk:
  - Implementation must not drift from guidance/templates/docs into CLI parser or schema behavior in wave 1.
  - Future checker work must remain structural and opt-in unless a separate schema proposal is reviewed.
```
