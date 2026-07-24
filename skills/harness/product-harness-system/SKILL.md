---
name: product-harness-system
description: >-
  Product harness architecture for discoverable scenarios,
  fixtures/fakes/replays, proof surfaces, claim ceilings, coverage, and trace
  across headless and UI harnesses. Use when a repository needs shared harness
  vocabulary, lifecycle, or cross-surface verification design.
---

# Product Harness System

Design a harness layer that makes product capabilities runnable, observable,
composable, and discoverable without creating a second product authority.

> **Harnesses expose observations; project authority gives them meaning.**

## Ownership

```text
Owns:
  shared Harness vocabulary
  scenario and proof-surface discovery
  fixture/fake/replay distinctions
  cross-headless/UI trace and coverage
  descriptive claim ceilings
  harness asset lifecycle

Adjacent owners:
  command, DB, replay, recovery proof -> $headless-product-harness
  component and browser proof -> $ui-product-harness
  concrete frontend test lane -> $frontend-test-system
  fact authority -> $evolvable-application-architecture
  docs placement -> $docs-governance
```

Product truth, concrete runners, active execution state, and completion decisions
remain outside this skill.

## Core Model

```text
Product Capability
  -> Harness Scenario
  -> Fixture / Fake / Replay when needed
  -> Headless and/or UI Harness Surface
  -> structured observations
  -> supported conclusion + not_proven
```

The portable Harness vocabulary and Descriptor/Result schemas are provided by
`$ai-coding-os-suite-contracts`. This Skill owns their product-proof semantics;
the contracts Skill makes the machine-readable forms independently discoverable.

```text
fixture  static deterministic input
fake     deterministic behavioral replacement through an explicit proof boundary
replay   recorded normalized input sequence
driver   action issuer through a formal boundary
probe    read-only observer
harness  runnable observation surface
```

Guarded labels such as `mock`, `smoke`, `e2e`, `integration`, or `complete`
carry a boundary and claim ceiling whenever used.

## Harness Pass

| Step | Completion criterion |
| --- | --- |
| Ground | The bounded product capability, current property, project authority, and existing descriptors/commands are identified. |
| Discover | Existing proof surfaces are reused where they observe the required property without bypassing production boundaries. |
| Split | Headless, UI, and concrete frontend test lanes are separated only where their semantics differ. |
| Add | The thinnest missing scenario, fixture, fake, replay, driver, probe, or harness exists; no empty artifact family is generated. |
| Observe | Result output distinguishes `observed`, `supports`, and `not_proven`, and identifies fake/local/real dependencies. |
| Retain | Descriptor, lifecycle, and coverage are persisted only when they improve future discovery or regression use. |

A proof ladder is a menu: select the surface required by the property.

## Descriptor and Result

```yaml
schema_version: 1
id: order.checkout.retry
capability: order.checkout
surface: headless
command: pnpm verify order.checkout.retry
uses:
  persistence: postgres
  external_payment: fake
can_observe:
  - committed order version
  - duplicate retry behavior
does_not_cover:
  - browser projection
  - real payment provider
claim_ceiling: local Postgres; one authority host; restart exercised
```

```yaml
schema_version: 1
harness: order.checkout.retry
status: pass
observed:
  order_version_before: 7
  order_version_after: 8
  duplicate_version_after: 8
supports:
  - duplicate retry produced no second committed transition
not_proven:
  - concurrent multi-process retry
  - real provider behavior
```

Add full provenance when evidence must survive a commit, execution context, CI
run, release decision, or audit.

## Lifecycle and Placement

```text
candidate   useful discovery surface
accepted    stable for normal reuse
regression  expected CI or release coverage
retired     replaced or intentionally removed with trace updated
```

Business-specific harnesses stay near their module or feature. Cross-host,
business-neutral primitives may enter an admitted testkit package. Generic
discovery tooling belongs under `tooling/verification`; an independent app is
justified only by a real host lifecycle.

Project docs placement is governed by `$docs-governance`.

## False-Proof Audit

Check that the harness:

- reaches the formal use case instead of a privileged DB writer;
- reuses product policy rather than copying a second algorithm;
- labels fake, replay, local, browser, and external surfaces accurately;
- proves projection continuity rather than transport reconnection alone;
- keeps assertions anchored to existing authority;
- executes the product path before reporting success;
- invalidates retained evidence when relevant surfaces change.

## Read When Needed

- Defining artifact roles: [Artifact Model](references/artifact-model.md)
- Deciding retention or placement needs: [Lifecycle and Placement](references/lifecycle-and-placement.md)
- Bounding conclusions: [Claim Ceilings](references/claim-ceilings.md)
- Linking capabilities to surfaces: [Trace Contract](references/trace-contract.md)
