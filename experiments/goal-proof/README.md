# Goal Proof Experiment

Goal Proof 是与 AI Coding OS 核心知识/规范网络共仓维护的早期实验。它是否适合作为长期 AI coding 执行方法尚未确定，因此不属于核心 Skill Suite、不进入 `$ai-coding-os` 路由，也不随核心 Suite ZIP 发布。

## Agent Kit mapping boundary

Goal Proof 的 user-invoked Skill 位于 `experiments/goal-proof/skill/**`，由本实验拥有。它使用与九项 Suite outbound mapping（八个 shared core Skill 加 supporting `effect-server-module-design`）分离的 bidirectional Agent Kit edge；不得把 Goal Proof 误写成 Suite outbound ownership、declared project source roster 或 `skills/**` 的正文来源。

配置、PR 或 staged export 只证明候选路由，不证明 Agent Kit admission、mirror publication、runtime rollout 或 npm release；这些结论必须引用对应 accepted commit 与发布回执。`release/**` 继续是 historical pre-import evidence，除非 release workflow 明确重生成，否则不作为当前证明。

## 实验边界

```text
Goal Proof experiment owns:
  Goal Pack 状态协议
  goal.yaml / progress.yaml / evidence.jsonl
  proof step、append-only evidence、completion review
  goal-proof CLI

AI Coding OS core owns:
  项目知识、规范、Authority、架构、产品与 proof semantics

Selected external workflow owns:
  ticket/tracker dependency、frontier、assignment、status 与发布生命周期
```

同一 workstream 只保留一个 execution-state owner。已有 tracker、tickets 或其他方法时，不创建平行 Goal ledger。

## 目录

```text
experiments/goal-proof/skill/     user-invoked `$goal-proof` Skill
experiments/goal-proof/dogfood/   本仓历史 Goal Pack、来源和证据
packages/cli/                     实验 CLI 源码与测试
```

`dogfood/**/evidence.jsonl` 是历史证据；路径迁移不授权重写记录内容。

## Invocation

`$goal-proof` 是 user-invoked。任务规模、持续时间或复杂度不会自动触发实验。项目若采用它，应显式声明 Goal Pack Home；没有项目约定时使用 `.goal-proof/goals/<goal-id>/`。CLI 0.2.x 仍读取旧 `docs/goal-proof/goals/<goal-id>/`，但新文档和写入不再采用该路径。

## 验证

```bash
python3 experiments/goal-proof/scripts/self_check.py
bun run --filter goal-proof build
bun run --filter goal-proof typecheck
bun run --filter goal-proof test
```

实验自检验证 Skill frontmatter、Skill-local links、eval 结构、Goal/Progress/Evidence templates 与 JSON Schemas。CLI 测试验证实际读写和兼容行为。核心 Suite audit 不把本实验计入 Skill roster。

## 与核心知识网络的关系

项目 Product、SSoT、Standards、ADR、Architecture、Contracts 和可执行 evidence 仍是 claim-scoped Authority。Goal Pack 可以引用它们，但不能复制或覆盖。实验执行中产生的 durable decision 回到其项目 owner；Goal progress 和 completion 仍留在实验方法内。
