# Architecture

本层保存 AI Coding OS 仓库的结构、owner 关系、运行时边界和发布视图。

## Owns

- Core Skills、project docs、Preset/generator、Harness、experiment 和 CLI 的结构关系。
- 核心知识网络与外部 execution owner 的依赖方向。
- source、audit、bundle 和 npm release 的边界。

## Must Not Own

- Product/SSoT 最高权威、任务状态、workflow dependency 或未采纳计划。

## Boundary

Architecture view 解释对象如何连接，不把结构图变成事实来源、阅读顺序或任务队列。与 SSoT、Standards、ADR 或源码冲突时，本层过期。

## Current Structure

```text
AI Coding OS repository
├── core Skill Suite
│   ├── Router and Contracts
│   ├── Governance and Product
│   ├── Application / Frontend / Effect Architecture
│   ├── Interface Capability and Harness/Test
│   └── Preset and deterministic Tooling
├── project knowledge network
│   └── Product / SSoT / Standards / ADR / Architecture / Roadmap / proof docs
├── co-located Goal Proof experiment
│   ├── user-invoked Skill
│   ├── dogfood history
│   └── experimental CLI package
└── repository verification and release support
```

Core Router 只选择知识 owner。Project docs 拥有 adopted semantics。External/experimental execution methods 可以消费 Authority 和 Evidence，但独立拥有 decomposition、dependency、status 和 completion。

## Physical Map

```text
skills/router/                        user-invoked core Owner Map
skills/contracts/                     portable shared contracts
skills/governance/                    docs Authority and network governance
skills/product/                       product definition
skills/architecture/                  application / frontend / Effect doctrine
skills/capability/                    interface capability planning
skills/harness/                       shared / headless / UI / frontend-test proof
skills/preset/                        reusable defaults and candidate snapshots
skills/tooling/                       generator / core audit / core bundle
experiments/goal-proof/               independent early workflow experiment
packages/cli/                         experiment CLI
docs/                                 project knowledge and standards network
```

## Distribution

```text
Core Suite ZIP
  contains skills/** only; canonical audit/manifest/reviews are versioned sidecars
  excludes experiments/**, packages/cli/**, project docs, repository release scripts
  uses bundle-local skills/VERSION
  runs its own audit/builder after extraction
  binds audit to packaged source through source_tree_sha256
  normalizes path/compiler diagnostics for cross-path deterministic provenance

npm goal-proof package
  contains compiled CLI and package docs
  uses an independent CLI package version
  does not distribute the core Skill Suite
```

## Routes

- Detailed repository ownership：[repository-layer-breakdown.md](repository-layer-breakdown.md)
- Current facts：[../ssot/README.md](../ssot/README.md)
- Standards：[../standards/README.md](../standards/README.md)
- Core Skill index：[../../skills/README.md](../../skills/README.md)
- Goal Proof experiment：[../../experiments/goal-proof/README.md](../../experiments/goal-proof/README.md)
