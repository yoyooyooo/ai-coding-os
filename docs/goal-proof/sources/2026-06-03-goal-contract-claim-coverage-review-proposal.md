# Goal Contract Claim Coverage Review Proposal

## 状态

```yaml
status: consumed-source
created_at: 2026-06-03
review_ledger: ../../review-plan/runs/2026-06-03-goal-contract-semantic-coverage-gate-proposal-review.md
promoted_to: ../goals/2026-06-03-triggered-claim-coverage-review/
source_kind: method-gap-proposal
target_skill:
  - goal-proof
  - goal-contracts
  - finding-proof-step
  - proof-step-implementation
target_layers:
  - skills/goal/goal-proof-system/SKILL.md
  - skills/goal/goal-proof-system/references/checker-rules.md
  - skills/goal/goal-proof-system/templates/evidence.jsonl
  - skills/goal/goal-contracts/**
  - skills/goal/finding-proof-step/**
  - skills/goal/proof-step-implementation/**
  - docs/goal-proof/README.md
not_authority: true
```

本文件已被消费为 Goal Pack source，不是当前 Goal Proof System 规则、schema、checker
或 skill 行为。当前执行状态以 `../goals/2026-06-03-triggered-claim-coverage-review/`
为准。

## 背景

Goal Proof System 已能约束 evidence record、work item 状态、allowed scope、
`next_action` 和 completion review 格式。但实际使用中仍有一种隐蔽 overclaim：

```text
objective 的自然语言暗示了更宽语义
  -> completion.required_evidence 只覆盖较窄子路径
  -> implementation 诚实地产生这些 evidence
  -> E999 completion review 按 token 映射通过
  -> 最终报告形式正确，但没有覆盖用户以为被证明的关键语义
```

这不是伪造 evidence，也不是跳过 proof step。缺口在于完成声明没有显式说明：

- 哪些 claim slice 被证明。
- 每个 slice 用的 proof level / proof mode。
- 哪些相邻语义被排除或仍是 gap。

## Adopted Candidate

采用：

```text
Triggered Claim Coverage Review
```

不采用：

- 新增 `goal.yaml` / `progress.yaml` 顶层 coverage 字段。
- 新增 proof modality 全局 enum。
- 让 CLI checker 理解 objective 自然语言。
- 用 required evidence token 名称编码完整证明语义。
- 改写 strong-agent ready gate 公式。

第一波只复用现有 v2 surface：

| 阶段 | 现有 surface | 承载内容 |
| --- | --- | --- |
| goal contract | `completion.required_evidence` | 按 claim-bearing slice 写可引用 required evidence |
| goal contract | `claim_limit` / `non_goals` / `constraints` | ready 前排除不声明的范围 |
| proof step | `progress.yaml.proof_step.target_delta` / `proof_path` / `checks` | 当前 slice、proof level、claim ceiling、失败检查 |
| implementation evidence | `claims` / `not_claimed` | 本轮实际证明和相邻未声明范围 |
| completion review | E999 `claim_evidence` / `not_claimed` / `remaining_gaps` | 最终 claim coverage review |

## Trigger Predicate

只有目标命中 semantic risk trigger 时，才强制做 claim coverage review。普通单步目标仍只要求
`claim_limit` 诚实。

触发条件：

- broad / multi-stage / multi-surface 目标。
- runtime proof level 混合：fixture、replay、adapter/projection、DB-backed、real runtime、browser-visible、production-near、manual acceptance。
- public surface、schema、protocol、CLI、template、README 或 skill 公开口径变化。
- authority action：accepted、approved、persisted、published、external side effect。
- product truth、quality judgment、ranking、retrieval、reasoning、recommendation 等被写入 completion claim。
- permission、private data、security、destructive 或 compliance boundary。
- completion 需要多条 evidence record 或跨 Goal Pack relation evidence。

## Claim-Bearing Axes

不要从 objective 抽取每个自然语言关键词。只审会影响完成声明的轴：

- stage / phase / layer / surface。
- proof level / runtime mode。
- authority side effect。
- public API / schema / protocol / command / template / skill surface。
- product truth 或质量判断。
- safety / permission / destructive boundary。
- lineage / relation / review gate。

若某个轴不属于本目标，ready 前用 `claim_limit`、`non_goals` 或 `constraints` 排除。
运行后或 completion 时，用 evidence `not_claimed` 或 E999 `remaining_gaps` 表达。

## Authoring Rules

### 1. Required Evidence Must Be Scoped

避免：

```yaml
completion:
  required_evidence:
    - workflow_complete=true
```

采用：

```yaml
completion:
  required_evidence:
    - "stage A to B adapter projection smoke passed"
    - "stage B to C DB-backed smoke passed"
    - "published authority write not claimed"
claim_limit: >
  Claims adapter projection and DB-backed smoke only; does not claim browser-visible
  behavior, production-near reliability, or external publication.
```

token 可以短。诚实性来自 `claim_evidence`、evidence refs、proof level、`not_claimed`
和 `remaining_gaps` 的映射，不来自超长 token 名称。

### 2. Proof Level Must Be Named, Not Re-enumerated

不要新增 canonical proof modality enum。优先复用现有 proof ladder：

```text
static/boundary check
-> offline fixture
-> replay
-> adapter/projection smoke
-> db_backed smoke
-> real runtime / manual acceptance
```

UI / harness 目标可继续使用已有 project 或 harness 词表，例如
`interface_headless`、`render_wiring`、`browser_visible`、`headless_product`、
`production_near`。新增 label 只作为 owner-local 说明，不进入 checker。

### 3. Ready Gate Stays The Same

当前公式不改：

```text
ready = stable goal contract + authorized proof_step can produce/inspect completion.required_evidence within claim_limit
```

semantic risk trigger 命中时，ready 前必须能说明 claim-bearing axes 如何落到
`completion.required_evidence`、`claim_limit`、`non_goals` 或 `constraints`。
如果说不清，不是新增 ready phase，而是返回 goal-contract repair、`needs_human`
或 `blocked`。

### 4. E999 Must Carry Claim Coverage Review

触发条件命中时，E999 completion review 必须包含 claim coverage review。最小形状：

```text
claim slice
-> required_evidence
-> evidence ref / command / check
-> proof level
-> not_claimed / remaining_gaps
```

JSON surface 仍使用 v2 字段：

```json
{
  "claim_evidence": [
    {
      "claim": "stage A to B adapter projection smoke passed; proof level: adapter/projection",
      "evidence": ["E003 evidence token", "bun run test:adapter-smoke passed"]
    }
  ],
  "not_claimed": [
    "browser_visible_behavior=false",
    "external_publication=false"
  ],
  "remaining_gaps": []
}
```

`not_proven` 只能作为叙事概念写进 summary 或 gap 文本；v2 JSON 不新增正式
`not_proven` 字段。

## Implementation Plan

第一波目标：让 agent authoring / proof-step / run / completion review guidance
都能执行 claim coverage review，不改 CLI schema parser。

| Wave | 文件 | 修改 |
| --- | --- | --- |
| W1 | `skills/goal/goal-contracts/SKILL.md` | 在 goal distance 和 rules 中加入 semantic risk trigger；要求 scoped `required_evidence`、`claim_limit`、`non_goals` 排除未声明 claim-bearing axes。 |
| W2 | `skills/goal/finding-proof-step/SKILL.md` | 在 Edge Self-Check 中加入 claim-bearing axes、proof level、not_claimed / remaining_gaps 自检；明确 target_delta 只证明当前 slice。 |
| W3 | `skills/goal/proof-step-implementation/SKILL.md` | 在 evidence / state transition 中要求保留 proof level 和相邻未声明 claim，不用宽 token 抹平不同 proof levels。 |
| W4 | `skills/goal/goal-proof-system/SKILL.md` | 在 completion 段加入 triggered claim coverage review 规则；说明 ready gate 不变。 |
| W5 | `skills/goal/goal-proof-system/templates/evidence.jsonl` | 更新 E999 示例，使 `claim_evidence[].claim` 可承载 proof level，`not_claimed` / `remaining_gaps` 非空示例不再像可省略装饰。 |
| W6 | `skills/goal/goal-proof-system/references/checker-rules.md` | 只记录 checker 第一波不解析 semantic coverage；后续可选 structural lint 的边界。 |
| W7 | `docs/goal-proof/README.md` | 索引和方法层说明同步，明确本提案仍非 authority，采纳后第一波无 CLI behavior change。 |

第一波验收：

- `rg` 能在四个 phase skills 和 E999 template 中找到 claim coverage review / semantic risk trigger 相关 guidance。
- `rg` 显示 `semantic_coverage_notes`、`proof_modality_by_path`、`not_in_scope` 只出现在 rejected / non-goal / historical context，不作为 active schema。
- `packages/cli/src/lib/goal-pack.ts` 无 parser / checker 行为变化。
- `bun run check` 通过。
- `git diff --check` 通过。

## Future Checker Boundary

后续 checker 只能作为 opt-in structural lint 或 `evidence_mode: strict` 增强：

- 可检查 done review 是否有 `claim_evidence`、`not_claimed`、`remaining_gaps`。
- 可检查 E999 的 `claim_evidence[].claim` 是否引用了每条可结构化拆分的 `completion.required_evidence`。
- 可检查 template 没有保留空占位。

不得检查：

- objective 自然语言是否完整覆盖。
- required evidence token 命名是否足够长。
- proof level label 是否属于新的全局 enum。

## Acceptance Trace

输入：

```text
用户要求交付一个多阶段分析 / 迁移 / 生成 / workflow。
```

Bad pack：

```text
objective 写全链路。
required_evidence 只要求第一段 real runtime。
后续阶段只证明 deterministic projection / lineage。
E999 只写 workflow_complete=true。
```

Expected：

```text
goal-contracts 阶段拆出 claim-bearing slices。
finding-proof-step 写明当前 proof level。
implementation evidence 记录 claims 和 not_claimed。
E999 claim coverage review 说明哪些阶段是 real runtime，哪些只是 deterministic projection。
若用户预期全链 real runtime，则 completion 停止，改为 remaining_gaps / needs_human / goal-contract repair。
```

## Non-Goals

- 不要求 checker 自动理解自然语言 objective。
- 不新增第二套 planning workflow、ledger 或 Goal Pack contract。
- 不新增 `goal.yaml` / `progress.yaml` 顶层 coverage 字段。
- 不新增 canonical proof modality enum。
- 不把每个小目标都变成矩阵流程。
- 不要求所有子路径跑最高 proof level。
- 不禁止 deterministic proof；只要求 deterministic 与 real runtime 的 claim 分开。

## Frozen Decisions

- 第一波只改 guidance / templates / docs，不改 CLI parser。
- canonical home 是 E999 completion review 的 claim coverage review；goal/progress 只放 authoring 和 proof-step guidance。
- semantic risk trigger 命中才强制；普通小目标不强制。
- proof level 复用现有 ladder 和 harness/project owner-local vocabulary。
- `not_in_scope` 不作为新 vocabulary；goal 阶段用 `non_goals` / `claim_limit`，evidence 阶段用 `not_claimed` / `remaining_gaps`。
- checker 后置，且只做 structural lint，不做 semantic parser。
