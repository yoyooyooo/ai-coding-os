# Roadmap

本层保存 AI Coding OS 当前迁移 gate、后续 capability delta 和 Evidence links。它不是 tracker、ticket、Goal、release 或其他 execution status 的副本。

## Owns

- 已接受的迁移方向与长期 gate。
- 已完成 capability delta 的 Evidence links。
- 尚未进入 Current Authority 的后续波次。

## Must Not Own

- 逐步任务、blocking edges、assignment、execution completion、Product/SSoT 或 Evidence record 原文。

## Current State

已完成的当前迁移：

- Core Suite 收敛为 14 个项目级知识、规范、Authority、产品、架构、接口、proof、Preset 和 Tooling Skills。
- Router 只提供 Owner Map；Route 不再表示阅读或执行序列。
- Docs/Preset/AGENTS 从 `Read First` 收敛为多入口 Knowledge/Discovery Surfaces 和 Routes。
- Owner-local Pass 统一解释为 coverage；真实状态机和事务协议保留 sequence。
- Core Evidence Envelope v2 收敛为方向中立、按真实消费压力存在的最小 claim-boundary shape；v1 directional reader 仅保留有限 compatibility。
- Goal Proof 从核心 `skills/**`、Router、Suite audit 和 core bundle 隔离到 `experiments/goal-proof/**`。
- Goal Proof 四个公开阶段 Skill 合并为一个 user-invoked experimental Skill 的 conditional references。
- Core Suite bundle 与 npm Goal CLI distribution 分开。
- Core ZIP 已自包含 bundle-local README、audit、builder 和 `skills/VERSION`；canonical audit 是实际 release sidecar，通过 `source_tree_sha256` 绑定源码，并排除绝对路径/compiler-dependent diagnostics 后参与跨机器 provenance hash。
- Preset renderer 只生成 `candidate-snapshot`，技术 fact writer map 归 Architecture Home；profile provenance 区分 user request、system default、dependency 和 resolved closure；语言中立 profile 不再泄漏 TypeScript filename patterns。
- Harness v2 validator 拒绝 legacy/canonical 双写和已知 camelCase aliases，静态 proof 可诚实声明 `[none]`；Effect Kit P3 Descriptor 必须绑定项目已有 Harness entry，verification command 有 timeout 和结构化失败输出。
- Product Source Synthesis 将静态源码/路由/Schema/表存在性归为 `implementation`，仅把执行或观察结果归为 `observed-behavior`。

Current facts 已同步到 SSoT，长期取舍由 [2026-07-25 boundary ADR](../adr/2026-07-25-core-knowledge-network-and-goal-proof-experiment.md) 解释。

## Future Candidates

- 基于真实跨项目安装证据，评估 core Suite ZIP 的发布渠道；当前只声明本仓自包含 bundle output。
- 冻结 doctrine，使用当前 10 个 composition cases 进行记录实际 Skill SHA 的真实 Agent dogfood；不以继续增加静态 case 替代行为证据。
- 基于真实使用与 model-run eval，判断 Goal Proof experiment 是否保留、重构或退役。
- 只有出现跨仓稳定 key、CI machine routing 或重复 Authority 冲突时，才重新评估 Authority Registry / Artifact Graph 扩张。
- 只有真实 navigation pressure 证明必要时，才增加 code-area projection 或更深 docs partitions。

## Promotion / Demotion

- 稳定事实 promote 到 SSoT。
- 可执行规则 promote 到 Standards。
- 长期取舍 promote 到 ADR。
- Execution detail 留在 selected method；历史 experiment evidence 留在 experiment dogfood。
- 已完成且只有追溯价值的 roadmap delta 缩成 Evidence link 或移出 current view。

## Evidence

- Public overview：`../../README.zh-CN.md`
- Current facts：`../ssot/README.md`
- Boundary ADR：`../adr/2026-07-25-core-knowledge-network-and-goal-proof-experiment.md`
- Core architecture：`../architecture/repository-layer-breakdown.md`
- Skill source standard：`../standards/skill-source-layout.md`
- Goal experiment history：`../../experiments/goal-proof/dogfood/README.md`
- Verification：`bun run check`、`bun run bundle:skills`

## Routes

- 文档网络：`../README.md`
- 当前事实：`../ssot/README.md`
- Standards：`../standards/README.md`
- Architecture：`../architecture/README.md`
