# Roadmap

本层保存顺序、状态、证据链接和迁移波次。

## Owns

- 已选择的迁移顺序。
- 当前状态摘要。
- 证据链接。
- 待执行 Goal Pack 或 roadmap 级 gap。

## Must Not Own

- 逐步实施任务清单。
- evidence record 细节。
- 产品事实。

## Boundary

本层只保存迁移顺序、当前 gate、证据链接和后续波次。它不是任务系统，
也不是 Goal Pack 状态的手写副本。Goal Pack ready / running / done、active work item、
evidence record 和 completion review 由 `docs/goal-proof/**` 与 CLI 输出拥有。

## Promotion / Demotion

- 被验证为稳定规则的 roadmap gate，promote 到 standards。
- 变成当前事实的迁移结果，promote 到 SSoT。
- 需要解释长期取舍的迁移决策，promote 到 ADR。
- 详细执行计划 demote 到 Goal Pack `plans/<work_id>.md` 或 root `specs/**`。
- 已完成且只剩追溯价值的材料，demote 到 evidence/source 或删除。

## Conflict

若 roadmap 状态与 Goal Pack evidence、CLI 输出、SSoT 或 standards 冲突，
roadmap 视为过期索引。修正链接和 gate 摘要，不复制 evidence 原文。

## 当前状态

已完成：

- v2 Goal Pack schema 迁移：`goal.yaml`、`progress.yaml`、`evidence.jsonl`、`proof_step`、`work_items`、`evidence_id`、`work_id`、`next_action`、`claim_limit`、`claim_evidence`。
- CLI / checker / renderer / tests / README / skills / templates / dogfood Goal Pack 主路径同步到 v2 口径。
- 仓库定位升级为 AI Coding OS 方法套件仓。
- skill suite 已扩展为 interface capability / product harness system / UI harness / headless harness 四层：新增 `interface-capability-planning`、`product-harness-system` 与 `ui-product-harness`。
- Repo shell 已收敛：GitHub repo / remote URL 为 `github.com/yoyooyooo/ai-coding-os`。
- 公开 skill suite 源码布局已收敛：canonical suite 使用本仓 `skills/**` grouped layout，公开触发名由 `SKILL.md` frontmatter `name` 决定，旧入口不保留 active alias。
- 顶层叙事 delta proposal 已收敛并完成首轮采纳：公共主线采用 `intent-to-evidence state transition`，`compiler` 只作 README / product 辅助隐喻，README 已将 `Diffusion` 并入该 loop。
- Goal Proof owner-local skill delta 已落地：`goal-contracts` 承载 `minimum sufficient horizon` 准则，`proof-step-implementation` 承载 evidence-to-progress 归约 guard，`ai-coding-os` 仅保留轻路由。
- 整仓 architecture view 已补齐：`docs/architecture/repository-layer-breakdown.md` 描述 public shell、method source、execution engine、authority docs、long-running artifacts、verification / release support 的分层边界。

已完成 Goal Pack 状态由 `../goal-proof/goals/` 下 evidence records 保留。当前没有 active Goal Pack。

## 后续波次

- 如果后续继续 polish product / SSoT 叙事，只采纳 artifact ownership 和用户价值表述；不得新增 workflow、schema、CLI 或公共 Check 名。
- 如果未来决定重命名 CLI / npm package，再单独开 Goal Pack；当前明确保留 `goal-proof`。
- 如果 OS 入口未来承载 CLI 或更重 artifact lifecycle，再重新评估 CLI / npm package 命名。

## 当前治理 Gate

本仓当前处于 `old-entry-retired` 状态：公开 repo shell、`skills/**` source layout、
README / docs / templates / tests 已按 `AI Coding OS` / `$ai-coding-os` /
`Goal Proof System` 口径收敛。后续不再扩散新命名。

下游 runtime 安装、同步脚本和外部 skill 管理仓不属于本仓公开状态。

## Evidence

- 顶层目标口径：`../../README.zh-CN.md`
- 文档路由：`../README.md`
- 当前事实：`../ssot/README.md`
- 命名 ADR：`../adr/2026-05-28-ai-coding-os-naming-and-boundary.md`
- Skill source layout 标准：`../standards/skill-source-layout.md`
- 顶层叙事 delta proposal：`../goal-proof/sources/2026-05-31-ai-coding-os-compiler-narrative-delta-proposal.md`
- 顶层叙事 review ledger：`../review-plan/runs/2026-05-31-compiler-narrative-delta-proposal-review.md`
- v2 迁移记录：`../goal-proof/goals/2026-05-24-goal-proof-v2-dogfood-migration/`
- Repo shell evidence：`gh repo view yoyooyooo/ai-coding-os`、`git remote -v`

## Read Next

- 文档路由：`../README.md`
- 当前事实：`../ssot/README.md`
- 文档治理：`../standards/docs-governance.md`
- Skill 源码布局：`../standards/skill-source-layout.md`
- Goal Pack 状态：`../goal-proof/README.md`
