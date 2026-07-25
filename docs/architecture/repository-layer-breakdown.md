# AI Coding OS Repository Ownership Map

```yaml
status: current-architecture-view
scope: repository layout, ownership, verification, and distribution
not_authority_over:
  - docs/ssot/**
  - docs/standards/**
  - docs/adr/**
  - source and executable evidence
  - external or experimental execution state
```

本视图帮助 Agent 判断文件归属和 change propagation。Repository nodes 是并列 owner，不是 public shell 到 execution 的流水线。

## Core Skill Suite

```text
skills/**
```

| Node | Owns | Must Not Own |
| --- | --- | --- |
| `router` | user-invoked knowledge Owner Map | durable artifact、workflow、model orchestration |
| `contracts` | portable knowledge kernel、Proof Surface、Evidence Envelope、eval/Harness schemas | static roster、project product vocabulary、execution lifecycle |
| `governance` | documentation Authority、Routes、Earned Shape、cleanup、audit | product truth、tracker state |
| `product` | product framing、model、decision、requirements、acceptance | docs placement、technical design、delivery evidence |
| `architecture` | application/frontend/Effect doctrine | product facts、execution status |
| `capability` | interface capability、surface、state/data ownership、proof needs | product truth、test runner |
| `harness` | proof architecture、headless/UI observation、frontend lane | business semantics、execution completion |
| `preset` | reusable defaults、incremental adoption guidance、explicit `candidate-snapshot`、managed upgrade candidate | accepted/current project claims、project facts、empty Docs layers、dynamic inheritance |
| `tooling` | deterministic generation、targeted contract negatives、bounded audit、source-bound self-contained core bundle | unsettled product/architecture decisions |

Core Skills may compose through bounded decision edges. They do not form one mandatory pipeline.

## Project Knowledge Network

```text
docs/product/**
docs/ssot/**
docs/standards/**
docs/adr/**
docs/architecture/**
docs/roadmap/**
docs/review-plan/**
docs/interface-capabilities/**
docs/product-harness/**
```

| Layer | Authority role |
| --- | --- |
| Product | product/method positioning |
| SSoT | current terms, facts, invariants, owner boundaries |
| Standards | executable rules and quality gates |
| ADR | accepted technical tradeoffs and reasons |
| Architecture | current structure、runtime views、technical fact writers 与 consistency boundaries |
| Roadmap | future sequence, gates, Evidence links |
| Review Plan | review ledger/evidence, not adopted Authority by itself |
| Interface Capabilities | project interface trace |
| Product Harness | project proof contract and coverage |

`docs/README.md` and layer READMEs are multi-entry routers. Source paths, tests,
ADRs, schemas, Harness Results, and direct artifact links are equally valid
entry surfaces.

## Co-located Goal Proof Experiment

```text
experiments/goal-proof/skill/**
experiments/goal-proof/dogfood/**
packages/cli/**
```

The experiment owns its Goal Pack state protocol and CLI behavior. It is outside
Core Suite membership, Router branches, core Evidence lifecycle, and core ZIP.
Historical dogfood evidence remains append-only and may contain superseded paths.

Repository checks keep claims separate:

```text
check:core                  core Skill source + project docs
check:goal-proof-experiment experiment Skill + CLI
check                       aggregate repo health only
```

## Verification And Distribution

```text
skills/VERSION                       bundle-local Core version
skills/tooling/suite_audit.py         core source/schema/eval/golden/provenance audit
skills/tooling/build_suite_release.py source-bound core-only deterministic ZIP + manifest
skills/governance/docs-governance/scripts/** project docs audit
experiments/goal-proof/scripts/**   experiment Skill self-check
scripts/**                          npm release support
```

The Core ZIP contains only `skills/**`; `skills/VERSION`、bundle-local README、audit 和 builder 使其可在干净解压目录自检，`source_tree_sha256` 将 canonical audit 绑定到打包源码。Builder 将 canonical audit、manifest、change report 与 composition review 作为同目录 versioned sidecars 输出，并在 provenance hash 前规范化机器绝对路径与 compiler-dependent diagnostics。npm package 发布 Goal Proof CLI；Core 与 CLI 版本独立，任一通过都不建立另一 surface 的 claim。

## Change Propagation

| Changed meaning | Required neighboring checks |
| --- | --- |
| Core Skill name/invocation/owner | Core index, Router, contracts, evals, Suite audit, public docs |
| Docs governance/network rule | Docs Skill/reference/template/scanner/tests, project Standards and routers |
| Preset generated surface | Preset Skill/profile/renderer/schema/eval/golden、candidate claim 与 Suite audit |
| Shared Proof/Evidence contract | Contract schema/examples/evals、targeted negative cases、Harness consumers、migration note |
| Goal experiment schema/CLI | Experiment Skill/templates/self-check, CLI docs/tests; no Core roster update |
| Core/Experiment distribution | release builder, package docs, manifest assertions, README/ADR |

## Routes

- Architecture index：[README.md](README.md)
- SSoT：[../ssot/README.md](../ssot/README.md)
- Standards：[../standards/README.md](../standards/README.md)
- Core Skills：[../../skills/README.md](../../skills/README.md)
- Experiment：[../../experiments/goal-proof/README.md](../../experiments/goal-proof/README.md)
