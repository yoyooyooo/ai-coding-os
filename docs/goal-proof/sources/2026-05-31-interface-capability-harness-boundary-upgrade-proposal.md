# Interface Capability And Harness Boundary Drift Prevention Plan

## Status

```yaml
status: adopted-implementation-plan
created_at: 2026-05-31
source_kind: implementation-plan
source_context:
  - Fermi docs/interface-capabilities/README.md
  - Fermi docs/product-harness/README.md
  - handoff_source: /var/folders/sf/rnr3jjbn3qb0c43yyjl3p9900000gn/T/handoff-XXXXXX.md.PkRaVlG4HX
review_goal: implementation-ready
review_ledger: docs/review-plan/runs/2026-05-31-interface-capability-harness-boundary-upgrade-review.md
target_project: ai-coding-os
target_claim: >
  用最小边界补强防止 InterfaceCapability、Product Harness、UI proof 和
  headless product proof 互相越权；不新增 skill，不引入第二套 harness vocabulary，
  不把 Fermi 产品对象上浮为 OS doctrine。
```

本文是 `$handoff` 生成、经 `$plan-optimality-loop` 打磨后的可实施计划。它不是
skill 修改的完成证据；实施完成仍需按本文 Verification 跑证据。

## Adopted Objective

本轮不做“四层 doctrine 升级”。AI Coding OS 已有相关 skill 与 shared Harness 词汇。
真正缺口是 boundary drift：

```text
InterfaceCapability 内嵌 HarnessScenario / fixture / Playwright body
  -> interface contract 变成 proof implementation

HarnessScenario 改写 user intent / entrypoint / product semantics
  -> proof contract 反向定义 capability

browser_visible 通过
  -> 被误报成 persistence / accepted business fact / production readiness

Goal Pack companion promotion verdict 放进 Product Harness
  -> harness skill 越权定义 Goal/docs lifecycle
```

采用模型：

```text
InterfaceCapability = user-facing intent contract
Product Harness System = shared proof contract, claim_ceiling, evidence refs, gaps
UI Product Harness = UI proof route
Headless Product Harness = product-authority proof route
```

`UI Product Harness` 和 `Headless Product Harness` 是 proof route，不是新的公共
authority 层。官方词汇继续使用 `HarnessScenario`、`Harness Coverage Matrix`、
`claim_ceiling`、`not_claimed`、`not_proven` 和 `gaps`。

## Source Findings From Fermi

Fermi 只提供素材，不提供 OS authority：

- `InterfaceCapability` 拥有用户任务、入口、交互合同、状态 / 数据归属和
  coverage intent；不拥有 HarnessScenario、fixture、Playwright 步骤、产品事实或
  Goal Pack 状态。
- `Product Harness` 拥有 HarnessScenario、fixture refs、surface refs、
  evidence refs、claim ceiling、negative claims、not_proven、coverage matrix 和
  lifecycle；不拥有 InterfaceCapability 语义、产品事实、测试代码或 Goal Pack
  evidence 原文。

不能上浮到 OS doctrine 的 Fermi 对象名：

```text
Channel
Work Unit
Agent Run
Result
Needs me
```

## Implementation Plan

### W1: 建一个 canonical boundary patch

目标文件：

```text
skills/harness/product-harness-system/references/trace-contract.md
```

新增短节 `Capability And Harness Boundary`，作为本轮唯一 canonical boundary 表。
其他文件只 cross-reference 或补 local stop rule，避免四处复制同一规则。

必须表达：

```text
InterfaceCapability owns:
  user intent
  user work item
  entrypoint / affordance
  interaction states
  frontend state/data ownership
  coverage_intent / harness_needs as non-authoritative request

HarnessScenario owns:
  covers refs
  fixtures refs
  surfaces refs
  evidence refs
  claim_ceiling
  not_claimed
  not_proven
  remaining_gaps

HarnessScenario must not:
  rewrite user intent
  rewrite entrypoint
  rewrite InterfaceCapability semantics
  turn fixture/browser evidence into product truth
```

`coverage_intent.required_levels` 如果保留，只能表示期望覆盖和 gap seed；它不是
coverage status，不推出完成，也不能覆盖 `HarnessScenario.claim_ceiling`。

### W2: 给 InterfaceCapability 加 local stop rule

目标文件：

```text
skills/capability/interface-capability-planning/references/planning-workflow.md
```

新增或收紧 `Capability vs Harness Boundary`：

- `InterfaceCapability` 可以引用 `hs.*`、`uh.*`、`hp.*` 等 proof refs。
- `InterfaceCapability` 可以声明 `coverage_intent` / `harness_needs.claim_intent`。
- `InterfaceCapability` 不能内嵌完整 HarnessScenario、fixture body、mock handler、
  Playwright steps、browser command、evidence body 或 product fact。
- 用户输入混入 proof implementation 时，agent 必须拆成 harness refs / gaps /
  handoff notes，不在 capability contract 内吸收。

如果该变更改变 `SKILL.md` 用户可见 ownership / stop / routing，则最小同步
`skills/capability/interface-capability-planning/SKILL.md`。否则不改 README。

### W3: 收紧 Product Harness 反向改写规则

目标文件：

```text
skills/harness/product-harness-system/references/trace-contract.md
```

在 W1 canonical 表旁补明确规则：

- `HarnessScenario.covers.interface_capability` 只能引用 `ic.*`。
- Harness 可以降低或限制自己的 `claim_ceiling`。
- Harness 可以记录 `not_claimed`、`not_proven`、`remaining_gaps`。
- Harness 不能修改 user intent、entrypoint、accepted product semantics。
- 如果 capability contract 缺失或不可信，handoff 给
  `$interface-capability-planning`，不要在 HarnessScenario 里补写语义。

### W4: 用 claim-to-minimum-proof 替代粗粒度 paired rule

目标文件：

```text
skills/harness/product-harness-system/references/claim-ceilings.md
skills/harness/ui-product-harness/references/harness-ladder.md
```

不要新增“有 headless ref 就能声明 business fact”的粗规则。改为矩阵：

| Desired claim | Minimum honest proof |
|---|---|
| browser path is visible / reachable | `browser_visible` |
| frontend state/cache/router/realtime/view-model behavior | `interface_headless` |
| render controls, pending/error/success wiring | `render_wiring` |
| projection fact consumed by UI | paired `browser_visible` plus headless `projection` or stronger |
| persistence / DB-backed fact | headless `db_backed` or stronger |
| runtime side effect / external runtime fact | headless `real_runtime_opt_in` and explicit opt-in evidence |
| local/staged production-near UI path | `production_near` plus required backend/runtime/auth/profile evidence |

UI/browser proof never upgrades to product fact by itself。Headless proof 也不证明 UI
已经可达、可见、可恢复或 reload 一致。

### W5: Goal Pack companion 只做 owner-preserving handoff

目标文件：

```text
skills/harness/product-harness-system/references/lifecycle-and-placement.md
```

只补短指针，不定义 retention verdict owner。

允许描述：

```text
Goal Pack product-harness.yaml may hold candidate HarnessScenario / coverage refs.
Promotion or retention verdict belongs to goal-proof and docs-governance.
Product Harness may output a handoff packet.
```

handoff packet shape：

```text
companion_path
capability_ids
harness_ids
evidence_refs
claim_ceiling
not_claimed
not_proven
gaps
promotion_question
owner_skill
```

禁止新增这些由 Product Harness 拥有的 verdict：

```text
promote | keep-in-goal | split | retire | block
```

Goal companion rules 的主 owner 仍是：

```text
skills/goal/goal-proof-system/references/artifact-routing.md
skills/governance/docs-governance/**
```

### W6: Eval delta only

不要重复已有 eval：

- `product-harness-system/evals/evals.json` 已覆盖 screenshot / fixture overclaim。
- `ui-product-harness/evals/evals.json` 已覆盖 Playwright pass without headless proof。

新增最小缺口：

```text
skills/capability/interface-capability-planning/evals/evals.json
```

新增 eval：

- id：`interface-capability-splits-proof-implementation`
- prompt：InterfaceCapability artifact 内嵌 Playwright steps、fixture body、mock
  handler 和 evidence body。
- expected：拆成 InterfaceCapability refs / coverage_intent / harness handoff gaps；
  不把 proof implementation 留在 capability contract。

```text
skills/harness/product-harness-system/evals/evals.json
```

新增 eval：

- id：`harness-scenario-does-not-rewrite-interface-capability`
- prompt：HarnessScenario 通过 `covers` 指向一个 InterfaceCapability，但又改写
  user intent、entrypoint 和 accepted product semantics。
- expected：拒绝改写；保留 `covers`；只调整 `claim_ceiling`、`not_claimed`、
  `not_proven` 和 gaps；必要时 handoff 到 InterfaceCapability owner。

可选强化：

- 若 W4 改动使现有 UI eval #3 expected_output 不够精确，只收紧该条输出；
  不新增重复 eval。
- 若 W4 改动使 Product Harness eval #2 不够精确，只收紧该条输出；
  不新增重复 eval。

### W7: Entrypoint audit

检查这些入口是否需要最小同步：

```text
skills/capability/interface-capability-planning/SKILL.md
skills/harness/product-harness-system/SKILL.md
skills/harness/ui-product-harness/SKILL.md
skills/harness/headless-product-harness/SKILL.md
```

规则：

- 若 reference 变更改变用户可见 routing、stop、ownership，必须同步对应 `SKILL.md`。
- 若只是 reference 内部例子或 eval 补强，不改 README。
- root README / `skills/README.md` 只有在跨 skill 导航变更时更新；本计划默认不需要。

### W8: Neutralize Fermi-specific positive examples

目标文件：

```text
skills/harness/ui-product-harness/references/interface-trace-dsl.md
```

该文件现有正向 DSL 示例包含 Fermi-ish vocabulary，例如 `Channel` / `channel-message`。
实施时必须把这些示例改成 repo-neutral domain，或明确标为 forbidden example。优先选
repo-neutral rewrite，避免 targeted scan 把正向示例误判为 OS doctrine 泄漏。

建议替换方向：

```text
ic.issue-intake.from-channel-message -> ic.task-intake.from-source-note
hp.channel-message.seeded -> hp.source-note.seeded
open the Channel workspace -> open the task intake workspace
```

不要把 `Channel`、`Work Unit`、`Agent Run`、`Result`、`Needs me` 留在正向示例里。

## Non-goals

- 不新增 skill。
- 不新增第二套 harness vocabulary。
- 不新增 schema-breaking required field。
- 不把 Fermi `Channel`、`Work Unit`、`Agent Run`、`Result`、`Needs me` 上浮为
  OS doctrine。
- 不实现具体 test runner、Playwright、fixture、harness command 或 Goal Pack。
- 不让 Product Harness 拥有 Goal Pack completion review、retention verdict 或 docs
  layer authority。
- 不让 InterfaceCapability 拥有 `claim_ceiling` 或 evidence completion status。

## Verification

在 AI Coding OS 仓根目录运行：

```bash
cd /Users/yoyo/Documents/code/personal/ai-coding-os
bun run check
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .
git diff --check
```

再跑 targeted checks，证明本计划的边界 claim：

```bash
python3 -m json.tool skills/harness/product-harness-system/evals/evals.json >/dev/null
python3 -m json.tool skills/harness/ui-product-harness/evals/evals.json >/dev/null
python3 -m json.tool skills/capability/interface-capability-planning/evals/evals.json >/dev/null
rg -n "Channel|Work Unit|Agent Run|Result|Needs me" \
  skills/capability/interface-capability-planning \
  skills/harness/product-harness-system \
  skills/harness/ui-product-harness \
  skills/harness/headless-product-harness
rg -n "ProductHarness|UI Harness layer|Headless Harness layer|four distinct layers|四层" \
  skills/capability/interface-capability-planning \
  skills/harness/product-harness-system \
  skills/harness/ui-product-harness \
  skills/harness/headless-product-harness
rg -n "interface-capability-splits-proof-implementation|harness-scenario-does-not-rewrite-interface-capability" \
  skills/capability/interface-capability-planning/evals/evals.json \
  skills/harness/product-harness-system/evals/evals.json
```

说明：

- 前两个 `rg` 命令期望无输出；若输出来自明确的 forbidden example 或 negative eval，
  closeout 必须说明为什么不构成 doctrine 泄漏。
- 最后一个 `rg` 命令期望能命中新 eval id，用于确认新增缺口已落盘。

## Implementation Order

1. 先改 `trace-contract.md`，建立 canonical boundary patch。
2. 再改 `planning-workflow.md`，把 capability contract 内的 proof implementation
   明确拆出。
3. 再改 `claim-ceilings.md` 与 `harness-ladder.md`，补 claim-to-minimum-proof。
4. 再改 `lifecycle-and-placement.md`，补 owner-preserving companion handoff。
5. 再改 `interface-trace-dsl.md`，把 Fermi-specific positive example 换成中性示例。
6. 最后补 eval delta 与 entrypoint audit。
7. 跑 Verification，按输出修正。

## Residual Risk

- 现有 skills 没有统一 eval runner；本计划只能要求 JSON parse、presence check 和 repo
  `bun run check`。如果后续需要量化 skill behavior，应另开 eval runner 工作项。
- `coverage_intent.required_levels` 这个字段名仍可能被误读；实施时优先改写为
  `coverage_intent` / `harness_needs.claim_intent` 的非权威请求口径。
