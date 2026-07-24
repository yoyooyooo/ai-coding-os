# Review Plan

本层存放 `$plan-optimality-loop` 对结构化计划、SSoT contract、proposal 和叙事候选稿的评审 ledger。

## Owns

- 多 reviewer 评审的 bootstrap、review contract、findings、counter proposals、adopted candidate、freeze record 和 consensus 状态。
- 对候选计划或叙事提案的改进轨迹。

## Must Not Own

- 产品事实、当前术语权威或已采纳取舍。
- Goal Pack 运行状态和 evidence record。
- Completion evidence 或 implementation status。
- README、SSoT、standard 或 ADR 的最终正文。

## Boundary

本层是评审过程和收敛结果的记录层。它可以说明某个候选提案为什么被修改、采纳或拒绝，但不能替代目标文件本身，也不能覆盖 `docs/ssot/**`、`docs/standards/**`、`docs/adr/**` 或 `docs/goal-proof/**`。

## Promotion / Demotion

- 已达成共识的 adopted candidate 可以作为后续 README、SSoT、standard、ADR、Goal Pack 或 source 修改的输入。
- 稳定事实必须 promote 到 `docs/ssot/**`，可执行规则 promote 到 `docs/standards/**`，长期取舍 promote 到 `docs/adr/**`。
- 只剩追溯价值的评审材料保留在 `runs/**`；不要复制进产品文档正文。
- 若 ledger 中的候选方案被目标文件正式吸收，ledger 仍作为评审证据保留，不升级为 authority。

## Homes

| 角色 | 路径 |
| --- | --- |
| review ledgers | `runs/*.md` |

最近 ledger：

- `runs/2026-06-03-product-capability-coverage-axis-rearchitecture-review.md`：Product Capability Coverage proposal 重审，收敛为 standalone `product-capability-coverage` 薄 skill，放入 `skills/capability/`，AI Coding OS 集成为 optional mapping。
- `runs/2026-06-03-product-capability-coverage-axis-proposal-review.md`：Product Capability Coverage Axis proposal，收敛为 decision-gated Product Proof Placement Lens；第一波不新增 public skill / coverage group / Coverage Map artifact。
- `runs/2026-06-03-goal-contract-semantic-coverage-gate-proposal-review.md`：Triggered Claim Coverage Review proposal，收敛 semantic coverage gate 为现有 v2 surface 上的 E999 claim coverage review。
- `runs/2026-06-02-goal-pack-ready-gate-diff-review.md`：C-001 owner split、ready gate、docs-only proof-surface predicate 和叙事 envelope 边界评审。

## Read Next

- 文档路由：`../README.md`
- 文档治理：`../standards/docs-governance.md`
- Goal Proof System：`../goal-proof/README.md`
