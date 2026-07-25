# ADR: Evidence-driven Skill Evaluation And Suite Evolution

- Status: accepted
- Date: 2026-07-26
- Scope: Skill behavior evaluation and Capability Epoch release governance

## Context

LLM/Agent 能力按阶段提升，旧脚手架可能从帮助变为束缚。仅用新模型开多个上下文 Review 能发现候选问题，但不能证明候选 Skill 真正改善行为。SkillOpt 展示了 rollout、reflection、bounded edit、held-out gate、checkpoint 与 experience replay 的实证闭环。

## Decision

- 新增 `$skill-evaluation-system`，负责 corpus、rollout、failure attribution、Ablation、held-out Gate、Transfer 和 Model-run Evidence。
- 新增 `$ai-coding-os-evolution`，负责 Agent Capability Profile、Capability Epoch、跨 Skill candidate synthesis、兼容边界、发布与回滚。
- 采用 `Train strategy; govern semantics`：执行策略可以实验优化，语义 Constitution 不能被单一分数自动改写。
- 评估使用分层 veto Gate，不把 Authority 破坏与平均任务收益相抵消。
- Candidate 默认 staged adoption；同一上下文不能作为唯一作者、唯一裁判和发布 Authority。

## Alternatives

- 新模型直接重写整套 Skills：拒绝，缺乏对照、held-out Evidence 和回滚。
- 原样 vendoring SkillOpt：拒绝，本 Suite 是多 Skill 知识网络，且项目级 Harness 超出纯文本 Benchmark。
- 只保留人工 Review：拒绝，无法测量 Skill 的边际价值与 Context 束缚成本。

## Consequences

- Failure 在修改 Skill 前先归因。
- Current、Candidate、Minimal Kernel 和 No Suite 成为默认对照。
- Eval contamination、case family、exposure 和 corpus hash 成为一等完整性问题。
- Suite 可以递归审视自己，但不能循环自证。

## Evidence And Claim Ceiling

本 ADR 采纳评估协议；当前快照尚未执行独立 Model-run、SkillOpt training 或 field sleep cycle，因此不声称行为增益。

## Revisit Conditions

在获得真实 Corpus、可执行 Oracle 和至少两个机器消费者后，再决定是否发布通用 Model-run Schema、评估工具链或 SkillOpt Backend adapter。
