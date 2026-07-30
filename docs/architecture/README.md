# Architecture

## Owns

- 八个语义 Skill 的当前拓扑、局部关系和边界。
- Self-navigating knowledge、Agent-legible project、Progressive Disclosure 和 cross-owner reconciliation。

## Must Not Own

- 产品 Quality Boundary、单个项目业务事实、一次运行结论或通用执行 Workflow。

## Current views

- [Skill Network](skill-network.md) — 八个 Owner 如何组合且保持独立。
- [Project Legibility](project-legibility.md) — 项目怎样通过工程表面解释自身。
- [Progressive Disclosure](progressive-disclosure.md) — 主 Skill、Reference、Template 与 Contextual Edge 的形状。
- [Cross-owner Reconciliation](cross-owner-reconciliation.md) — Accepted Meaning、Source Reality、Observed Reality 和多个 Owner 如何局部对账。

## Architectural invariants

```text
semantic owner != documentation home != fact authority != evidence owner
repository directory != package/crate != host != deployable != authority boundary
intent != proposal != projection != accepted fact
Service/Layer/Runtime != product meaning
Effect mechanism projection != second application source grammar
successful local observation != broad behavioral proof
portable default != universal mandate
```
