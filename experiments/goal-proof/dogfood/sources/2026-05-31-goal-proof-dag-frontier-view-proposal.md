# Goal Proof DAG / Ready Frontier Implementation Plan

## 状态

```yaml
status: adopted-implementation-plan
created_at: 2026-05-31
updated_at: 2026-05-31
source_kind: cli-delta-plan
source_context: fermi_goal_pack_thread
origin_repo: /Users/yoyo/Documents/code/personal/fermi
target_project: ai-coding-os
target_surface:
  - goal-proof CLI
  - Goal Relations
  - Goal Pack progress.blockers schema
review_ledger: docs/review-plan/runs/2026-05-31-goal-proof-dag-frontier-plan-review.md
plan_authority: true
not_current_cli_contract: true
not_current_schema_contract: true
```

本文件已经从候选 proposal 收敛为后续实施用计划。它可以作为新 Goal Pack
或实现分支的计划输入，但还不是当前发布版 CLI contract、schema SSoT、ADR
或完成证据。

## 问题

Fermi 的 `agent-operable-memory-next-wave` thread 暴露了一个真实 operator
问题：人类或 agent 需要快速回答：

- 这组 Goal Pack 的依赖图是什么。
- 现在哪个 Goal Pack 可以开跑。
- blocked Goal Pack 分别在等哪个前置完成或人工决定。
- 哪些关系是已经被 predecessor evidence 验证的 relation，哪些只是 pending wait。

现有 `relations` command family 继续有价值：

```bash
goal-proof relations list [target] [--thread <id>] [--json]
goal-proof relations goals [target] [--thread <id>] ...
goal-proof relations work [target] [--thread <id>] ...
goal-proof relations check [target] [--thread <id>] [--json]
goal-proof relations graph [target] [--thread <id>] [--json]
```

但它们不应扩成 queue、scheduler、worklist 或 pending dependency system。

当前边界保持：

```text
relations.links   = verified cross-pack relation evidence
relations check   = relation evidence verifier
relations graph   = derived relation metadata graph
relations goals   = thread-member Goal Pack discovery
relations work    = thread-member work item discovery
```

缺口是 operator-ready projection：同一 thread 里，哪些 pack 现在可执行，哪些 pack
被等待条件挡住，以及这些等待条件对应哪些 edge。

## Adopted Candidate

采用 top-level `goal-proof dag`，但 public contract 必须是 frontier-first，
不是 scheduler-first，也不是 stored graph-first。

```bash
goal-proof dag [project-root|goals-dir] --thread <thread-id> [--json]
```

MVP 中 `--thread` 必填。没有 thread 时不做跨 thread 聚合，避免把多个独立
Goal Thread 拼成一个隐式执行计划。

`goal-proof dag` 是只读 projection：

- 不启动 work。
- 不自动改 `progress.yaml.status`、`active_work_item`、`blockers` 或 `next_action`。
- 不创建 successor pack。
- 不声明 DAG 顺序就是 scheduler order。
- 不改变 `relations check` 对 hard relation evidence 的失败语义。

## Dominance Freeze

最终结构压成三个 owner：

```text
relations.links      verified relation evidence
progress.blockers    pending wait condition
goal-proof dag       read-only thread frontier projection
```

`relations graph` 继续只渲染 relation metadata graph。`goal-proof dag` 可以复用
relations collector 和 checker helper，但不能把 `relations` namespace 变成 readiness
queue。

## 不采纳

- 不让 `relations check` 忽略 missing future evidence。
- 不把 pending dependency 写进 `relations.links`。
- 不把 `relations graph` 扩成 verified graph、pending blocker、ready frontier、
  scheduler 四种语义的混合入口。
- 不新增 stored thread object、thread lifecycle、thread registry 或 graph file。
- 不新增 `goal-proof dag run`、`goal-proof thread run`、`relations queue`、
  `relations worklist`。
- 不解析 free-text blocker 并把它当 authority。
- 不引入 `relations.dag.predecessor_goal_ids` 或 `successor_goal_ids`。
- 不在 blocker schema 里写 `unblocks.status` 或 `unblocks.next_action`。
- 不在 pending blocker 里预写未来 `E999`。

## Authority Rules

### `relations.links`

`relations.links` 只表达已经可由 predecessor evidence 验证的关系：

```yaml
relations:
  thread_id: agent-operable-memory-next-wave
  links:
    - goal_id: 2026-05-31-memory-operation-safety-hardening
      relation: successor_of
      evidence_ref: E999
      evidence:
        - completion_satisfied=true
```

如果 predecessor 的 evidence record 不存在，`relations check` 继续失败。不要为
pending dependency 放宽这个规则。

### `progress.blockers`

`progress.blockers` 表达当前 Goal Pack 的 pending wait condition。它允许兼容
现有 string blocker，同时新增 structured blocker union。

允许形状：

```yaml
blockers:
  - "等待人工确认发布窗口。"
  - kind: goal_completion
    goal_id: "2026-05-31-memory-operation-safety-hardening"
    predicate:
      completion_satisfied: true
  - kind: decision
    decision_id: "provider_selection"
    description: "选择真实 external Memory provider。"
```

规则：

- string blocker 是 human-readable opaque blocker，只显示 raw text，不生成 edge。
- `kind: goal_completion` 表示等待另一个 Goal Pack 达到 completion predicate。
- pending blocker 不写未来 `evidence_ref: E999`。
- predecessor 完成后，successor 可以再用 `relations.links` 引用真实 evidence record。
- `kind: decision` 是 node-level blocker，不生成 goal-to-goal edge。
- blocker 不写解除后的状态迁移。解除必须通过后续 evidence record 和 `apply` 明确发生。

### `goal-proof dag`

`goal-proof dag` 只读取：

- `goal.yaml.id`
- `goal.yaml.status`
- `goal.yaml.relations.thread_id`
- `goal.yaml.relations.links`
- `progress.yaml.status`
- `progress.yaml.next_action`
- `progress.yaml.active_work_item`
- `progress.yaml.blockers`
- `evidence.jsonl` 中 relation check 所需 evidence

MVP 不读取 `relations.dag.*`。若未来需要短显示名，只能作为纯 display alias 另行评审，
不得承载 edge。

## Edge Admission

`goal-proof dag` 的 edge 只来自两个 authority：

```text
verified_dependency  relations.links 中的 successor_of / depends_on
blocking             structured progress.blockers 中的 goal_completion
```

不作为 readiness edge：

- `related_to`
- `supersedes`
- raw string blockers
- display alias
- free-text 中看似依赖的自然语言

`supersedes` 和 `related_to` 仍属于 `relations graph` 的 relation metadata surface；
不要在 frontier view 里暗示它们是可执行顺序。

## Frontier Classification

`goal-proof dag` 必须保留 stored state 和 derived state 的区别。

Stored fields：

- `goal_status`
- `progress_status`
- `next_action`
- `active_work_item`

Derived field：

- `frontier_state`

分类规则：

| 条件 | `frontier_state` | 说明 |
| --- | --- | --- |
| `progress_status` 或 `goal_status` 是 `done` | `done` | 已完成，不进入 ready frontier |
| `progress_status` 或 `goal_status` 是 `retired` | `retired` | 已退役，不进入 ready frontier |
| 有 structured 或 raw blocker | `blocked` | raw blocker 不生成 edge，但会挡住 ready |
| `progress_status=blocked` 或 `next_action=blocked` | `blocked` | 状态已阻塞 |
| `next_action=needs_human` | `blocked` | 需要人工决定 |
| `progress_status=ready|running` 且 `next_action=proof_step|continue|needs_plan|review` | `ready` | 当前可由 agent/operator 推进 |
| `progress_status=forming` | `forming` | 目标尚未准备执行 |
| 其他组合 | `unknown` | 输出 warning |

如果 stored state 与 blocker 冲突，例如 `progress_status=ready` 但存在 blocker，
`frontier_state` 必须是 `blocked`，并输出 warning。

## JSON Contract

最小 JSON：

```json
{
  "ok": true,
  "thread_id": "agent-operable-memory-next-wave",
  "goals_root": "docs/goal-proof/goals",
  "nodes": [
    {
      "goal_id": "2026-05-31-memory-operation-safety-hardening",
      "path": "docs/goal-proof/goals/2026-05-31-memory-operation-safety-hardening",
      "goal_status": "ready",
      "progress_status": "ready",
      "next_action": "proof_step",
      "active_work_item": "W001",
      "frontier_state": "ready",
      "blockers": {
        "structured": [],
        "raw": []
      }
    }
  ],
  "edges": [
    {
      "from_goal_id": "2026-05-31-memory-operation-safety-hardening",
      "to_goal_id": "2026-05-31-real-codex-memory-command-execution",
      "kind": "blocking",
      "source": "progress.blockers",
      "predicate": {
        "completion_satisfied": true
      }
    }
  ],
  "ready_goal_ids": ["2026-05-31-memory-operation-safety-hardening"],
  "blocked_goal_ids": ["2026-05-31-real-codex-memory-command-execution"],
  "done_goal_ids": [],
  "errors": [],
  "warnings": []
}
```

`nodes[].goal_id` 是主键。不要让可选 display label 成为 JSON 主键。

Text 输出应服务 operator 扫描：

```text
thread_id=agent-operable-memory-next-wave

ready:
  2026-05-31-memory-operation-safety-hardening next=proof_step active_work_item=W001

blocked:
  2026-05-31-real-codex-memory-command-execution waits_for_goal=2026-05-31-memory-operation-safety-hardening completion_satisfied=true
  2026-05-31-real-external-memory-provider-opt-in-spike waits_for_decision=provider_selection

edges:
  2026-05-31-memory-operation-safety-hardening -> 2026-05-31-real-codex-memory-command-execution kind=blocking
```

## Error And Warning Policy

`ok=false`：

- malformed structured blocker。
- `goal_completion.goal_id` 在 goals root 中不存在。
- selected thread 内 goal id 重复。
- admitted readiness edges 出现 cycle。
- `relations check` 对 selected thread 的 hard relation evidence 失败。

`ok=true` 但输出 warning：

- string blocker 只能 raw display，不能生成 edge。
- `goal_completion.goal_id` 存在但不在 selected thread 中。
- stored state 看似 ready 但 blocker 非空。
- stored state / `next_action` 组合无法分类，只能给 `frontier_state=unknown`。
- `related_to` 或 `supersedes` relation 存在但不进入 readiness edge。

## Implementation Plan

### W1: Blocker Union Schema

目标：让 pending wait condition 有机器可读 authority，并保持旧 string blocker 兼容。

触达：

- `packages/cli/src/lib/goal-pack.ts`
  - 新增 `parseProgressBlockers`。
  - `progress.blockers` 支持 `string | goal_completion_blocker | decision_blocker`。
  - serializer 必须保留 object blocker 形状。
  - `apply` 合并 `blocked_by` 时不能把 object blocker 写成 `[object Object]`。
  - blocked evidence 的 `blocked_by` 可继续是 string，也可使用同一 structured blocker union。
- `packages/cli/test/check-goal-pack.test.ts`
  - 校验合法 structured blockers。
  - 拒绝 malformed structured blockers。
  - 证明 string blockers 仍兼容。
  - 证明 `apply` 后 structured blockers 不丢形。
- `skills/goal/goal-proof-system/references/checker-rules.md`
  - 记录 blocker union schema 和校验边界。
- `skills/goal/goal-proof-system/templates/progress.yaml`
  - 保留轻量 string 示例，并增加 structured long-running 示例。

W1 不新增 `goal-proof dag`。

### W2: Read-Only DAG Frontier Command

目标：新增只读 projection，不创建 scheduler 或 second authority。

触达：

- `packages/cli/src/goal-proof.ts`
  - 新增 top-level `dag` command。
  - `--thread <id>` 在 MVP 中 required。
  - 支持 `--json`。
- Future candidate: packages/cli/src/render-goal-dag.ts（当前 CLI 尚未实现）。
  - 预期新建 renderer。
  - 复用 goals root 解析、Goal Pack collection 和 relation check helper。
  - 只读取 selected thread。
  - 生成 `nodes`、`edges`、`ready_goal_ids`、`blocked_goal_ids`、`done_goal_ids`、
    `errors`、`warnings`。
- `packages/cli/src/index.ts`
  - export DAG renderer / runner。
- Future candidate: packages/cli/test/goal-dag-cli.test.ts（当前测试集尚未实现）。
  - 预期包含 Fermi-like fixture。
  - JSON contract。
  - text output。
  - no-write assertion。
  - `--thread` required。
  - raw blocker 不生成 edge。
  - structured blocker 生成 blocking edge。
  - cycle / missing goal error。
- `packages/cli/test/goal-relations-cli.test.ts`
  - regression：`relations check`、`relations graph`、`relations goals`、
    `relations work` 行为不变。

### W3: Public Docs And Skill Sync

目标：同步 public surface，避免命令存在但 docs/skills 没有路由。

触达：

- `README.md`
- `README.zh-CN.md`
- `packages/cli/README.md`
- `packages/cli/README.zh-CN.md`
- `skills/goal/goal-proof-system/references/cli.md`
- `skills/goal/goal-proof-system/references/goal-relations.md`
- `docs/goal-proof/README.md`
- 相关 help/documentation coverage tests

文案必须保留：

```text
Use relations graph for verified relation metadata.
Use dag for thread DAG, blockers, and ready frontier.
```

同时必须写明：

- `dag` 只读。
- `dag` 不是 scheduler。
- `relations.thread_id` 仍只是 shared label。
- Goal Pack 仍是完成单位。

## Test Plan

最小命令：

```bash
bun test packages/cli/test/check-goal-pack.test.ts
bun test packages/cli/test/goal-dag-cli.test.ts
bun test packages/cli/test/goal-relations-cli.test.ts
bun run check
```

必须覆盖：

- structured blocker shape 被 `goal-proof check` 接受。
- malformed structured blocker 被 `goal-proof check` 拒绝。
- string blocker 仍可用，且 `dag` 只 raw display。
- `apply` 不破坏 structured blockers。
- `dag --json` 输出 `nodes`、`edges`、`ready_goal_ids`、`blocked_goal_ids`、
  `warnings`、`errors`。
- Fermi-like fixture 中 M1 ready，M2/M3/M4/M5 blocked。
- M4 同时有 predecessor completion blocker 和 `provider_selection` decision blocker。
- `relations.links` 缺 predecessor evidence 时，`relations check` 仍失败。
- `dag` 对 pending structured blocker 不因缺 future `E999` 失败。
- `dag` 不写任何 Goal Pack state。
- `relations graph` 输出仍只代表 relation metadata graph。
- `relations goals` / `relations work` 不出现 queue/order/scheduler 文案。
- CLI help、root README、package README、skill CLI reference 都记录 `goal-proof dag`。

## Acceptance Trace

Fixture：

```text
thread_id=agent-operable-memory-next-wave
M1 ready, next_action=proof_step
M2 blocked, goal_completion waits_for M1 completion_satisfied=true
M3 blocked, goal_completion waits_for M2 completion_satisfied=true
M4 blocked, goal_completion waits_for M3 completion_satisfied=true plus decision provider_selection
M5 blocked, goal_completion waits_for M1 completion_satisfied=true
```

执行：

```bash
goal-proof dag docs/goal-proof/goals --thread agent-operable-memory-next-wave --json
```

期望：

- `ok=true`
- `ready_goal_ids` 只包含 M1 的 `goal_id`
- `blocked_goal_ids` 包含 M2、M3、M4、M5 的 `goal_id`
- `edges` 至少包含 M1 -> M2、M2 -> M3、M3 -> M4、M1 -> M5
- M4 node 的 blockers 同时包含 goal completion blocker 和 decision blocker
- 没有 state write
- 没有 scheduler / queue claim

## Follow-Up Boundary

本计划停止在实施准备，不开始改 CLI。若进入执行，建议创建独立 Goal Pack 或实现分支，
把本文件作为 authority ref，并按 W1 -> W2 -> W3 顺序推进。
