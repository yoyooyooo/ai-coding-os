# Product Capability Coverage Axis Proposal

## 状态

```yaml
status: frozen-implementation-candidate
created_at: 2026-06-03
source_kind: method-upgrade-proposal
target_skill:
  - ai-coding-os
  - product-capability-coverage
  - product-harness-system
  - ui-product-harness
  - headless-product-harness
  - interface-capability-planning
target_layers:
  - skills/router/ai-coding-os/SKILL.md
  - skills/coverage/product-capability-coverage/SKILL.md
  - skills/README.md
  - skills/harness/product-harness-system/SKILL.md
  - skills/harness/ui-product-harness/SKILL.md
  - skills/harness/headless-product-harness/SKILL.md
  - skills/capability/interface-capability-planning/SKILL.md
  - docs/product-harness/README.md
  - docs/ssot/README.md
not_authority: true
```

本文件冻结“能力覆盖轴”升级方案。它不是当前 skill 行为、目录结构或公开口径 authority。
若采纳，应先转成 Goal Pack 或实施计划，再修改 skill / README / docs。

## 背景

当前 AI Coding OS 已有完整的 artifact owner 分层：

- `product-harness-system`：Harness artifact、`claim_ceiling`、Harness Coverage Matrix、生命周期。
- `ui-product-harness`：interface-headless、render wiring、browser-visible、production-near UI proof。
- `headless-product-harness`：proof command、smoke、fixture / replay、DB-backed、real runtime opt-in。
- `interface-capability-planning`：InterfaceCapability、surface、状态 / 数据归属、testability handoff。

这些 skill 互补，但用户常问的是另一类任务：

```text
这个产品功能怎么测？
这个 bug 修复后 regression 放哪层？
用户行为矩阵怎么下沉成测试？
哪些 e2e 需要保留，哪些应该下沉？
headless product proof 和 UI proof 怎么组合？
```

这类问题横跨 product、domain、API、storage、realtime、UI、runtime 和 release。
把它塞进任意现有 harness skill，都会让 artifact owner 变成策略入口。

## Adopted Candidate

采用：

```text
Product Capability Coverage Axis
```

新增独立 skill：

```text
product-capability-coverage
```

定位：

```text
用户给一个产品功能、bug、workflow、用户行为矩阵或 headless capability
  -> 拆 claim slices
  -> 识别 claim-bearing axes
  -> 找 owner layer
  -> 选择 lowest honest proof level
  -> 决定 regression placement
  -> 只在无法下沉的跨层接缝保留 e2e / production-near sentinel
```

## Core Doctrine

### 1. 用户行为是发现维度，不是 e2e 列表

用户行为用于暴露风险轴：

- 空白、trim、格式、unicode、多行、长文本。
- 重复提交、快速点击、并发、idempotency。
- 切换对象、stale projection、reload、backfill。
- 网络失败、重试、离线、WS gap、stream close。
- runtime busy、queue、drain、restart、migration。

这些行为不自动变成 browser e2e。每一项先下沉到最小可证明层。

### 2. Headless product 不是绕开 UI

Headless product proof 优先证明产品事实、projection、persistence、runtime seam。
它不能声明用户可见路径成功；UI proof 也不能单独声明 domain fact 完成。

### 3. 每个 claim slice 找最低诚实证明层

默认 proof placement：

| Axis | Preferred owner / proof |
| --- | --- |
| input / intent semantics | interface-headless 或 render wiring |
| command shape | client / transport contract test |
| public schema / DTO | contract guard / schema sync test |
| domain fact | domain / application test |
| idempotency / concurrency | application / storage seam test |
| persistence / restart / migration | DB-backed smoke |
| projection / read model | projection test / API smoke |
| realtime / async lifecycle | reducer、stream kernel、backfill test |
| visible UI state | render wiring / browser-visible |
| reload / navigation recovery | browser-visible |
| package / runtime / DB composition | production-near sentinel |
| external real runtime | real_runtime_opt_in only |

### 4. e2e 是接缝哨兵，不是覆盖主力

e2e / browser / production-near 只保留：

- 下层无法观察的跨层 composition。
- package / runtime / DB / browser / reload 的真实组合路径。
- 用户可见路径和 headless proof 之间的消费接缝。

每个高风险链路默认少量 sentinel；不得把所有用户排列组合推成 e2e suite。

### 5. e2e 发现 bug 后必须下沉 root regression

当 e2e 或手测发现问题：

```text
production-near failure
  -> root cause owner
  -> lower-level regression
  -> e2e sentinel 保留跨层接缝证明
```

如果 root cause 无法下沉，必须在 `not_proven` / gap 中写明原因。

## New Skill Contract

### Owns

- Product capability coverage decomposition.
- 用户行为 / headless capability 到 claim slices 的拆解。
- `Coverage Map` 轻量输出。
- test / proof placement 决策。
- e2e / production-near sentinel 选择。
- regression 下沉建议。
- gap audit for coverage.

### Does Not Own

- 产品事实、domain authority、API schema。
- 具体测试代码、runner、Playwright 脚本、xtask 命令实现。
- Harness artifact 生命周期、Harness Coverage Matrix。
- Goal Pack state、evidence record、completion review。
- UI/IA 最终语义或 InterfaceCapability authority。

### Handoff

```text
coverage strategy / test placement -> product-capability-coverage
HarnessScenario / claim_ceiling / Matrix lifecycle -> product-harness-system
UI proof design / render / browser-visible -> ui-product-harness
headless command / smoke / fixture / replay -> headless-product-harness
InterfaceCapability semantics -> interface-capability-planning
multi-turn evidence execution -> goal-proof
architecture authority ambiguity -> agentic-architecture
docs placement / promotion -> docs-governance
```

## Output Shape

`product-capability-coverage` 默认输出轻量 `Coverage Map`，不是 durable Harness Matrix。

```text
capability:
entrypoints:
claim_slices:
risk_axes:
coverage_map:
  - slice:
    owner_layer:
    proof_level:
    test_placement:
    existing_coverage:
    gap:
    promotion_gate:
e2e_sentinels:
root_regressions_to_sink:
not_claimed:
next_tests:
```

字段含义：

- `Coverage Map`：一次任务的轻量覆盖决策，可直接用于实现或 review。
- `Harness Coverage Matrix`：长期 proof contract，仍归 `product-harness-system`。
- `promotion_gate`：什么时候从轻量 map promote 到 durable HarnessScenario / Matrix。

## Single-Skill Mode

该 skill 必须可单独安装和使用。项目没有完整 OS suite 时，它仍能输出：

```text
capability
claim_slices
owner_layer
proof_level
test_placement
e2e_sentinel
gaps
```

在完整 AI Coding OS suite 中，它作为 coverage axis router，按需要转交到
UI / headless / harness / interface / goal skills。

## Group Structure

推荐从当前 artifact-owner 目录升级为 task-axis + owner-skill 并存结构：

```text
router/
  ai-coding-os

goal/
  goal-proof
  goal-contracts
  finding-proof-step
  proof-step-implementation
  write-work-plans

coverage/
  product-capability-coverage

architecture/
  agentic-architecture
  frontend-architecture
  effect-best-practices

interface/
  interface-capability-planning

harness/
  product-harness-system
  ui-product-harness
  headless-product-harness

governance/
  docs-governance
```

第一波可以只新增 `skills/coverage/product-capability-coverage/SKILL.md`，
不立即迁移 `skills/capability/interface-capability-planning` 到 `skills/interface/`。
目录迁移应另设 migration gate，避免把新 skill 引入和大规模 layout churn 混在一起。

## Router Changes

`ai-coding-os` 应新增明确路由：

```text
用户问“怎么测 / 覆盖 / regression / e2e 是否需要 / 用户行为矩阵 / bug 测试落点”
  -> product-capability-coverage

用户问 Harness artifact / claim_ceiling / Harness Coverage Matrix / lifecycle
  -> product-harness-system
```

`product-harness-system` 需要降权澄清：它不再作为普通“功能怎么测”的入口。
它只拥有 durable harness artifact、matrix、trace、promotion / retirement。

## Acceptance Trace

输入：

```text
Channel message 输入：用户可能空白、重复提交、第一条 active 时发第二条、刷新后仍 working。
```

Expected Coverage Map：

```text
blank / whitespace content
  owner_layer: transport + application
  proof_level: contract/application test
  e2e_sentinel: false

rapid duplicate submit
  owner_layer: UI mutation/store/render
  proof_level: interface_headless + render_wiring
  e2e_sentinel: false

first active + second queued + drain
  owner_layer: application/storage seam
  proof_level: application + DB-backed
  e2e_sentinel: only package/PGlite/reload seam

package tgz + PGlite statement-by-statement + browser reload
  owner_layer: production-near composition
  proof_level: production_near
  e2e_sentinel: true, one bounded sentinel
```

## Implementation Waves

### Wave 1: 新 skill 和 router 口径

- 新增 `skills/coverage/product-capability-coverage/SKILL.md`。
- 更新 `skills/README.md` group 表。
- 更新 `skills/router/ai-coding-os/SKILL.md` 路由。
- 更新 `docs/ssot/README.md` 方法事实。
- 不迁移现有目录。

### Wave 2: Harness skill handoff

- `product-harness-system` 增加“普通 coverage strategy 转交 coverage skill”。
- `ui-product-harness` 增加“coverage skill 决定是否进入 UI proof”。
- `headless-product-harness` 增加“coverage skill 决定是否需要 headless proof / smoke”。
- `interface-capability-planning` 增加“coverage intent 可被 coverage skill 消费”。

### Wave 3: Reference 和 eval

- 添加 coverage decomposition examples。
- 添加 evals：
  - 用户行为矩阵不生成全 e2e。
  - e2e bug 下沉 root regression。
  - headless capability 不声明 browser path。
  - Coverage Map 不等同 Harness Coverage Matrix。

### Wave 4: 可选目录迁移

- 将 `skills/capability/interface-capability-planning` 迁到 `skills/interface/`。
- 需要同步 skill layout docs、README、tests、sync scripts。
- 不作为 Wave 1 阻塞。

## Verification Plan

第一波验收：

```bash
bun run check
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .
git diff --check
```

静态核对：

```bash
rg "product-capability-coverage|Coverage Map|Harness Coverage Matrix" skills docs
rg "how to test|怎么测|coverage strategy" skills/router/ai-coding-os/SKILL.md
```

不得在第一波改变：

- Goal Proof CLI parser。
- Goal Pack schema。
- existing skill runtime trigger names。
- 已有 harness proof ladder 名称。

## Non-Goals

- 不合并 `product-harness-system`、`ui-product-harness` 和 `headless-product-harness`。
- 不把所有非 Goal Proof skill 收进一个 mega skill。
- 不新增第二套 Harness vocabulary。
- 不把 Coverage Map 升级成强制 artifact。
- 不要求所有项目使用 e2e。
- 不要求所有项目维护 durable Harness Coverage Matrix。
- 不替代 Goal Proof evidence / completion review。

## Frozen Decisions

- 新增独立 skill：`product-capability-coverage`。
- 新增 coverage axis，但不吞并现有 owner skills。
- `Coverage Map` 是轻量决策输出；`Harness Coverage Matrix` 仍归 `product-harness-system`。
- 用户行为驱动和 headless product 驱动统一进入 claim-slice / owner-layer / proof-level 拆解。
- e2e / production-near 是 bounded sentinel，不是默认覆盖主力。
- e2e 发现 bug 后必须尝试下沉 root regression。
- 第一波不做大规模目录迁移；先新增 skill 和路由口径。
- 后续可选将 `capability/` 改为 `interface/`，但必须独立迁移 gate。
