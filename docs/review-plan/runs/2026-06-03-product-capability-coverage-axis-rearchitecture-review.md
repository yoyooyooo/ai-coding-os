# Plan Optimality Ledger: Product Capability Coverage Re-architecture

## Meta

```yaml
target: docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
targets:
  - docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
source_kind: file-plan
reviewers:
  - A1-structure-purity
  - A2-token-economy
  - A3-dominance-alternatives
  - A4-objective-function
  - A5-standalone-ecosystem
round_count: 2
challenge_scope: open-max
consensus_status: consensus
```

## Bootstrap

```yaml
target_complete: true
alignment_gate:
  policy: auto
  status: inferred
  resolved_points:
    - 用户要求重新走 `$plan-optimality-loop`。
    - 用户明确说明独立 `product-capability-coverage` 的动机是 standalone reuse 和产品能力拆解本身是单独能力。
    - 用户要求抛开“先验证再改”前提，将已有 `skills/**` 视为新体系初始输入，可完全打散重组。
    - 本轮不开始实现，只冻结新的可实施计划和 ledger。
  open_questions: []
  confirmation_basis: >
    用户明确给出前一轮结论的挑战点、独立 skill 的目标函数、最大力度挑战授权和 skill 调用。
review_contract:
  artifact_kind: implementation-plan
  review_goal: implementation-ready
  target_claim: >
    在最大力度挑战下，冻结新的可实施方案：把“产品能力/用户行为/bug/workflow 如何拆成
    claim slices、proof placement、e2e sentinel 与 regression sink”作为可独立使用的能力；
    允许新增独立 product-capability-coverage skill；允许把现有 skills/** 当初始输入完全
    打散重组；同时避免第二套 Harness artifact、Goal Pack schema、CLI 行为和无边界 mega skill。
  target_refs:
    - docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
    - docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-proposal-review.md
    - skills/README.md
    - skills/router/ai-coding-os/SKILL.md
    - skills/harness/product-harness-system/SKILL.md
    - skills/harness/ui-product-harness/SKILL.md
    - skills/harness/headless-product-harness/SKILL.md
    - skills/capability/interface-capability-planning/SKILL.md
    - README.md
    - README.zh-CN.md
    - docs/README.md
    - docs/product/README.md
    - docs/ssot/README.md
    - docs/standards/skill-source-layout.md
  non_default_overrides:
    alignment_policy: auto
    scope_fence: >
      可挑战现有体系和上一轮 decision-gated plan；不把少 public surface 当默认目标。
      不开始实现；不得引入 CLI/schema、第二 Harness artifact、Goal Pack schema、测试 runner
      ownership 或无边界 mega skill；必须说明 standalone 最小语义。
    stop_condition: consensus
    write_policy: >
      reviewer 不改文件；主 agent 合成后可修改目标 proposal、ledger 和必要索引。
review_object_manifest:
  source_inputs:
    - docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
    - docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-proposal-review.md
    - skills/**
    - README.md
    - README.zh-CN.md
    - docs/README.md
    - docs/product/README.md
    - docs/ssot/README.md
    - docs/standards/skill-source-layout.md
  materialized_targets:
    - docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
    - docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-rearchitecture-review.md
  authority_target: docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
  bound_docs:
    - docs/goal-proof/README.md
    - docs/review-plan/README.md
    - docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-rearchitecture-review.md
  derived_scope:
    artifact_kind: implementation-plan
    review_goal: implementation-ready
  allowed_classes:
    - standalone product capability coverage skill
    - product capability / bug / workflow / behavior-matrix decomposition
    - generic proof-home taxonomy
    - e2e sentinel and root regression sink
    - optional AI Coding OS integrations
    - skill source layout and public docs sync
    - eval coverage
  blocker_classes:
    - second Harness artifact or Harness Coverage Matrix variant
    - Goal Pack schema or CLI/checker behavior change
    - product truth or test runner ownership
    - final placement / claim_ceiling / UI-headless ladder ownership
    - unbounded mega skill
    - downstream installed-state claim
  ledger_target: docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-rearchitecture-review.md
challenge_scope: open-max
reviewer_set:
  - A1
  - A2
  - A3
  - A4
  - A5
active_advisors:
  - A4
  - A5
activation_reason: >
  open-max challenge touches public skill surface, standalone semantics, skill source layout, and objective function.
max_reviewer_count: 5
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
  proposal is rewritten to implementation-ready; all reviewer blockers are merged or explicitly rejected;
  adopted freeze record and public-surface obligations are recorded; converge returns no unresolved findings.
reopen_bar: >
  Reopen only if adopted plan still lacks standalone semantics, leaks final proof authority, creates second Harness/Goal/CLI system,
  or a smaller plan preserves standalone value and dominates on the workflow axes.
ledger_path: docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-rearchitecture-review.md
writable: true
```

## Assumptions

| id | summary | status | resolution_basis |
| --- | --- | --- | --- |
| A-001 | 更少 public surface 默认更优。 | overturned | A1/A3/A4/A5 指出 standalone reuse 是本轮目标函数的一等项。 |
| A-002 | `product-harness-system` 是 proof placement 的中性宿主。 | overturned | A1/A3/A4 指出它已拥有 Harness artifact / Matrix / claim_ceiling，会吞掉 pre-owner decomposition。 |
| A-003 | standalone semantics 等同 downstream installed-state claim。 | overturned | A4/A5/A2 区分 `source_standalone_semantics=true` 和 `downstream_distribution_claimed=false`。 |
| A-004 | 独立 skill 必然导致第二 Harness artifact。 | overturned | Reviewers converged on thin skill with strict `does_not_own` firewall. |
| A-005 | 新 skill 需要新 `coverage/` group。 | overturned | A1/A2/A3/A5 converged on `skills/capability/` for Wave 1. |

## Rounds

### Round 1

```yaml
round: 1
phase: challenge
input_residual: prior decision-gated proof placement lens proposal
```

#### Findings

| id | severity | class | summary | evidence | status |
| --- | --- | --- | --- | --- | --- |
| F-001 | critical | invalidity | Prior proposal did not satisfy standalone skill objective. | A1/A3/A4/A5; proposal explicitly deferred public skill to Wave 2. | merged |
| F-002 | critical | invalidity | Hosting pre-owner claim slicing in `product-harness-system` causes owner inversion. | A1/A3/A4; Product Harness already owns Harness artifact, Matrix, claim_ceiling. | merged |
| F-003 | critical | ambiguity | Standalone output leaked AI Coding OS owner skill taxonomy. | A5; prior `next_owner_handoff` named suite skills as default output. | merged |
| F-004 | high | ambiguity | Standalone minimal vocabulary was missing. | A5; prior plan relied on claim_ceiling / Harness Matrix / Goal Pack terms for boundary. | merged |
| F-005 | high | controversy | `product-capability-coverage` name may imply coverage status or Harness Matrix authority. | A1/A2; accepted with explicit name boundary and negative evals. | merged |
| F-006 | high | invalidity | Public skill change requires same-wave README / docs / SSoT / skill-source-layout updates. | A2/main inspection; root READMEs and docs list full skill suite. | merged |
| F-007 | medium | invalidity | Evals must live with new skill and prove behavior, not only text presence. | A2/A3/A4; accepted eval ids and negative expectations. | merged |

#### Counter Proposals

| id | summary | why_better | overturns_assumptions | resolves_findings | supersedes_proposals | dominance | axis_scores | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CP-001 | Standalone Core + Optional Suite Integrations. | Satisfies standalone reuse while keeping OS owners optional. | A-001,A-003 | F-001,F-003,F-004 | prior decision-gated lens | adopted |
| CP-002 | Thin `product-capability-coverage` under `skills/capability/`. | Adds the needed public trigger without new group churn. | A-002,A-005 | F-001,F-002,F-005,F-006 | `coverage/` group and router-only lens | adopted |
| CP-003 | Generic proof-home vocabulary by default. | Prevents standalone output from requiring AI Coding OS. | A-003 | F-003,F-004 | suite-owner default output | adopted |
| CP-004 | Behavior evals in the new skill. | Proves feature/bug/workflow decomposition and boundary negatives. | A-004 | F-005,F-007 | static-only validation | adopted |

#### Resolution Delta

- Proposal title changed to Product Capability Coverage Skill Proposal.
- Adopted candidate changed to Standalone Product Capability Coverage Core + Optional AI Coding OS Integrations.
- Wave 1 now adds `skills/capability/product-capability-coverage/SKILL.md`.
- `coverage/` group is rejected for Wave 1.
- Standalone generic vocabulary and proof homes are defined.
- AI Coding OS owner skills moved to optional integration mapping.
- Same-wave public docs / SSoT / skill-source-layout updates are required.

### Round 2

```yaml
round: 2
phase: converge
input_residual: rewritten standalone product-capability-coverage proposal
```

#### Findings

| id | severity | class | summary | evidence | status |
| --- | --- | --- | --- | --- | --- |
| F-008 | low | controversy | `product-capability-coverage` may still be misread as coverage status or Harness Matrix authority. | A1/A2 converge; proposal now defines name boundary, `does_not_own`, evals, and negative scans. | residual-risk |
| F-009 | low | controversy | New public skill increases docs maintenance surface. | A2/A5 converge; proposal requires same-wave README / docs / SSoT / skill-source-layout updates. | residual-risk |
| F-010 | low | ambiguity | Optional AI Coding OS integrations could leak into standalone output. | A5 converge; proposal makes generic proof homes default and adds standalone-no-os-taxonomy eval. | residual-risk |

#### Counter Proposals

| id | summary | why_better | overturns_assumptions | resolves_findings | supersedes_proposals | dominance | axis_scores | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CP-005 | Keep the adopted standalone thin skill with explicit residual controls. | No smaller alternative preserves standalone reuse without reintroducing owner inversion or router-only failure. | A-001,A-002,A-003,A-004,A-005 | F-008,F-009,F-010 | none | dominates | concept-count: moderate; public-surface: moderate; compat-budget: high; migration-cost: moderate; proof-strength: high; future-headroom: high | adopted |

#### Resolution Delta

- No unresolved findings remained.
- Residual risks were retained as implementation controls, not blockers.
- Consensus status was frozen after A1/A2/A3/A4/A5 converge verdicts.

## Adoption

adopted_candidate: Standalone Product Capability Coverage Core + Optional AI Coding OS Integrations

lineage:

- CP-001
- CP-002
- CP-003
- CP-004

rejected_alternatives:

- Prior decision-gated Product Proof Placement Lens as first-wave target.
- `product-harness-system` hosted proof placement lens as primary entry.
- New `coverage/` group in Wave 1.
- Full task-axis suite rearchitecture in Wave 1.
- Any Coverage Map / coverage status / Harness Matrix replacement.

rejection_reason:

- They either fail standalone semantics, create owner inversion, add unnecessary layout churn, or risk second-system behavior.

dominance_verdict:

- Adopted candidate is stronger on proof-strength and future-headroom because it directly supports standalone product capability coverage.
- It costs one new public skill, but avoids a new group and avoids broad skill-suite rearchitecture.
- It preserves compatibility by keeping AI Coding OS owner skills as optional integrations and changing no CLI/schema.

### Freeze Record

adopted_summary:

```text
Wave 1 adds a standalone thin `product-capability-coverage` skill under
`skills/capability/`. It owns product capability claim slicing, risk-axis
discovery, generic proof-home recommendation, e2e sentinel rationale, and root
regression sink handoff. It does not own product truth, final placement,
Harness Coverage Matrix, claim_ceiling, UI/headless proof ladders, Goal Pack
evidence, or test runners. AI Coding OS skill owners are optional integrations.
Public docs, SSoT, skill-source-layout, router, handoff consumers, and evals
update in the same wave.
```

kernel_verdict:

- Ramanujan: a thin standalone skill is cleaner than making Product Harness host pre-owner decomposition.
- Kolmogorov: one new skill plus same-wave docs is cheaper than a new `coverage/` group or full suite rearchitecture.
- Godel: strict `does_not_own` and optional integration boundaries avoid second Harness / Goal / CLI systems.

frozen_decisions:

- Wave 1 adds `product-capability-coverage`.
- It lives under `skills/capability/` in Wave 1.
- No `skills/coverage/` group in Wave 1.
- `source_standalone_semantics: true`.
- `downstream_distribution_claimed: false`.
- Default output uses generic proof homes, not AI Coding OS skill names.
- AI Coding OS owner skills are optional integrations.
- Handoff is recommendation, not final authority.
- `coverage` in the name means route-time claim/risk coverage analysis, not Harness Coverage Matrix or coverage status.
- Public README / docs / SSoT / skill-source-layout must update in the same wave.

non_goals:

- No CLI / Goal Pack schema / checker behavior change.
- No Harness Coverage Matrix replacement or second Harness artifact.
- No product truth ownership.
- No test runner, Playwright script, command, fixture, replay, or concrete test implementation ownership.
- No UI/headless proof ladder ownership.
- No Goal Pack evidence or completion review ownership.
- No downstream runtime installed-state claim.
- No `coverage/` group in Wave 1.

allowed_reopen_surface:

- Implementation cannot express standalone generic vocabulary without leaking AI Coding OS owner taxonomy.
- `product-capability-coverage` starts owning final proof placement, claim_ceiling, runner, Harness Matrix, or evidence lifecycle.
- Public docs cannot be synchronized in the same wave.
- A smaller plan preserves standalone value and avoids owner inversion.

proof_obligations:

- `bun run check`
- `python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .`
- `git diff --check`
- `python3 -m json.tool skills/capability/product-capability-coverage/evals/evals.json >/dev/null`
- `rg -n "product-capability-coverage" README.md README.zh-CN.md docs/README.md docs/product/README.md docs/ssot/README.md docs/standards/skill-source-layout.md skills/README.md skills/router/ai-coding-os/SKILL.md`
- Eval id presence checks for the six product-capability-coverage evals.
- Negative scan for `Coverage Map`, `coverage_map`, `coverage status`, and `new proof-level enum` on active surfaces.
- `git diff -- packages/cli/src packages/cli/test` has no CLI/schema/checker diff.

delta_from_previous_round:

- Reopened prior consensus because standalone reuse and product capability coverage were upgraded to first-class target-function terms.
- Replaced router + Product Harness lens with standalone thin skill.
- Kept the prior anti-second-system constraints.

## Consensus

```yaml
status: consensus
rounds_completed: 2
unresolved_findings: []
reviewer_final_verdicts:
  A1: no unresolved findings
  A2: no unresolved findings
  A3: no unresolved findings
  A4: no unresolved findings
  A5: no unresolved findings
residual_risk:
  - product-capability-coverage name can be misread as coverage status; must be controlled by frontmatter, does_not_own, evals, and negative scans.
  - new public skill increases docs maintenance surface; same-wave public docs sync is required.
  - optional_integrations must not leak AI Coding OS owner taxonomy into standalone-only output.
```
