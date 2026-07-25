# Product Capability Coverage Skill Proposal

## Status

```yaml
status: reviewed-implementation-plan
created_at: 2026-06-03
review_ledger: ../../review-plan/runs/2026-06-03-product-capability-coverage-axis-rearchitecture-review.md
source_kind: method-upgrade-proposal
target_skill:
  - product-capability-coverage
  - ai-coding-os
  - product-harness-system
  - ui-product-harness
  - headless-product-harness
  - interface-capability-planning
target_layers:
  - skills/capability/product-capability-coverage/SKILL.md
  - skills/capability/product-capability-coverage/evals/evals.json
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
  - docs/goal-proof/README.md
not_authority: true
source_standalone_semantics: true
downstream_distribution_claimed: false
```

本文件是已评审的实施计划，不是当前 skill 行为或 SSoT authority。若采纳实施，
应创建 Goal Pack 或执行计划，再修改 skill、eval、router、README 和 docs。

## Reviewed Target Function

本轮采用新目标函数：

```text
产品能力 / 用户行为 / bug / workflow
  -> claim slices
  -> risk axes
  -> proof home recommendation
  -> e2e sentinel rationale
  -> regression sink handoff
  -> not_claimed / gaps
```

这是一项可独立使用的 agent skill 能力，不只是 AI Coding OS 内部 harness
路由分支。第一波应新增薄 `product-capability-coverage` skill，并定义
standalone 最小语义；AI Coding OS suite integration 是可选映射。

采用：

```text
Standalone Product Capability Coverage Core + Optional AI Coding OS Integrations
```

## Why A Separate Skill

独立 skill 成立，因为它处理的是 pre-owner decomposition：

- 用户给的是产品能力、用户行为矩阵、bug、workflow 或验收疑问。
- 目标不是立刻设计 Harness artifact，也不是立刻写 UI/headless proof。
- 第一动作是拆 claim slices、识别 risk axes、建议 proof home、决定 e2e sentinel
  是否只是跨层接缝、并给 root regression sink。

把这件事放进 `product-harness-system` 会让 Harness artifact owner 吞掉前置产品能力
拆解；放进 `ai-coding-os` router 又不能 standalone；放进 UI/headless 任一 owner 会
提前偏向某种 proof surface。

## Name Boundary

公开触发名采用用户目标语义：

```text
product-capability-coverage
```

这里的 `coverage` 只表示 route-time claim/risk coverage analysis，不表示：

- Harness Coverage Matrix。
- coverage status。
- test coverage percentage。
- durable coverage artifact。
- proof completion state。

不得新增 `Coverage Map`、`coverage_map`、`coverage status`、新的 proof-level enum、
Goal Pack schema 字段或 CLI checker 行为。

## Core Axioms

1. Claim slice is not proof.
   A slice names what might need proof; it does not decide final proof authority.
2. User behavior is risk discovery, not an e2e list.
   Blank input, duplicate submit, reload, backfill, retry, concurrency, and
   realtime gaps reveal risk axes; they do not automatically become browser e2e.
3. Lowest honest proof home first.
   Prefer the owner closest to the fact, state, contract, projection, UI
   consumption, runtime composition, or release seam being claimed.
4. E2E is a seam sentinel.
   Keep e2e / browser / production-near only for cross-layer composition that
   lower owners cannot observe honestly.
5. E2E bug must sink root regression.
   A visible failure should produce a lower-level regression sink when root
   cause is localizable; if not, record a gap.
6. Handoff is not final authority.
   This skill recommends proof homes and requests; receiving owners freeze final
   placement, claim ceiling, proof ladder, runner, evidence, and lifecycle.

## Standalone Contract

### Owns

- Product capability claim slicing.
- User behavior / bug / workflow risk-axis discovery.
- Generic proof-home recommendation.
- E2E / production-near sentinel rationale.
- Root regression sink recommendation.
- Inline handoff note / response contract.
- `not_claimed` and `gaps` for unproven adjacent surfaces.

### Does Not Own

- Product truth, domain authority, API schema, DB state, or design authority.
- Test runner implementation, Playwright scripts, command surfaces, fixtures,
  replay files, or concrete test code.
- Final proof placement, claim ceiling, evidence record, lifecycle, or coverage
  status.
- Harness Coverage Matrix or any Harness artifact.
- Goal Pack state, schema, evidence records, or completion review.
- UI/headless proof ladder ownership.

### Generic Vocabulary

Use standalone terms by default:

```text
capability
user_job
workflow_step
bug_or_failure_mode
claim_slice
risk_axis
proof_home
proof_request
e2e_sentinel
regression_sink
handoff
not_claimed
gaps
```

Generic proof homes:

```text
product_owner
domain_owner
api_or_contract_owner
service_owner
data_owner
projection_owner
ui_owner
runtime_owner
release_owner
human_acceptance
```

AI Coding OS skill names appear only under optional integrations, not in the
standalone output.

## Output Shape

Output is an inline answer / handoff note, not a durable artifact. It must not
include stable IDs, lifecycle state, promotion status, evidence refs, or matrix
cell status.

Recommended shape:

```text
capability:
user_job:
claim_slices:
  - slice:
    risk_axes:
    proof_home:
    proof_request:
    e2e_sentinel:
    regression_sink:
    handoff:
not_claimed:
gaps:
optional_integrations:
  ai_coding_os:
```

Handoff sentence template:

```text
Put `<slice>` under `<proof_home>` because `<risk_axis>`.
Minimum proof request: `<proof_request>`.
Keep e2e sentinel only for `<seam_reason>`.
Sink regression to `<regression_sink>` if the failure localizes there.
Not claimed: `<not_claimed>`.
Gap: `<gap>`.
```

## Optional AI Coding OS Integrations

When the full AI Coding OS suite is available, map generic proof homes to owner
skills:

```text
user-facing capability semantics -> interface-capability-planning
durable HarnessScenario / claim_ceiling / Harness Coverage Matrix -> product-harness-system
UI render / browser-visible / production-near path -> ui-product-harness
headless command / fixture / replay / DB-backed proof -> headless-product-harness
multi-record execution / evidence / completion review -> goal-proof
docs placement / promotion / demotion -> docs-governance
architecture authority ambiguity -> agentic-architecture
```

`ai-coding-os` routes ordinary “怎么测 / regression 放哪层 / e2e 是否保留 /
用户行为矩阵怎么下沉” requests to `product-capability-coverage` first, unless the
user explicitly selects a more specific owner skill.

## Implementation Waves

### Wave 1: Standalone Skill Source

Allowed scope:

- `skills/capability/product-capability-coverage/SKILL.md`
- `skills/capability/product-capability-coverage/evals/evals.json`
- `skills/router/ai-coding-os/SKILL.md`
- `skills/harness/product-harness-system/SKILL.md`
- `skills/harness/ui-product-harness/SKILL.md`
- `skills/harness/headless-product-harness/SKILL.md`
- `skills/capability/interface-capability-planning/SKILL.md`
- `skills/README.md`
- `docs/README.md`
- `docs/product/README.md`
- `docs/ssot/README.md`
- `docs/standards/skill-source-layout.md`
- `README.md`
- `README.zh-CN.md`
- `docs/goal-proof/README.md`
- this source file and review ledger

Tasks:

1. Add `skills/capability/product-capability-coverage/SKILL.md`.
2. Frontmatter description must say this is standalone product capability
   coverage analysis for feature / bug / workflow / behavior-matrix testing
   placement.
3. Add the standalone contract, core axioms, generic vocabulary, output shape,
   handoff template, `does_not_own`, and optional AI Coding OS integrations.
4. Update `ai-coding-os` router so coverage / testing / regression placement /
   e2e sentinel / user behavior matrix asks route to `product-capability-coverage`.
5. Update product harness, UI harness, headless harness, and interface capability
   skills only as consumers of handoff. They do not lose final authority.
6. Update `skills/README.md`, root README, README.zh-CN, `docs/README.md`,
   `docs/product/README.md`, `docs/ssot/README.md`, and
   `docs/standards/skill-source-layout.md` in the same wave because this changes
   the public skill suite.
7. Add minimum evals to `skills/capability/product-capability-coverage/evals/evals.json`.

Do not add `skills/coverage/` in Wave 1. The existing `capability/` group is
acceptable because this is product capability decomposition, not a new artifact
family. A future source-layout review may move task-axis skills later.

### Wave 2: Optional Layout Reclassification

Only if future evidence shows `capability/` becomes overloaded:

- Review whether `product-capability-coverage` and
  `interface-capability-planning` should remain in `capability/`, or whether a
  new `coverage/` / `interface/` grouping is worth the public layout churn.
- This requires a separate skill-source-layout review and same-wave README /
  SSoT / standards updates.

## Minimum Evals

Eval ids:

- `product-capability-coverage-feature-behavior-matrix`
- `product-capability-coverage-bug-regression-sink`
- `product-capability-coverage-headless-not-browser-claim`
- `product-capability-coverage-e2e-sentinel-only-seam`
- `product-capability-coverage-standalone-no-os-taxonomy`
- `product-capability-coverage-not-harness-matrix`

Behavior expectations:

- Feature/user behavior matrix decomposes into multiple claim slices and proof
  homes; it does not become a full e2e suite.
- Bug report includes failure mode, likely root regression sink, e2e sentinel
  rationale, and gap if root cannot be localized.
- Headless proof request does not claim browser-visible path.
- UI/browser proof request does not claim product fact unless paired with product
  owner proof.
- Standalone output does not require AI Coding OS skill names.
- Output does not define Harness Coverage Matrix, coverage status, claim ceiling,
  evidence record, or lifecycle state.

## Acceptance Trace

Input:

```text
用户提交评论时可能空白、重复点击提交、第一条还在发送时发第二条、刷新后仍应看到正确状态。
```

Expected standalone output:

```text
capability: submit comment
user_job: publish one valid comment without duplicates or lost queued work
claim_slices:
  - slice: blank / whitespace input rejected
    risk_axes: input semantics, validation boundary
    proof_home: api_or_contract_owner + domain_owner
    proof_request: contract/domain validation
    e2e_sentinel: no
    regression_sink: validation rule near product/domain owner
  - slice: rapid duplicate submit does not create duplicates
    risk_axes: idempotency, UI mutation, service concurrency
    proof_home: service_owner, optionally ui_owner for disabled/pending state
    proof_request: service/application test plus UI state request if user-visible
    e2e_sentinel: no unless duplicate only appears through browser/runtime composition
    regression_sink: idempotency/application owner
  - slice: first active + second queued drains correctly
    risk_axes: queue, persistence, async lifecycle
    proof_home: service_owner + data_owner
    proof_request: application/storage test
    e2e_sentinel: only if reload/runtime composition is the claim
    regression_sink: queue/storage owner
not_claimed:
  - browser reload recovery unless browser/runtime sentinel is exercised
gaps:
  - external production reliability not proven
```

AI Coding OS optional integration may map:

```text
api_or_contract_owner -> headless-product-harness
domain_owner / service_owner / data_owner -> headless-product-harness or project tests
ui_owner -> ui-product-harness
durable matrix / claim_ceiling -> product-harness-system
multi-step evidence -> goal-proof
```

## Verification Plan

Required:

```bash
bun run check
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .
git diff --check
python3 -m json.tool skills/capability/product-capability-coverage/evals/evals.json >/dev/null
rg -n "product-capability-coverage" README.md README.zh-CN.md docs/README.md docs/product/README.md docs/ssot/README.md docs/standards/skill-source-layout.md skills/README.md skills/router/ai-coding-os/SKILL.md
rg -n "product-capability-coverage-feature-behavior-matrix|product-capability-coverage-bug-regression-sink|product-capability-coverage-headless-not-browser-claim|product-capability-coverage-e2e-sentinel-only-seam|product-capability-coverage-standalone-no-os-taxonomy|product-capability-coverage-not-harness-matrix" skills/capability/product-capability-coverage/evals/evals.json
```

Boundary checks:

```bash
test ! -d skills/coverage
! rg -n "Coverage Map|coverage_map|coverage status|new proof-level enum" skills/capability/product-capability-coverage skills/router skills/harness docs/ssot docs/product README.md README.zh-CN.md
git diff -- packages/cli/src packages/cli/test
```

Allowed negative / historical mentions of rejected terms may appear only in this
source, review ledger, historical evidence, or eval negative examples.

## Non-Goals

- No CLI / Goal Pack schema / checker behavior change.
- No Harness Coverage Matrix replacement or second Harness artifact.
- No product truth ownership.
- No test runner, Playwright script, command, fixture, replay, or concrete test
  implementation ownership.
- No UI/headless proof ladder ownership.
- No Goal Pack evidence or completion review ownership.
- No downstream runtime installed-state claim.
- No `coverage/` group in Wave 1.

## Frozen Decisions

- Wave 1 adds a standalone `product-capability-coverage` skill.
- The skill lives under `skills/capability/` in Wave 1.
- `source_standalone_semantics: true`.
- `downstream_distribution_claimed: false`.
- Default output uses generic proof homes, not AI Coding OS skill names.
- AI Coding OS owner skills are optional integrations.
- Handoff is recommendation, not final authority.
- `coverage` in the skill name means route-time claim/risk coverage analysis, not
  Harness Coverage Matrix or coverage status.
- Public README / docs / SSoT / skill-source-layout must update in the same wave.

## Ready-To-Implement Summary

First implementation Goal Pack should claim:

```text
repo-local source update for standalone product-capability-coverage skill,
router integration, optional suite handoffs, public docs sync, and eval coverage
```

It must not claim:

```text
downstream runtime installation
new CLI/schema/checker behavior
new Harness artifact or Matrix
product truth or test runner implementation
```
