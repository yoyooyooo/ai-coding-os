# Plan Optimality Ledger: Interface Capability And Harness Boundary Upgrade

## Meta

```yaml
target: docs/goal-proof/sources/2026-05-31-interface-capability-harness-boundary-upgrade-proposal.md
targets:
  - docs/goal-proof/sources/2026-05-31-interface-capability-harness-boundary-upgrade-proposal.md
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
    - 用户明确要求先用 `$handoff` 写提案，再用 `$plan-optimality-loop` 打磨成可实施计划。
    - 用户明确要求使用多 reviewer 路径。
    - 本轮目标是 AI Coding OS 仓库，不是 Fermi 仓实现。
    - 本轮只产出提案、review ledger 和可实施计划，不开始修改 skill 正文。
  open_questions: []
  confirmation_basis: >
    用户给出了目标主题、方法顺序、write intent 和多 reviewer loop 要求；关键信息足以直接冻结。
review_contract:
  artifact_kind: implementation-plan
  review_goal: implementation-ready
  target_claim: >
    把 Fermi 中 InterfaceCapability vs ProductHarness 的分层经验提炼到 AI Coding OS，
    使现有 `$interface-capability-planning`、`$product-harness-system`、`$ui-product-harness`
    和 `$headless-product-harness` 可实施地补强；不新增 skill，不引入第二套 harness
    vocabulary，不把 Fermi 产品对象上浮为 OS doctrine。
  target_refs:
    - docs/goal-proof/sources/2026-05-31-interface-capability-harness-boundary-upgrade-proposal.md
    - skills/capability/interface-capability-planning/SKILL.md
    - skills/capability/interface-capability-planning/references/planning-workflow.md
    - skills/harness/product-harness-system/SKILL.md
    - skills/harness/product-harness-system/references/artifact-model.md
    - skills/harness/product-harness-system/references/trace-contract.md
    - skills/harness/product-harness-system/references/claim-ceilings.md
    - skills/harness/product-harness-system/references/lifecycle-and-placement.md
    - skills/harness/ui-product-harness/SKILL.md
    - skills/harness/ui-product-harness/references/harness-ladder.md
    - skills/harness/headless-product-harness/SKILL.md
    - skills/harness/product-harness-system/evals/evals.json
    - skills/harness/ui-product-harness/evals/evals.json
    - skills/goal/goal-proof-system/references/artifact-routing.md
  non_default_overrides:
    alignment_policy: auto
    scope_fence: >
      可以挑战提炼目标、落点、实施顺序、eval 设计、是否需要改 README/docs；
      不开始实现 skill 修改；不能要求新建 skill；不能引入第二套 harness vocabulary。
    stop_condition: implementation-ready
    write_policy: >
      reviewer 不改文件；主 agent 可修改 proposal 和本 ledger。
review_object_manifest:
  source_inputs:
    - /var/folders/sf/rnr3jjbn3qb0c43yyjl3p9900000gn/T/handoff-XXXXXX.md.PkRaVlG4HX
    - docs/goal-proof/sources/2026-05-31-interface-capability-harness-boundary-upgrade-proposal.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/workflow.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/ledger-schema.md
    - /Users/yoyo/.agents/skills/plan-optimality-loop/references/reviewer-prompts.md
    - Fermi docs/interface-capabilities/README.md
    - Fermi docs/product-harness/README.md
  materialized_targets:
    - docs/goal-proof/sources/2026-05-31-interface-capability-harness-boundary-upgrade-proposal.md
    - docs/review-plan/runs/2026-05-31-interface-capability-harness-boundary-upgrade-review.md
  authority_target: docs/goal-proof/sources/2026-05-31-interface-capability-harness-boundary-upgrade-proposal.md
  bound_docs:
    - docs/review-plan/runs/2026-05-31-interface-capability-harness-boundary-upgrade-review.md
  derived_scope:
    artifact_kind: implementation-plan
    review_goal: implementation-ready
  allowed_classes:
    - InterfaceCapability / Product Harness ownership boundary
    - UI proof vs headless product proof claim boundary
    - claim ceiling and minimum proof matrix
    - Goal Pack companion placement handoff
    - skill reference update plan
    - eval coverage plan
  blocker_classes:
    - new skill requirement
    - second harness vocabulary
    - Fermi product vocabulary promoted to OS doctrine
    - Product Harness owning Goal Pack lifecycle
    - InterfaceCapability owning claim_ceiling
    - UI proof reported as business fact without product-authority evidence
    - unbound eval runner or unowned eval file
  ledger_target: docs/review-plan/runs/2026-05-31-interface-capability-harness-boundary-upgrade-review.md
challenge_scope: open
reviewer_set:
  - A1
  - A2
  - A3
  - A4
active_advisors:
  - A4
activation_reason: >
  open scope 且目标涉及长期 skill 边界、public/internal proof surface 和成功标准，按默认启用 A4。
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
  proposal 已保存为 implementation-ready plan；全部 reviewer 的有效 blocker 被合并或拒绝；
  freeze record 写入 adopted candidate、non-goals、proof obligations 和 residual risk。
reopen_bar: >
  只有能证明 adopted candidate 仍引入双重 owner、双重 vocabulary、claim_ceiling 泄漏、
  lifecycle authority 混乱，或能在 dominance axes 上严格支配，才允许 reopen。
ledger_path: docs/review-plan/runs/2026-05-31-interface-capability-harness-boundary-upgrade-review.md
writable: true
```

## Assumptions

| id | summary | status | resolution_basis |
|---|---|---|---|
| A-001 | 四层模型比现有 skill handoff 更清楚。 | overturned | A1/A3/A4 均指出会增加 public concept count；adopted plan 改为 two contracts plus two proof routes。 |
| A-002 | Product Harness 可以定义 Goal Pack companion promotion verdict。 | overturned | A1/A2/A3/A4 均指出 Product Harness 不拥有 Goal/docs lifecycle；adopted plan 改为 owner-preserving handoff packet。 |
| A-003 | `required_levels` 可作为 InterfaceCapability 完成要求。 | overturned | InterfaceCapability 只能声明 coverage intent / claim intent；claim_ceiling 和 coverage status 归 Harness。 |
| A-004 | paired headless proof 足以支持 business fact claim。 | overturned | adopted plan 使用 claim-to-minimum-proof matrix；headless sublevel 必须匹配 claim 类型。 |
| A-005 | 新增 eval 越多越好。 | overturned | adopted plan 只补 eval delta，避免重复已有 screenshot / Playwright overclaim eval。 |

## Rounds

### Round 1

```yaml
round: 1
phase: challenge
input_residual: initial handoff proposal
```

#### Findings

| id | severity | class | summary | evidence | status |
|---|---|---|---|---|---|
| F-001 | high | invalidity | 初稿的“四层防混淆规则”会把 UI Harness / Headless Harness 固化成新 authority 层，接近第二套 harness vocabulary。 | A1/A3/A4；现有 Product Harness System 已统一拥有 Harness vocabulary。 | merged |
| F-002 | high | invalidity | Step 4 把 Goal Pack companion promotion verdict 放进 Product Harness，越权定义 Goal/docs lifecycle。 | A1/A2/A3/A4；`product-harness-system` 不拥有 Goal Pack evidence records 或 docs authority；Goal companion rules 已在 Goal Proof artifact routing。 | merged |
| F-003 | medium | ambiguity | `required_levels` 容易让 InterfaceCapability 拥有 completion / claim ceiling。 | A2/A3；InterfaceCapability 只能声明 coverage intent 或 harness needs。 | merged |
| F-004 | medium | invalidity | “business_fact_claim requires paired headless_product evidence”过粗，会把弱 headless proof 当成强 product fact。 | A3；headless sublevel 分 boundary/offline_fixture/replay/adapter/projection/db_backed/real_runtime_opt_in。 | merged |
| F-005 | medium | controversy | eval 计划重复已有 screenshot/business fact 和 Playwright-without-headless negative case。 | A1/A2/A3/A4；已有 `product-harness-system` eval #2 和 `ui-product-harness` eval #3。 | merged |
| F-006 | medium | ambiguity | 初稿 verification 只能证明 repo 健康，不能证明 target_claim。 | A1/A4；需要 JSON parse、forbidden-term scan、新 eval presence check。 | merged |
| F-007 | low | ambiguity | README 是否更新不应按 public/internal 直觉判断，应按 entrypoint ownership/routing/stop 是否变化判断。 | A3；skill public surface 是 `SKILL.md` 和 reference，而不只是 README。 | merged |

#### Counter Proposals

| id | summary | why_better | overturns_assumptions | resolves_findings | supersedes_proposals | dominance | axis_scores | status |
|---|---|---|---|---|---|---|---|---|
| CP-001 | Boundary Drift Prevention Patch：只补 IC 不内嵌 proof implementation、Harness 不改写 IC、UI proof 不升级 product fact。 | 更小、更可证伪，直接打过度声明和跨 owner 改写风险。 | A-001 | F-001,F-003,F-005,F-006 | initial four-layer upgrade | dominates | concept-count:+2; public-surface:+1; compat-budget:+2; migration-cost:+2; proof-strength:+1; future-headroom:+1 | adopted |
| CP-002 | Companion Handoff Packet：Product Harness 只输出 candidate trace / handoff packet，promotion verdict 交给 Goal Proof / docs-governance。 | 保留 trace 价值，消除第二 lifecycle authority。 | A-002 | F-002 | initial companion promotion | dominates | concept-count:+1; public-surface:+1; compat-budget:+2; migration-cost:+1; proof-strength:0; future-headroom:+2 | adopted |
| CP-003 | Claim-to-minimum-proof matrix：不同 claim 绑定最低诚实 proof level / headless sublevel。 | 防止“有 headless ref 就能声明 business fact”。 | A-004 | F-004,F-006 | coarse paired claim rule | partial | concept-count:0; public-surface:0; compat-budget:+1; migration-cost:0; proof-strength:+2; future-headroom:+1 | adopted |
| CP-004 | Eval delta only：只新增两个缺口 eval，已有重复 eval 只按需收紧 expected_output。 | 降低维护重复，成功标准直接对应 drift 风险。 | A-005 | F-005,F-006 | broad eval add list | dominates | concept-count:+1; public-surface:0; compat-budget:+1; migration-cost:+1; proof-strength:+1; future-headroom:+1 | adopted |

#### Resolution Delta

- Proposal 从 `Boundary Upgrade Proposal` 改为 `Boundary Drift Prevention Plan`。
- 删除 “four distinct layers” 叙事，冻结为 `InterfaceCapability` / `Product Harness System`
  两类 contract 与 `UI Product Harness` / `Headless Product Harness` 两条 proof route。
- Step 4 从 promotion verdict 改为 owner-preserving handoff packet。
- Verification 新增 targeted JSON parse、forbidden-term scan 和 eval presence check。

### Round 2

```yaml
round: 2
phase: converge
input_residual: revised boundary drift prevention plan
```

#### Findings

| id | severity | class | summary | evidence | status |
|---|---|---|---|---|---|
| F-008 | high | invalidity | forbidden-term scan 会命中 `ui-product-harness/references/interface-trace-dsl.md` 的 `Channel` 正向示例，但计划未覆盖该文件。 | A1/A3 converge；现有 DSL 示例含 `open the Channel workspace` 和 `channel-message`。 | merged |
| F-009 | medium | ambiguity | new eval presence check 用文案正则，大小写、连字符和词形都可能与实施后的 eval 不匹配。 | A1/A3/A4 converge；W6 使用 `InterfaceCapability` / `HarnessScenario`，Verification 使用 lowercase hyphen regex。 | merged |

#### Counter Proposals

| id | summary | why_better | overturns_assumptions | resolves_findings | supersedes_proposals | dominance | axis_scores | status |
|---|---|---|---|---|---|---|---|---|
| CP-005 | 把 `interface-trace-dsl.md` 纳入 W8，替换 Fermi-specific positive example。 | targeted scan 将变成真实边界门，而不是已知 false positive。 | A-006 | F-008 | none | dominates | concept-count:0; public-surface:+1; compat-budget:+1; migration-cost:0; proof-strength:+1; future-headroom:+1 | adopted |
| CP-006 | 给两个新增 eval 固定稳定 id，并用 id presence check。 | 比自然语言正则更稳定，避免 implementation-ready 计划自带假阴性。 | A-007 | F-009 | regex prompt presence check | dominates | concept-count:0; public-surface:0; compat-budget:+1; migration-cost:0; proof-strength:+1; future-headroom:+1 | adopted |

#### Resolution Delta

- Proposal 新增 W8，要求将 `interface-trace-dsl.md` 的 `Channel` / `channel-message`
  正向示例改成 repo-neutral 示例。
- W6 新增稳定 eval id：
  `interface-capability-splits-proof-implementation` 和
  `harness-scenario-does-not-rewrite-interface-capability`。
- Verification 的 new eval presence check 改为查固定 id。

## Adoption

adopted_candidate: Boundary Drift Prevention Patch + Companion Handoff Packet + Claim-to-minimum-proof Matrix + Eval Delta Only

lineage:

- CP-001
- CP-002
- CP-003
- CP-004
- CP-005
- CP-006

rejected_alternatives:

- initial four-layer upgrade
- Product Harness-owned companion promotion verdict
- broad eval expansion
- coarse paired headless rule

rejection_reason:

- 它们增加公共概念、制造第二 owner、重复已有 eval，或不能按 claim 类型约束 proof strength。

dominance_verdict:

- adopted candidate 在 concept-count、public-surface、compat-budget、migration-cost 和
  future-headroom 上支配初稿；在 proof-strength 上不弱于初稿，并因 targeted checks 更强。

### Freeze Record

adopted_summary:

```text
把本轮实现收敛为最小 boundary drift prevention：在 Product Harness trace contract 建
canonical boundary；在 InterfaceCapability 加 proof implementation split stop rule；在
claim ceilings/UI ladder 加 claim-to-minimum-proof；Goal companion 只做 handoff，不定义
promotion verdict；eval 只补两个缺口；正向示例必须 repo-neutral，不能携带 Fermi 产品对象。
```

kernel_verdict:

```text
Ramanujan: adopted candidate 压缩概念，不新增四层 doctrine。
Kolmogorov: stop rule 绑定 targeted checks，而不是泛化文档扩写。
Godel: adopted candidate 消除 Product Harness vs Goal Proof/docs-governance 的第二 authority。
```

frozen_decisions:

- 不新增 skill。
- 不新增第二套 harness vocabulary。
- 不使用 `ProductHarness` 作为新对象层；继续使用 `Product Harness System`、`HarnessScenario`、`Harness Coverage Matrix`。
- `InterfaceCapability` 拥有 user intent / work item / entrypoint / interaction / state ownership / coverage intent。
- `HarnessScenario` 拥有 covers refs / fixtures refs / surfaces refs / evidence refs / claim_ceiling / not_claimed / not_proven / gaps。
- `coverage_intent` 只是非权威请求或 gap seed，不是 coverage status。
- UI/browser proof 不自动证明 product fact。
- Headless proof 不自动证明 UI 可达、可见、可恢复或 reload 一致。
- Goal Pack companion promotion / retention verdict 归 `$goal-proof` / `$docs-governance`。

non_goals:

- 不上浮 Fermi `Channel`、`Work Unit`、`Agent Run`、`Result`、`Needs me`。
- 不实现具体 runner、Playwright、fixture、harness command 或 Goal Pack。
- 不改 root README，除非 entrypoint audit 发现公开路由变化。

allowed_reopen_surface:

- 发现 adopted plan 仍让 Product Harness 拥有 Goal/docs lifecycle。
- 发现 adopted plan 仍让 InterfaceCapability 拥有 claim_ceiling 或 evidence completion。
- 发现 targeted scan 不能识别 Fermi object 上浮或第二 vocabulary。
- 发现有更小方案能保持 proof-strength 不降并严格降低 public-surface。

proof_obligations:

- `bun run check`
- `python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .`
- `git diff --check`
- eval JSON parse for changed eval files
- forbidden-term scan for Fermi product object names
- forbidden vocabulary scan for second harness vocabulary
- new eval id presence check

delta_from_previous_round:

- Round 1 合并初稿所有 high blocker。
- Round 2 合并 targeted scan false-positive blocker 和 eval presence false-negative blocker。
- Final converge：A1/A2/A3/A4 均返回 `no unresolved findings`。

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
  - skills 当前没有统一 eval runner；本计划用 JSON parse、presence check 和 repo check 作为实施期最低验证。
  - coverage_intent.required_levels 字段名仍可能误读；实施时优先降级为 coverage_intent / harness_needs.claim_intent 的非权威请求。
```
