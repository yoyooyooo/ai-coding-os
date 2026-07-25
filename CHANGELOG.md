# Changelog

## 0.5.0-experimental.1 — 2026-07-26

### 定位升级

- 将 AI Coding OS 定位为面向 Agent 的项目认知、决策与验证基础设施。
- 确立 Agent-legible project、Minimal context / maximal legibility、No silent material assumption、Evidence over confidence、Earned persistence 等 Suite Doctrine。
- 将目标从“消灭所有 Unknown”修正为：避免未识别、未归属、未约束但足以改变结果的 material unknown 和 false known。

### 架构

- 将 `$evolvable-application-architecture` 收纯为跨语言 authority-first 应用架构语义内核。
- 将 TypeScript、点分文件名和 Monorepo 形态下沉为生态或 Preset 投影。
- 补全 Rust Projection，覆盖所有权与事实 Authority、模块/crate、trait/dispatch、async 生命周期、类型边界、公共 API 演进和证据。
- 新增 `$architecture-decision-system`，以局部、Earned 的 Architecture Decision IR 处理跨 Owner 决策、冲突、模糊点、Map–Territory 对账、Architecture Health 和 Diff。

### Skill 评估与 Suite 演进

- 新增 `$skill-evaluation-system`，吸收 SkillOpt 的 rollout、failure attribution、bounded update、held-out gate、checkpoint 和 transfer 思想。
- 新增 `$ai-coding-os-evolution`，负责 Agent Capability Profile、能力纪元重标定、fresh-context review、instruction/context ablation、候选 Suite 合成、发布与回滚。
- 明确“Train strategy; govern semantics”：可实验优化执行策略，不允许单一 Benchmark 分数偷换产品或架构语义 Authority。

### 治理与证据

- `$docs-governance` 增加 Context Legibility、Knowledge Freshness、Durable Assumption Hygiene 和失效条件治理。
- `$product-definition` 增加 tacit expectation elicitation 与 blind-spot pass。
- Harness Skills 支持 Empirical Unknown / Probe Request，并明确 `does_not_decide`。
- Suite Contracts 增加 decision-and-uncertainty 共享语义，同时保持中央 Contract 最小化。

### Preset 与工具

- 将通用 `application-core` 与 `monorepo-core` 分离。
- 新增 `rust` Preset Profile；`typescript-node` 不再隐式要求 Monorepo。
- 更新 Router、Evals、Suite audit、发布边界和源码卫生检查。
- 移除 `__MACOSX`、AppleDouble 与源码树内嵌交付 ZIP。

### Claim Ceiling

- 本版本仍为 experimental 快照。
- 未执行独立模型行为 Eval、SkillOpt 训练、真实 Rust 项目迁移或生产行为验证。
