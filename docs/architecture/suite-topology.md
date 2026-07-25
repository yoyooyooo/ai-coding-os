# Suite Topology

## Core Shape

```text
Product / project obligations
          │
          ▼
semantic owners and shared contracts
          │
          ├── application architecture core
          ├── frontend / Effect / Rust / repository projections
          ├── architecture decision and local ADIR
          └── documentation governance
          │
          ▼
implementation / preset candidates / deterministic generation
          │
          ▼
Harness, tests, runtime and release Evidence
          │
          ▼
project knowledge update or Suite evolution evidence
```

## Source Groups

| Group | Role |
| --- | --- |
| `router` | 只在意图不明确或跨 Owner 时选择最小 Owner 集 |
| `contracts` | 最小跨 Skill 术语与可选机器合同，不成为中央本体 |
| `governance` | Docs Authority、Route、Earned Shape、freshness 和 cleanup |
| `product` | 产品定义、隐性期望、blind spots、要求和验收 |
| `architecture` | EAA、Frontend、Effect 与跨 Owner Architecture Decision System |
| `capability` | 用户工作到 InterfaceCapability、state/data owner 和 proof needs |
| `harness` | Proof Surface、Probe、Evidence 和 Claim Ceiling |
| `preset` | 可复用候选默认；项目显式采纳后才进入 Current Home |
| `tooling` | 只消费已确定输入的确定性生成与离线审计 |
| `meta` | Skill 行为评估与 Suite Capability Epoch 演进 |

## Cross-language Architecture

`$evolvable-application-architecture` 只拥有语言无关的：

```text
Fact Authority
Consistency Domain
Use Case / Transaction
Observation / Candidate / Receipt
Capability Port / Adapter
Composition / Lifecycle
Migration / Fencing / Deletion Gate
Evidence Boundary
```

生态投影分别决定地道实现：

```text
TypeScript -> semantic filenames, module/public/wiring, package checks
Frontend   -> state owner, intent, projection, reconciliation, host resources
Effect     -> Service, Layer, Runtime, Scope, typed failure, concurrency
Rust       -> module visibility, crate promotion, trait/dispatch, async shutdown,
              type boundaries, SemVer/MSRV/features, Rust-specific proof
```

核心语义可以组合，但任何投影都不能重定义产品事实 Authority、产品语义或 Claim Ceiling。

## Preset Topology

```text
application-core  language-neutral architecture defaults
monorepo-core     selected workspace repository topology
typescript-node   TypeScript naming/import projection
rust              Rust module/crate/trait/async/public-API projection
react/effect      independent ecosystem projections
verification-core proof-contract defaults
```

Profiles 通过 `requires` 形成最小 closure；`requested`、`defaults_added`、`dependency_added` 和 `resolved` 分开记录。Preset 只产生 candidate snapshot。

## Release Boundary

Canonical source 包含当前 Docs 与 grouped Skills。Release sidecars 记录机械 Audit、Manifest、Change Report、Composition Review、checksums 和 rollback anchor。模型行为、真实项目迁移和生产运行保持独立 Evidence。
