# Roadmap

## Owns

- 尚未成为 Current Suite 的长期能力候选、前提、晋升门和首个可证伪步骤。

## Must Not Own

- 当前事实、已接受架构、执行状态或完成声明。

## Future Candidates

### Machine-consumable ADIR

- **Current foundation:** `$architecture-decision-system` 的语义模型、Decision Trace、Health 与项目 materialization contract。
- **Not current:** 全局 Schema、Registry、CI graph 和自动架构数据库。
- **Promotion gate:** 至少两个独立机器消费者需要稳定读写同一 IR，并证明 Markdown/reference 路由不足。
- **First proof:** 在两个真实项目上用同一最小 Schema 完成 architecture diff 与 drift check，且不制造第二 Current Home。

### Model-run Skill Evaluation Tooling

- **Current foundation:** `$skill-evaluation-system` 的 Evaluation Ladder、split integrity、attribution 和 hierarchical gates。
- **Not current:** 通用 runner、dashboard、自动 optimizer 或 nightly Suite rewrite。
- **Promotion gate:** 已有可执行 Oracle、Protected Corpus、重复运行预算和明确数据边界。
- **First proof:** 对一个 Skill 比较 Current/Candidate/Minimal/No-Skill，并保留完整 manifest、held-out Gate 和 rollback。

### SkillOpt Backend Adapter

- **Current foundation:** 已吸收 rollout、bounded update、held-out gate、checkpoint 和 staged adoption 语义。
- **Not current:** 未 vendoring SkillOpt，也未声称兼容其所有 Harness。
- **Promotion gate:** 真实 Suite Eval 证明外部 Backend 能复用项目 Harness，且不会将语义 Constitution 当作普通 Prompt 权重训练。
- **First proof:** 一个隔离的单 Skill E1 候选优化实验。

### Rust Skill Promotion

- **Current foundation:** EAA Rust Projection、Rust Evals、Preset `rust` Profile。
- **Not current:** 独立 `$rust-application-architecture`。
- **Promotion gate:** Rust 形成稳定独立用户意图、完整模块/crate/trait/async/API/release/proof 决策面和独立 Corpus。
- **First proof:** 两个结构不同的真实 Rust 项目使用同一投影，暴露出 EAA Reference 无法清晰拥有的独立决策。

### Compatibility Overlays

- **Current foundation:** Canonical Suite 面向默认 Agent Capability Baseline，脚手架定期 re-earn。
- **Not current:** 为所有模型在主 Skill 内堆叠多套指导。
- **Promotion gate:** 次级 Agent Profile 有真实部署需求，且 Protected Evals 证明需要额外显式约束。
- **First proof:** Overlay 相对 Canonical 保持语义一致并显著减少该 Profile 的失败。

## Routes

- [Current SSoT](../ssot/README.md)
- [Current Architecture](../architecture/README.md)
- [Skill Evaluation Standard](../standards/skill-evaluation-and-release.md)
