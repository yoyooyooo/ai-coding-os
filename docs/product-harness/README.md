# Product Harness

本层保存项目级 Harness proof contract：怎样观察一个产品属性、claim ceiling 到哪里、coverage 与 gaps 如何被长期发现。

## Owns

- `HarnessScenario` 语义级 proof story。
- Fixture/fake/replay、route/component 和 Evidence artifact refs。
- Proof Surface、`claim_ceiling`、`not_claimed`、`not_proven` 和 Harness Coverage Matrix。
- Harness lifecycle：`candidate | accepted | regression | retired`。
- 从任意 source、proposal 或 execution method 显式 promote 的稳定 proof contract。

## Must Not Own

- Product/domain Authority、API schema、数据库事实或 InterfaceCapability 语义。
- 最终 UX/UI/IA/visual design。
- 可执行测试代码、fixture data、Playwright script 或 raw run output。
- Tracker、ticket、Goal、release 或其他 execution state/completion。

## Boundary

Harness 通过 ID 引用 capability，不重新定义用户能力：

```yaml
kind: HarnessScenario
id: hs.channel.issue-from-message
covers:
  interface_capability: ic.channel.issue-from-message
proof_surface:
  surface_kind: browser
  dependency_reality:
    - real_local
claim_ceiling: one browser-visible local-stack path
not_claimed:
  - final visual approval
  - backend fact correctness without paired headless proof
not_proven: []
```

## Evidence Policy

```text
raw observations and run artifacts -> owning test/Harness/CI/report surface
selected execution status          -> selected workflow owner
project-level proof contract        -> docs/product-harness/**
```

Evidence links preserve source and claim ceiling. Pure static proof uses `dependency_reality: [none]` and never mixes `none` with runtime dependencies. A passing run or completed ticket does not automatically accept this contract, Product intent, InterfaceCapability definition lifecycle, documentation lifecycle, or release status.

## Promotion / Demotion

Candidate proof material enters this layer only after documentation Authority accepts its durable discovery/regression value. Promotion keeps source/Evidence refs and drops workflow-specific state.

One-off proof, replaced coverage, stale claim ceilings, and retired routes remain source/report evidence or are removed after retention review. The layer keeps one current proof contract per meaning.

## Conflict

Product/SSoT define meaning; InterfaceCapability defines user-facing projection; this layer defines proof contract; executable Evidence can prove the contract stale. Resolve by question rather than a universal order.

## Routes

- Interface Capability：`../interface-capabilities/README.md`
- 文档网络：`../README.md`
- 当前事实：`../ssot/README.md`
- 文档治理：`../standards/docs-governance.md`
