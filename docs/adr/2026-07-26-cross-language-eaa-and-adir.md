# ADR: Cross-language EAA And Local ADIR

- Status: accepted
- Date: 2026-07-26
- Scope: application architecture core and ecosystem projection model

## Context

EAA 的 Fact Authority、Use Case、Capability、Composition、Evolution 与 Evidence 语义天然跨语言，但旧内容仍泄露 TypeScript 点分文件名和 Monorepo 形态。Rust 讨论进一步暴露 memory ownership、visibility、crate 和 product fact authority 之间的混淆。跨 EAA、Frontend、Effect 和未来生态的冲突、Health 与长期决策也需要稳定中间表达。

## Decision

- `$evolvable-application-architecture` 收纯为跨语言 authority-first 应用架构语义内核。
- TypeScript、Frontend、Effect、Rust 与 repository topology 作为独立投影。
- Rust 先由 EAA Reference 与 Preset `rust` Profile 承载，不立即创建独立 Skill。
- 新增 `$architecture-decision-system`；其核心 ADIR 是局部、部分、引用式、Earned 的 decision-bearing graph。
- Decision Tree 是 owner-scoped rule forest 的局部视图；Architecture Health 是当前 Source/Rules/Evidence 的派生结果，不是静态分数。

## Alternatives

- 将每种语言复制一套完整架构哲学：拒绝，会产生语义漂移。
- 建立中央全项目 Architecture IR Schema：拒绝，当前没有足够机器消费者，且会增加形式完整性负担。
- 把 Architecture Decision System 内嵌 EAA：拒绝，完整 Suite 中它已有跨多个 Owner 的独立用户意图。

## Consequences

- Preset 分离 `application-core`、`monorepo-core`、`typescript-node` 和 `rust`。
- Rust 不继承 `.ts` patterns 或 Monorepo。
- ADIR 默认不落盘；需要长期共享时按 `$docs-governance` 进入 Architecture、ADR、Standards、Reports 或 Roadmap。
- 普通 Rust/Frontend/Effect 局部问题仍直接进入对应 Owner，不强制经 Architecture Decision System。

## Evidence And Claim Ceiling

源码与 Evals 证明语义和静态边界已表达；真实 Rust 项目地道性、编译、async shutdown、迁移和真实 Adapter 行为仍待项目级验证。

## Revisit Conditions

当 Rust 出现稳定独立触发、完整生态决策面和独立 Eval Corpus 时，评估晋升 `$rust-application-architecture`。
