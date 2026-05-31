# AI Coding OS 顶层叙事 Delta Proposal：Intent-to-Evidence State Transition

## 状态

```yaml
status: candidate-source
created_at: 2026-05-31
source_kind: narrative-delta-proposal
target_layers:
  - README.zh-CN.md
  - README.md
  - AGENTS.md
  - docs/product/README.md
  - docs/ssot/README.md
  - skills/README.md
not_authority: true
```

本文件是候选叙事提案，不是当前 SSoT、ADR、schema、CLI、skill 行为或完成证据。若采纳，应按本文的 layer adoption matrix 分层落地。

## 核心结论

建议把 AI Coding OS 的顶层叙事从“skill suite 列表”补强为：

```text
AI Coding OS 把人类意图推进为有证据支撑的 workspace 状态变化。
```

英文：

```text
AI Coding OS turns human intent into evidence-backed workspace state transitions.
```

`compiler` 可以作为 README / product 层的辅助隐喻，但公共主线应优先使用 `state transition`，因为它更贴近现有 Goal Proof 词表，概念更少，也不暗示存在真实编译器、统一线性流水线或第二套 runtime。

## 来源收敛

本 proposal 消化了两类来源：

- Fermi `agent-collaboration-memory-kernel` rolling work 暴露的问题：自然下一步不应只留在聊天里，而应由 Goal Pack 状态承接。
- 一轮 `$plan-optimality-loop` 对早期 handoff 的收敛结论：不新增 Goal Mode 系统，不新增第二 workflow，改用现有 Goal Proof slots 承接目标距离和 evidence 后续行判断。

跨仓 review 结论仅作为来源背景，不作为本仓 authority。本文已内联冻结约束，不要求未来读者跳转到 Fermi 路径才能理解采纳边界。

## Dominance Freeze

| 项 | 结论 |
| --- | --- |
| baseline | 当前 README / docs 已说明 AI Coding OS 是高智能 agent skill suite，Goal Proof 是长期目标载体，但没有把 rolling state transition 讲成主模型。 |
| rejected | `Terminal/Gate/Frontier` 作为规范 Goal Modes。 |
| rejected | `farthest still-falsifiable gate` 作为目标函数。 |
| rejected | `Continuation Turn` / `Continuation Window` 作为新 phase 或新 workflow。 |
| rejected | 把所有 skills 重释为单一 compiler pipeline。 |
| adopted | `intent -> goal contract -> proof_step -> evidence -> next_action` 作为 Goal Proof 主路径的最小 public loop。 |
| adopted | `minimum sufficient horizon` 作为 goal contract creation 的目标距离准则：足够吸收预期自然续行，但不能削弱 completion。 |
| adopted | evidence 后必须 reduce 回现有 Goal Pack state：`next_action`、`proof_step`、work item status、claims、not_claimed、blockers 或 `needs_human`。 |
| promotion boundary | README / product 可使用 state transition 和轻量 compiler 隐喻；SSoT 只收 artifact ownership / invariant，不收隐喻句；skills 只在 owner-local 文本中补 guard。 |

## 最小公共模型

公共叙事只需要一条 canonical loop：

```text
human intent
-> goal contract
-> proof_step
-> evidence
-> next_action
```

解释：

- `goal contract`：`goal.yaml` 中的 objective、completion、claim_limit、stop_rules、authority_refs 和 agent_authority。
- `proof_step`：`progress.yaml.proof_step` 中当前可证伪推进步。
- `evidence`：`evidence.jsonl` 中追加的 evidence record，包括 claims、not_claimed、checks、gaps。
- `next_action`：从 evidence reduce 出来的下一状态：`continue`、`proof_step`、`needs_plan`、`blocked`、`review`、`done` 或 `needs_human`。

这条 loop 复用现有 Goal Proof 词表。它不是新 schema、不是新 CLI、不是 scheduler、不是第二状态机。

## Artifact 解释

建议后续 README / product 适度加入这张解释，不进入 SSoT 的隐喻事实层：

| Artifact | State-transition meaning | 现有职责 |
| --- | --- | --- |
| `goal.yaml` | goal contract | 目标授权、边界、completion、claim_limit、stop_rules |
| `progress.yaml` | rolling state | proof_step、active_work_item、work_items、blockers、last_check、next_action |
| `evidence.jsonl` | append-only transition evidence | evidence records、claims、not_claimed、checks、completion review |
| `plans/<work_id>.md` | reviewed plan for high-risk slice | 仅 `needs_plan` 时存在，不是第二任务系统 |

SSoT 若后续采纳，只应收 artifact ownership 事实，例如：

```text
goal.yaml owns goal contract fields.
progress.yaml owns current rolling state.
evidence.jsonl is append-only evidence.
```

不要把 “AI Coding OS is a compiler” 或 “can be described as compiler” 写进 SSoT。

## 高智能 Agent 的自由边界

推荐产品层叙事：

```text
自由不在静默改目标。
自由在选择足够好的目标距离、proof path、执行 slice、evidence 解释和下一状态。
```

高自由：

- 主动识别用户真正需要的目标距离。
- 将模糊意图压缩成 goal contract。
- 选择最聪明的 proof path。
- 在当前 proof path 内执行最大的安全有用 slice。
- 把复杂结果压缩成 claims / not_claimed / gaps。
- 根据 evidence 决定下一状态。

硬边界：

- 不静默改变 objective、completion、claim_limit、stop_rules、authority_refs。
- 不把第一步 proof_step 反推成整个目标。
- 不把下一步自然工作留在聊天里而不写回 state。
- 不把未证明的相邻 surface 报成完成。
- 不把 provider summary、roadmap prose、chat memory 当作 evidence。

## 目标距离准则

不要采用：

```text
farthest still-falsifiable gate
```

采用：

```text
minimum sufficient horizon
```

定义：

```text
选择最小足够、用户授权、可证伪的目标距离：它能吸收预期自然续行，但不削弱 completion。
```

校准：

| 情况 | 判断 |
| --- | --- |
| 过近 | objective 只覆盖第一步 proof_step，完成后仍必然要用户重新判断自然下一步。应扩大到 minimum sufficient horizon。 |
| 过远 | completion evidence、claim_limit 或 stop_rules 无法封口。应缩小目标或请求用户决策。 |
| 合法 | 目标能吸收自然续行，且 protected fields 能判断继续/停止。proof_step 仍保持为当前最近可证伪推进步。 |

这个准则属于 `goal-contracts` 的 owner-local 规则。README / product 可解释目标距离，SSoT 不应新增 `Goal Mode`。

## Evidence 后状态归约

不要把 `Continuation Turn` / `Continuation Window` 做成新 phase。

采用 owner-local 规则：

```text
proof-step-implementation reduces fresh evidence into existing Goal Pack state.
```

归约目标只允许使用现有状态面：

- evidence `claims`
- evidence `not_claimed`
- `progress.yaml.next_action`
- `progress.yaml.proof_step`
- `progress.yaml.active_work_item`
- `progress.yaml.work_items[].status`
- `progress.yaml.blockers`
- `progress.yaml.last_check`

不新增 `next_action` 枚举，不新增 required YAML field，不新增 CLI 行为。

核心不变量：

```text
可以滚过当前计划，不能滚过 goal contract。
```

英文：

```text
Roll past the current plan, not past the goal contract.
```

## Layer Adoption Matrix

| Target | Allowed delta | Forbidden content | Verification |
| --- | --- | --- | --- |
| `README.zh-CN.md` / `README.md` | 顶层一句话；最小 loop；artifact 解释。 | 完整 decision table；`Terminal/Gate/Frontier` 规范模式；大写 Check 作为公共流程节点。 | 首屏能读出 state transition 主线；不新增 schema/CLI 承诺。 |
| `AGENTS.md` | 维护者 guardrail：state transition 模型不是新 workflow；目标距离和 evidence reduction 必须回到现有 Goal Proof fields。 | 把 compiler 写成新运行时、scheduler、CLI 或全局流水线。 | agent 实施规则仍指向现有 Goal Pack artifacts。 |
| `docs/product/README.md` | 高智能 agent 自由边界；为什么 state transition 模型服务 rolling execution。 | checker 规则、schema 细节、Goal Pack 当前状态。 | 产品层只讲定位和价值。 |
| `docs/ssot/README.md` | 仅 artifact ownership / invariant。 | `compiler` 隐喻事实；`Terminal/Gate/Frontier`；`Goal Mode` 字段。 | SSoT 不收 “can be described as” 句式。 |
| `skills/README.md` | 最多一句：skills 可被理解为支持 intent-to-evidence state transition 的方法集合；触发仍按 `name:`。 | 新 pass ownership 矩阵；把所有 skill 排成单一 pipeline。 | 现有 group ownership 表仍是主结构。 |
| owner skill files | `goal-contracts` 写目标距离准则；`proof-step-implementation` 写 evidence-to-progress 归约 guard。 | 五个 skill 复制完整 doctrine；大写 Check 进入公共词表。 | 另开 skill delta matrix 后实施。 |

README 采纳时应同时处理现有 `Diffusion` 隐喻：要么并入 state-transition loop，作为对 “coarse intent becomes sharper through evidence” 的一句说明；要么降级为历史/legacy metaphor。不要让 `Diffusion`、`compiler` 和 `state transition` 同时作为三个并列公共模型存在。

## Acceptance Trace

后续采纳本 proposal 时，至少用一个 trace 证明原问题被解决：

```text
input:
  用户讨论了多步方案，并要求转成 Goal Pack。

expected:
  agent 不把第一步实现写成 objective。
  agent 选择 minimum sufficient horizon。
  goal.yaml 能列出 completion evidence、claim_limit、stop_rules。
  progress.yaml.proof_step 只写当前最近可证伪推进步。

after evidence:
  evidence.jsonl 记录 claims / not_claimed。
  progress.yaml 写回 next_action。
  若下一步仍在 goal contract 内，更新 proof_step 或继续。
  若下一步会改变 objective/completion/claim_limit/stop_rules/authority_refs，写 needs_human。
```

Horizon calibration 必须覆盖：

- 拒绝过近目标：第一步完成后仍必然要求用户重新推断自然下一步。
- 拒绝过远目标：completion 或 claim_limit 无法封口。
- 接受合法目标：能吸收自然续行，且 evidence 后可由现有 `next_action` 决策。

## 不建议采纳

- 新增 `Goal Mode` YAML 字段。
- 把 `Terminal/Gate/Frontier` 写成规范分类。
- 把 `Goal Horizon Check` / `Continuation Check` 写成顶层公共流程名。
- 把 `Continuation Turn` / `Continuation Window` 写成新 phase。
- 把 compiler 隐喻写成 SSoT 当前事实。
- 把所有 skills 排成单一 compiler pipeline。
- 让 README 承载完整 decision table。

## 可实施文案草稿

中文 README 首段候选：

```text
AI Coding OS 是一套面向高智能 agent 的 AI coding 方法论和 skill suite。
它把人类意图推进为有证据支撑的 workspace 状态变化：先形成 goal contract，
再找到当前可证伪 proof_step，执行有用 slice，追加 evidence，并把 evidence
归约成下一步状态。
```

英文 README 首段候选：

```text
AI Coding OS is a methodology and skill suite for highly capable coding agents.
It turns human intent into evidence-backed workspace state transitions: form a
goal contract, find the next falsifiable proof_step, execute a useful slice,
append evidence, and reduce that evidence into the next state.
```

Goal Proof 段落候选：

```text
Goal Proof System is the state-transition carrier for long-running goals:
`goal.yaml` holds the goal contract, `progress.yaml` holds the current rolling
state, and `evidence.jsonl` is the append-only evidence trail.
```

中文：

```text
Goal Proof System 是长期目标的状态推进载体：`goal.yaml` 保存 goal contract，
`progress.yaml` 保存当前 rolling state，`evidence.jsonl` 是 append-only evidence trail。
```

## 后续建议

建议下一步单独开一个小范围 docs change 或 Goal Pack：

```text
目标：采纳 intent-to-evidence state transition 顶层叙事。
边界：只改 README / AGENTS / product / SSoT artifact facts / skills index；不改 CLI、schema、runtime。
完成：中英 README 主线一致；SSoT 不收隐喻；skills index 不新增 pass matrix；acceptance trace 能证明目标距离和 evidence 后状态归约。
```

Skill 源文件改造应单独进行，先写 delta matrix，再按 owner-local 规则修改，避免叙事变更和 skill 行为变更混成一个 claim。
