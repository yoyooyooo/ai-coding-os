# Goal Proof Dogfood History

本目录保留 Goal Proof 早期实验在本仓产生的 Goal Packs、sources、notes 和 append-only evidence。它是实验历史与回归材料，不是 AI Coding OS 核心文档 layer，也不代表这些 workstreams 仍然 active。

## Owns

- 本仓历史 Goal Pack artifacts 与 evidence records。
- 已消费但仍有追溯价值的实验 sources。
- CLI 与方法演进的 dogfood fixtures。

## Must Not Own

- 当前 Product、SSoT、Standards、ADR、Architecture 或 Roadmap Authority。
- AI Coding OS 核心 Skill roster、路由或 execution workflow。
- 任意 tracker、ticket system 或外部执行方法的状态。

## Retention

真实 `evidence.jsonl` 保持原文和 append-only 语义。目录迁移不授权重写历史记录中的旧路径、命令或当时口径。需要修正当前解释时，在实验 README、当前 Skill/CLI 文档或新的 evidence 中说明，不篡改旧记录。

## Homes

```text
sources/             consumed experimental inputs
goals/<goal-id>/     historical Goal Packs
```

Goal Pack 常见结构：

```text
goal.yaml
progress.yaml
evidence.jsonl
plans/<work_id>.md   only when the experiment selected needs_plan
notes/**
```

## Recorded Goal Packs

- `goals/2026-06-03-triggered-claim-coverage-review/`
- `goals/2026-05-31-goal-proof-dag-frontier-cli/`
- `goals/2026-05-24-goal-proof-v2-dogfood-migration/`
- `goals/2026-05-24-agent-first-output-control-cli/`
- `goals/2026-05-23-evidence-query-cli/`
- `goals/2026-05-23-goal-relations-protocol/`
- `goals/2026-05-23-goal-relations-cli-verification/`
- `goals/2026-05-23-evidence-add-stdin-input-cli/`
- `goals/2026-05-23-relations-thread-discovery-cli/`

## Sources

- `sources/2026-05-31-ai-coding-os-compiler-narrative-delta-proposal.md`
- `sources/2026-06-03-product-capability-coverage-axis-proposal.md`
- `sources/2026-06-03-goal-contract-claim-coverage-review-proposal.md`
- `sources/2026-05-31-goal-proof-dag-frontier-view-proposal.md`
- `sources/2026-05-24-goal-proof-v2-dogfood-migration-handoff.md`

## Routes

- Experiment boundary and checks: `../README.md`
- User-invoked Skill: `../skill/SKILL.md`
- CLI package: `../../../packages/cli/`
- Current repository knowledge network: `../../../docs/README.md`
