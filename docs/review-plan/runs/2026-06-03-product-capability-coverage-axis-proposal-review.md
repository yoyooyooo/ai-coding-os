# Plan Optimality Ledger: Product Proof Placement Lens

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
round_count: 2
challenge_scope: open
consensus_status: consensus
```

## Bootstrap

```yaml
target_complete: true
alignment_gate:
  policy: auto
  status: inferred
  resolved_points:
    - 用户明确调用 `$plan-optimality-loop` 评估目标 proposal。
    - 用户要求把 proposal 转化为可实施计划。
    - 用户明确允许强力挑战已有体系、目标函数、是否新增 skill、owner 边界和成功标准。
    - 本轮不开始实现 skill、eval、router 或 CLI，只修订 proposal 和 review ledger。
  open_questions: []
  confirmation_basis: >
    用户给出目标文件、review skill、实施计划转化目标和 open challenge 授权；
    信息足以冻结 review contract，无需先问。
review_contract:
  artifact_kind: implementation-plan
  review_goal: implementation-ready
  target_claim: >
    将 Product Capability Coverage Axis proposal 转化为可实施计划：评估是否应新增
    product-capability-coverage skill、如何定义 coverage / proof placement 输出、
    如何与 product-harness-system / ui-product-harness / headless-product-harness /
    interface-capability-planning / goal-proof 分工、哪些 waves 可落地、哪些边界必须冻结。
  target_refs:
    - docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
    - skills/router/ai-coding-os/SKILL.md
    - skills/harness/product-harness-system/SKILL.md
    - skills/harness/ui-product-harness/SKILL.md
    - skills/harness/headless-product-harness/SKILL.md
    - skills/capability/interface-capability-planning/SKILL.md
    - skills/README.md
    - docs/README.md
    - docs/product/README.md
    - docs/ssot/README.md
    - docs/standards/skill-source-layout.md
    - README.md
    - README.zh-CN.md
  non_default_overrides:
    alignment_policy: auto
    scope_fence: >
      可以挑战现有体系、是否新增 skill、目录 / owner 边界、成功标准、eval 和验收。
      输出必须收敛成更小、更稳、更可实施的候选；不得引入第二套 Harness artifact、
      第二套 Goal Pack contract、强制 durable artifact、CLI/schema 行为变化。
    stop_condition: consensus
    write_policy: >
      reviewer 不改文件；主 agent 合成后可修改目标 proposal、ledger 和必要索引。
review_object_manifest:
  source_inputs:
    - docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
    - /Users/yoyo/Documents/code/personal/agent-kit/skills/plan-optimality-loop/references/workflow.md
    - /Users/yoyo/Documents/code/personal/agent-kit/skills/plan-optimality-loop/references/ledger-schema.md
    - /Users/yoyo/Documents/code/personal/agent-kit/skills/plan-optimality-loop/references/reviewer-prompts.md
    - skills/router/ai-coding-os/SKILL.md
    - skills/harness/product-harness-system/SKILL.md
    - skills/harness/ui-product-harness/SKILL.md
    - skills/harness/headless-product-harness/SKILL.md
    - skills/capability/interface-capability-planning/SKILL.md
    - docs/standards/skill-source-layout.md
  materialized_targets:
    - docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
    - docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-proposal-review.md
  authority_target: docs/goal-proof/sources/2026-06-03-product-capability-coverage-axis-proposal.md
  bound_docs:
    - docs/goal-proof/README.md
    - docs/review-plan/README.md
    - docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-proposal-review.md
  derived_scope:
    artifact_kind: implementation-plan
    review_goal: implementation-ready
  allowed_classes:
    - proof placement lens
    - coverage / testing / regression routing
    - claim slicing and risk-axis discovery
    - owner recommendation and owner handoff
    - e2e / production-near sentinel selection criteria
    - root regression sink guidance
    - golden eval acceptance traces
    - skill promotion gate
  blocker_classes:
    - second Harness artifact or Harness Coverage Matrix variant
    - new Goal Pack schema or CLI behavior
    - coverage skill owning final placement, claim_ceiling, promotion, UI proof level, or headless sublevel
    - public skill / group / SSoT fact without same-wave docs and eval evidence
    - durable Coverage Map object
    - standalone runtime distribution claim
  ledger_target: docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-proposal-review.md
challenge_scope: open
reviewer_set:
  - A1
  - A2
  - A3
  - A4
active_advisors:
  - A4
activation_reason: >
  open scope plus public skill / owner boundary / success-standard challenge requires objective-function review.
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
  proposal 已保存为 implementation-ready plan；全部有效 reviewer unresolved findings 已合并或拒绝；
  freeze record 写入 adopted candidate、non-goals、proof obligations 和 residual risk；
  converge reviewer 不再发现直接支配方案。
reopen_bar: >
  只有能证明 adopted candidate 仍引入第二 Harness artifact、第二 coverage matrix、
  owner inversion、public surface overclaim，或在 dominance axes 上被更小更强方案严格支配，
  才允许 reopen。
ledger_path: docs/review-plan/runs/2026-06-03-product-capability-coverage-axis-proposal-review.md
writable: true
```

## Assumptions

| id | summary | status | resolution_basis |
| --- | --- | --- | --- |
| A-001 | 普通“怎么测 / regression 放哪层”必须新增独立 public skill。 | overturned | A1/A2/A3/A4 均指出 router + product-harness lens 是更小先验；新增 skill 只能作为 promotion decision。 |
| A-002 | `Coverage Map` 声明轻量就不会变成 artifact。 | overturned | A1/A2/A3/A4 均指出大写对象名、固定字段、promotion gate 会形成第二套 Harness Coverage Matrix。 |
| A-003 | coverage skill 可以拥有 proof placement 但不侵占 owner skill。 | overturned | Final placement、claim_ceiling、UI proof level、headless sublevel 仍归现有 owner。 |
| A-004 | eval 可以后置到 public route / skill 之后。 | overturned | Public route 或 owner 变化必须同波次有 golden eval / acceptance trace。 |
| A-005 | `coverage/` group 和 standalone mode 是低成本扩展。 | overturned | 增加 public source layout、README、SSoT、兼容预算；第一波不采纳。 |

## Rounds

### Round 1

```yaml
round: 1
phase: challenge
input_residual: initial product capability coverage axis proposal
```

#### Findings

| id | severity | class | summary | evidence | status |
| --- | --- | --- | --- | --- | --- |
| F-001 | critical | invalidity | 目标函数被“新增独立 skill”绑死，而 review 目标本应评估是否需要新增 skill。 | A1/A2/A3/A4；proposal 把 `product-capability-coverage` 写进 Adopted Candidate 和 Frozen Decisions。 | merged |
| F-002 | critical | invalidity | `Coverage Map` / `coverage_map` / `promotion_gate` 接近第二套 Harness Coverage Matrix。 | A1/A2/A3/A4；proposal output shape 含 status / gap / promotion fields；Product Harness 已拥有 Matrix、claim_ceiling、lifecycle。 | merged |
| F-003 | high | invalidity | coverage skill owning final placement / proof level 会和 UI/headless/harness owner 形成双重 authority。 | A1/A2/A3/A4；现有 owner skills 已拥有 proof ladder、claim_ceiling、placement rules。 | merged |
| F-004 | high | invalidity | Wave 1 扩 public surface，Wave 3 才补 eval，proof-strength 倒置。 | A1/A2/A3/A4；公开路由 / skill / SSoT 变化需要同波次行为级验收。 | merged |
| F-005 | high | controversy | 新 `coverage/` group 和 standalone mode 增加 source layout / public docs / compat budget。 | A1/A2/A3；当前 skill-source-layout 要求新分组同波次更新公开 docs 和 SSoT。 | merged |
| F-006 | medium | ambiguity | 验收主要是静态 rg，不能证明“用户行为矩阵不会变成全 e2e”。 | A2/A4；需要 golden prompt / eval 断言 claim slices、owner handoff、e2e sentinel reason、root regression sink。 | merged |
| F-007 | medium | ambiguity | target_layers 漏 root README、README.zh-CN、docs/product、docs/standards/skill-source-layout 等 public skill table surfaces。 | 主 agent inspection；若新增 public skill / group，这些必须同波次更新或不声明 public suite change。 | merged |

#### Counter Proposals

| id | summary | why_better | overturns_assumptions | resolves_findings | supersedes_proposals | dominance | axis_scores | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CP-001 | Router + Product Harness proof placement lens；不新增 skill。 | 最小概念数，复用 Product Harness placement owner，解决用户入口问题。 | A-001,A-002,A-003,A-005 | F-001,F-002,F-003,F-005,F-007 | initial Product Capability Coverage Axis | adopted |
| CP-002 | Eval-first / decision-gated rollout。 | 先证明 placement behavior，再决定是否扩 public surface。 | A-001,A-004 | F-004,F-006 | initial wave ordering | adopted |
| CP-003 | Thin skill only after promotion evidence。 | 保留 future headroom，但避免第一波 public overclaim。 | A-001,A-005 | F-001,F-005,F-007 | direct new skill | adopted-as-gate |
| CP-004 | Proof Placement Brief instead of Coverage Map。 | 去除第二 Matrix 风险；输出是 inline handoff, not artifact。 | A-002,A-003 | F-002,F-003,F-006 | Coverage Map | adopted |

#### Resolution Delta

- Proposal title changed from Product Capability Coverage Axis to Product Proof Placement Lens.
- First-wave plan no longer creates `product-capability-coverage`, `coverage/`, SSoT current fact, or Coverage Map.
- Wave 1 now targets router wording, Product Harness proof placement reference, and golden evals.
- Promotion to a thin skill becomes Wave 2 decision gate, not frozen first-wave work.
- Output changed to inline `Proof Placement Brief`.
- Verification now includes golden eval id checks and negative scans for new skill / Coverage Map / CLI changes.

### Round 2

```yaml
round: 2
phase: converge
input_residual: revised Decision-gated Product Proof Placement Lens proposal
```

#### Findings

| id | severity | class | summary | evidence | status |
| --- | --- | --- | --- | --- | --- |
| F-008 | low | controversy | `Proof Placement Brief` 仍有固定名称和字段形状，实施时可能漂移为 durable artifact。 | A2/A4 converge residual；proposal 已将其定义为 inline non-durable brief，并加入 negative scan。 | residual-risk |
| F-009 | low | controversy | `product-harness-system` lens 可能让 Product Harness 入口变重。 | A1 converge residual；proposal 用 Wave 2 promotion gate 承接该风险。 | residual-risk |

#### Reviewer Verdicts

| reviewer | status | verdict |
| --- | --- | --- |
| A1 | closed | 无 unresolved findings；未发现更小且更强的直接支配方案。 |
| A2 | closed | 无 unresolved findings；residual risk 是 brief 字段模板需靠 negative scan / golden eval 防漂移。 |
| A3 | closed | Replacement converge 无 unresolved findings；未发现更小更强直接支配方案。 |
| A4 | closed | 无 unresolved findings；revised candidate 等同 ALT1 + ALT2 的小步验证方案。 |

## Adoption

adopted_candidate: Decision-gated Product Proof Placement Lens

lineage:

- CP-001
- CP-002
- CP-003
- CP-004

rejected_alternatives:

- Direct Wave 1 `product-capability-coverage` public skill.
- New `coverage/` source group in Wave 1.
- Durable or quasi-durable `Coverage Map`.
- Coverage skill owning final placement, claim ceiling, UI proof level, headless sublevel, or promotion.
- Standalone mode that reproduces AI Coding OS owner taxonomy outside the suite.

rejection_reason:

- These alternatives increase concept-count, public-surface, compat-budget, and migration-cost before behavior evidence proves necessity; several create second-system risk against Product Harness and owner-local proof ladders.

dominance_verdict:

- Adopted candidate strictly improves concept-count, public-surface, compat-budget, and migration-cost over the initial proposal, and improves proof-strength by moving golden evals into Wave 1. Future-headroom remains open through a Wave 2 promotion gate.

### Freeze Record

adopted_summary:

```text
Implement a decision-gated Product Proof Placement Lens first: route coverage /
testing / regression / e2e-placement questions from ai-coding-os into
product-harness-system, add an inline Proof Placement Brief reference, and add
golden evals that prove user behavior matrices are decomposed into owner
handoffs and bounded e2e sentinels. Do not add a public skill, coverage group,
Coverage Map artifact, SSoT current fact, CLI/schema change, or standalone
distribution claim in Wave 1. A thin product-capability-coverage skill remains
only a Wave 2 promotion option if Wave 1 evidence proves it necessary.
```

kernel_verdict:

- Ramanujan: adopted candidate removes the new skill, new group, and Coverage Map object from the first wave.
- Kolmogorov: adopted candidate shortens public surface and replaces broad docs expansion with one reference plus golden evals.
- Godel: adopted candidate avoids second Harness artifact, second coverage matrix, and owner inversion.

frozen_decisions:

- Wave 1 does not add `product-capability-coverage`.
- Wave 1 does not add `skills/coverage/`.
- Wave 1 does not write SSoT current fact for a new skill.
- Output is an inline Proof Placement Brief, not a durable artifact.
- `Coverage Map`, `coverage_map`, `existing_coverage`, and `promotion_gate` are rejected active vocabulary for Wave 1.
- Final proof level, claim ceiling, Harness Coverage Matrix, UI proof ladder, and headless sublevel remain with existing owner skills.
- Golden evals must land in the same wave as router / lens changes.
- Promotion to a public skill requires Wave 2 evidence and same-wave public docs / skill-source-layout updates.

non_goals:

- No new Goal Pack schema or CLI parser/checker behavior.
- No new proof-level enum.
- No second Harness artifact or Matrix.
- No standalone runtime installation or downstream distribution claim.
- No root README / SSoT public skill table update unless a later wave actually promotes a public skill.

allowed_reopen_surface:

- Evidence proves Product Harness placement lens still makes `product-harness-system` too broad or confuses ordinary user entry.
- Golden evals prove a distinct route-time decomposition owner is necessary.
- A smaller plan maintains proof-strength while reducing public surface further.
- Revised proposal still leaks final placement authority or Matrix lifecycle into the lens.

proof_obligations:

- `bun run check`
- `python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .`
- `git diff --check`
- `python3 -m json.tool skills/harness/product-harness-system/evals/evals.json >/dev/null`
- Golden eval id presence check for proof placement lens.
- Negative scan for `skills/coverage`, `name: product-capability-coverage`, `Coverage Map`, `coverage_map`, `promotion_gate`, `existing_coverage` on active surfaces.
- `git diff -- packages/cli/src packages/cli/test` has no CLI/schema/checker diff.

delta_from_previous_round:

- Round 1 critical findings merged into the proposal rewrite.
- Direct new-skill implementation was replaced by decision-gated proof placement lens.
- Behavior-level evals moved from Wave 3 to Wave 1.

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
residual_risk:
  - Proof Placement Brief must remain inline recommendation, not durable artifact or evidence field.
  - Product Harness lens may become too broad; Wave 2 promotion gate handles that if golden evals expose repeated routing pressure.
```
