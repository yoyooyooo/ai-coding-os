# Plan Optimality Ledger: Compiler Narrative Delta Proposal

## Meta

```yaml
target: docs/goal-proof/sources/2026-05-31-ai-coding-os-compiler-narrative-delta-proposal.md
targets:
  - docs/goal-proof/sources/2026-05-31-ai-coding-os-compiler-narrative-delta-proposal.md
source_kind: file-plan
reviewers:
  - A1-structure-purity
  - A2-token-economy
  - A3-dominance-alternatives
  - A4-objective-function
round_count: 3
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
    - 用户明确要求使用 `$plan-optimality-loop` 打磨这份顶层叙事提案。
    - 用户明确允许多 reviewer / subagents 参与。
    - 用户要求每一轮持续优化提案本体，直到多方没有进一步建议和异议。
    - 本轮目标在 `/Users/yoyo/Documents/code/personal/ai-coding-os` 源仓内完成，不回到 Fermi 实施 Goal Pack。
  open_questions: []
  confirmation_basis: >
    用户给出明确 skill、目标工件、write policy 和 stop condition：持续优化 proposal，
    直到彻底对齐。
review_contract:
  artifact_kind: implementation-plan
  review_goal: zero-unresolved
  target_claim: >
    这份顶层叙事 delta proposal 是否足够清晰、收敛、一致，能作为后续 README/docs/skill
    叙事升级的候选源；并且不引入第二套 workflow、schema 或 authority。
  target_refs:
    - docs/goal-proof/sources/2026-05-31-ai-coding-os-compiler-narrative-delta-proposal.md
    - AGENTS.md
    - README.zh-CN.md
    - README.md
    - docs/README.md
    - docs/product/README.md
    - docs/ssot/README.md
    - skills/README.md
  non_default_overrides:
    alignment_policy: auto
    scope_fence: >
      可以挑战目标函数、术语、文档落点、叙事主轴、采纳顺序、验收标准；
      不实现 README/docs/skill 改造；允许主 agent 根据 reviewer 结论持续修改 proposal 本体。
    stop_condition: consensus
    write_policy: >
      reviewer 不改文件；主 agent 可修改目标 proposal 和本 review ledger。
review_object_manifest:
  source_inputs:
    - docs/goal-proof/sources/2026-05-31-ai-coding-os-compiler-narrative-delta-proposal.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/workflow.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/reviewer-prompts.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/reviewer-views.md
    - AGENTS.md
    - docs/README.md
    - docs/product/README.md
    - docs/ssot/README.md
  materialized_targets:
    - docs/goal-proof/sources/2026-05-31-ai-coding-os-compiler-narrative-delta-proposal.md
    - docs/review-plan/runs/2026-05-31-compiler-narrative-delta-proposal-review.md
  authority_target: docs/goal-proof/sources/2026-05-31-ai-coding-os-compiler-narrative-delta-proposal.md
  bound_docs:
    - docs/review-plan/runs/2026-05-31-compiler-narrative-delta-proposal-review.md
  derived_scope:
    artifact_kind: implementation-plan
    review_goal: zero-unresolved
  allowed_classes:
    - top-level narrative
    - intent-to-evidence compiler model
    - Goal Proof artifact semantics
    - skill pass ownership
    - execution-strategy ownership boundary
    - Goal Horizon Check
    - Continuation Check
    - docs layer placement
    - adoption sequence and acceptance
  blocker_classes:
    - second workflow or second authority system
    - new schema or required Goal Pack field
    - compiler metaphor overclaiming runtime/compiler implementation
    - Terminal/Gate/Frontier promoted to normative Goal Modes
    - Continuation Turn or Window promoted to phase/workflow
    - proposal pretending to be SSoT/ADR
    - implementation steps mixed with narrative-source claim
  ledger_target: docs/review-plan/runs/2026-05-31-compiler-narrative-delta-proposal-review.md
challenge_scope: open
reviewer_set:
  - A1
  - A2
  - A3
  - A4
active_advisors:
  - A4
activation_reason: >
  open scope 且目标涉及长期顶层叙事、public surface、skill cluster 治理和目标函数，按默认启用 A4。
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
  全部 reviewer 对最新 proposal 和 freeze record 均返回无 unresolved findings；目标 proposal 已保存；
  本 ledger 写入 adopted candidate、rejected alternatives、residual risk。
reopen_bar: >
  只有能在 dominance axes 上严格支配 adopted candidate，或证明 proposal 仍会引入第二 workflow、
  schema pressure、authority 混淆、不可执行采纳路径，才允许 reopen。
ledger_path: docs/review-plan/runs/2026-05-31-compiler-narrative-delta-proposal-review.md
writable: true
```

## Round 1

phase: challenge

### Findings

| id | severity | class | summary | evidence | status |
|---|---|---|---|---|---|
| F-001 | blocker | invalidity | proposal 把顶层叙事 delta 扩成准标准、owner map、implementation plan 和验收清单。 | A2 指出文本同时定义 compiler loop、artifact 表、skill pass 表、两个命名检查、文档落点和验收。 | adopted |
| F-002 | blocker | invalidity | suite-wide compiler pass 叙事过宽，可能把独立 decision surfaces 误读成单一线性 pipeline。 | A4/A3 指出当前 skills/README 按 group ownership 和 decision surface 组织。 | adopted |
| F-003 | high | controversy | `Goal Horizon Check` / `Continuation Check` 作为大写规范名会扩大 public process surface。 | A1/A2/A3 均指出大写 Check 会被 README/AGENTS/skills 传播为新流程节点。 | adopted |
| F-004 | high | invalidity | SSoT promotion 建议把 compiler metaphor 写成事实层 authority。 | A1/A2/A3/A4 均指出 SSoT 只收事实、术语和不变量，不收隐喻句。 | adopted |
| F-005 | high | ambiguity | success criteria 偏“文案出现”，没证明原问题：自然续行必须写回 Goal Pack state。 | A4 要求最小 acceptance trace。 | adopted |
| F-006 | medium | ambiguity | Fermi review ledger 作为关键 provenance 会造成跨仓 authority leak。 | A1/A2/A3 要求内联 freeze summary，Fermi 路径只作来源背景。 | adopted |
| F-007 | medium | ambiguity | Diffusion 和 compiler 双隐喻并存未裁决，公共心智模型分叉。 | A2 指出现有 README 已有 Diffusion analogy。 | adopted |
| F-008 | medium | ambiguity | `minimum sufficient horizon` 缺正反例校准。 | A4 要求过远拒绝、过近拒绝、合法继续三类判断。 | adopted |

### Counter Proposals

| id | summary | why_better | resolves_findings | dominance | status |
|---|---|---|---|---|---|
| CP-001 | Minimal Compiler Overlay / state-transition loop：公共主线改成 `intent -> goal contract -> proof_step -> evidence -> next_action`。 | 复用现有 Goal Proof vocabulary，降低 concept-count 和 public-surface。 | F-001, F-002, F-007 | dominates on concept-count / public-surface / migration-cost | adopted |
| CP-002 | No New Check Names：删除顶层大写 Check，把目标距离和 evidence reduction 收为 owner-local 规则。 | 保留核心改进，不制造第二 workflow。 | F-003 | dominates on public-surface / compat-budget | adopted |
| CP-003 | Metaphor quarantine：compiler 只作 README/product 辅助隐喻；SSoT 只收 artifact ownership facts。 | 维护 authority hierarchy。 | F-004 | dominates on proof-strength / future-headroom | adopted |
| CP-004 | Acceptance trace + horizon calibration。 | 验收能证明自然续行写回 state，且能拒绝过近/过远目标。 | F-005, F-008 | dominates on proof-strength | adopted |
| CP-005 | Inline freeze summary；Fermi path 只作背景。 | 防止跨仓路径成为必读 authority。 | F-006 | dominates on compat-budget | adopted |

### Resolution Delta

- 重写 proposal 标题和主线为 `Intent-to-Evidence State Transition`。
- 公共 loop 压缩为 `human intent -> goal contract -> proof_step -> evidence -> next_action`。
- 删除 suite-wide compiler pass ownership 表。
- 删除顶层 `Goal Horizon Check` / `Continuation Check` 规范名。
- SSoT 落点改为 artifact ownership / invariant only。
- 新增 `Dominance Freeze`、`Layer Adoption Matrix`、`Acceptance Trace` 和 horizon calibration。
- Fermi review ledger 降级为来源背景，adopted constraints 已内联。

## Adoption

adopted_candidate: goal-proof-first-state-transition-overlay

lineage:

- A1 `ALT-1`
- A1 `ALT-2`
- A1 `ALT-3`
- A2 `A2-ALT-1`
- A2 `A2-ALT-2`
- A2 `A2-ALT-3`
- A2 `A2-ALT-4`
- A3 `A3-ALT-1`
- A3 `A3-ALT-2`
- A3 `A3-ALT-3`
- A3 `A3-ALT-4`
- A4 `A4-ALT-01`
- A4 `A4-ALT-02`
- A4 `A4-ALT-03`
- A4 `A4-ALT-04`

rejected_alternatives:

- `suite-wide compiler pipeline`: rejected because it linearizes independent decision surfaces.
- `public Goal Horizon Check / Continuation Check`: rejected because it creates new process primitives.
- `compiler metaphor in SSoT`: rejected because SSoT should hold artifact facts, not metaphor.
- `Fermi ledger as required authority`: rejected because cross-repo source should not be necessary for source repo adoption.

### Freeze Record

adopted_summary: >
  The proposal now defines a thin Goal Proof-first state-transition overlay.
  Public narrative should use existing Goal Proof vocabulary: human intent -> goal contract -> proof_step -> evidence -> next_action.
  Compiler remains a light explanatory metaphor, not a new workflow, schema, or suite-wide pipeline.

frozen_decisions:

- Use `state transition` as public mainline; keep `compiler` as optional README/product metaphor.
- Do not create public Goal Modes.
- Do not create public `Goal Horizon Check` / `Continuation Check` primitives.
- Keep target-distance logic as an owner-local `goal-contracts` criterion: `minimum sufficient horizon`.
- Keep evidence-after-state logic as an owner-local `proof-step-implementation` rule: reduce evidence into existing Goal Pack state.
- SSoT may only receive artifact ownership / invariant facts, not compiler metaphor facts.
- README must not carry full decision tables.
- skills/README must not add a second pass ownership matrix.

proof_obligations:

- Run converge review against the rewritten proposal.
- Verify no `Terminal/Gate/Frontier` normative mode is introduced.
- Verify no required YAML field / schema / CLI / next_action is introduced.
- Verify acceptance trace covers over-near, over-far, and valid continuation cases.
- Verify README adoption does not leave `Diffusion`, `compiler`, and `state transition` as three parallel public models.

## Consensus

```yaml
status: achieved
rounds_completed: 3
unresolved_findings: []
residual_risk:
  - 后续实施 README / docs / skills 时仍需遵守 Layer Adoption Matrix。
  - 最大回归风险是把 compiler 隐喻重新扩成 suite-wide pipeline，或把 owner-local rules 写成公共 workflow。
```

## Round 2

phase: converge

### Findings

| id | severity | class | summary | evidence | status |
|---|---|---|---|---|---|
| F-009 | minor | ambiguity | README 现有 `Diffusion` 隐喻去留未写入 adoption matrix，可能与 state-transition / compiler 形成三模型并存。 | A2 Round 2 residual。 | adopted |

### Resolution Delta

- 在 proposal 的 Layer Adoption Matrix 后补充：README 采纳时必须将 `Diffusion` 并入 state-transition loop，或降级为 legacy metaphor；不得保留三个并列公共模型。

```yaml
round_2_verdict:
  A1: no_unresolved_findings
  A2: minor_residual_adopted
  A3: no_unresolved_findings
  A4: no_unresolved_findings
```

## Round 3

phase: converge

### Residual Check

| reviewer | verdict |
|---|---|
| A1-structure-purity | 无 unresolved findings。三模型并存风险已封口。 |
| A2-token-economy | 无 unresolved findings。`state transition` 是公共主线，`compiler` 仅辅助隐喻，`Diffusion` 必须并入 loop 或降级为 legacy metaphor。 |
| A3-dominance-alternatives | 无 unresolved findings。 |
| A4-objective-function | 无 unresolved findings。三模型并存风险已封口。 |

### Final Freeze

```yaml
adopted_candidate: goal-proof-first-state-transition-overlay
consensus_status: achieved
final_public_mainline: intent-to-evidence state transition
compiler_metaphor: README/product auxiliary only
diffusion_metaphor: merge_into_state_transition_loop_or_demote_to_legacy
ssot_policy: artifact_invariants_only
schema_change: false
cli_change: false
skill_behavior_change: false
```
