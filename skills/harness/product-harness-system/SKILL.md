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

> **Harnesses expose observations; applicable product, fact, policy, and API contract authority gives them meaning.**

## Ownership

```text
Owns:
  shared Harness vocabulary
  scenario and proof-surface discovery
  fixture/fake/replay distinctions
  cross-headless/UI trace and coverage
  empirical Unknown / Probe Request shaping
  descriptive claim ceilings and `does_not_decide` boundaries
  empirical Unknown / Probe Request framing
  harness asset lifecycle

Adjacent Suite owners, when installed:
  Product AC/UAT source semantics -> $product-definition
  InterfaceCapability source -> $interface-capability-planning
  command, persistence, replay, and recovery proof -> $headless-product-harness
  interface, render, and browser proof -> $ui-product-harness
  concrete frontend test lane -> $frontend-test-system
```

Product truth, concrete runners, active execution state, and completion decisions
remain outside this skill.

## Core Model

```text
Product Capability
  -> Harness Scenario
  -> Fixture / Fake / Replay when needed
  -> orthogonal Proof Surface + owner-local test lane
  -> structured observations
  -> supports + does_not_decide + not_proven
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

## Harness Coverage Decisions

Cover applicable decisions in the order exposed by the claim; a proof ladder is a menu, not a project workflow.

| Decision | Completion criterion |
| --- | --- |
| Ground | The bounded product capability, current property, applicable product/fact/API contract authority, and existing descriptors/commands are identified. |
| Discover | Existing proof surfaces are reused where they observe the required property without bypassing production boundaries. |
| Split | Headless, UI, and concrete frontend test lanes are separated only where their semantics differ. |
| Add | The thinnest missing scenario, fixture, fake, replay, driver, probe, or harness exists; empirical Unknowns become bounded Probe Requests and no empty artifact family is generated. |
| Observe | Result output distinguishes `observed`, `supports`, `does_not_decide`, and `not_proven`, and identifies fake/local/real dependencies. |
| Retain | Descriptor, lifecycle, and coverage are persisted only when they improve future discovery or regression use. |

A proof ladder is a menu: select the surface required by the property.

## Descriptor and Result

An empirical Unknown may enter as a Probe Request naming the question, observable boundary, dependency reality, expected observations, decision it can inform, and decisions it cannot make.

A Descriptor makes a scenario discoverable by naming its capability,
`proof_surface.surface_kind`, dependency realities, environment, proof focus,
entrypoint, observable properties, exclusions, and claim ceiling. A Result
records the same Proof Surface plus direct `observed` values, bounded `supports`, explicit `does_not_decide`,
and adjacent `not_proven` claims. Use `$ai-coding-os-suite-contracts` for the
machine schema. Add its direction-neutral Evidence Envelope only when a real
machine consumer or durable cross-owner citation earns it; receivers retain the
claim ceiling and decide their own local sufficiency or classification.

## Empirical Unknowns and Probe Requests

When product and architecture meaning are settled but behavior is unknown, frame
a bounded Probe Request:

```text
question
proof surface and dependency reality
observable values
what the observation may support
what it cannot decide
remaining not_proven
```

A probe may close an empirical unknown. It cannot decide product policy, fact
authority, architecture acceptance, execution completion, or release status.

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
- keeps observation surface, dependency reality, environment, and proof focus orthogonal;
- proves projection continuity rather than transport reconnection alone;
- keeps assertions anchored to existing authority;
- executes the product path before reporting success;
- invalidates retained evidence when relevant surfaces change.

## Output Contract

Return only the harness architecture material needed for the claim:

```text
capability_and_property
scenario_or_descriptor
proof_surface_and_dependency_reality
existing_or_missing_harness_assets
observed / supports / does_not_decide / not_proven shape
claim_ceiling
coverage_and_lifecycle_decisions
trace_refs
```

## Read When Needed

- Defining artifact roles: [Artifact Model](references/artifact-model.md)
- Deciding retention or placement needs: [Lifecycle and Placement](references/lifecycle-and-placement.md)
- Bounding conclusions: [Claim Ceilings](references/claim-ceilings.md)
- Linking capabilities to surfaces: [Trace Contract](references/trace-contract.md)
- Turning empirical Unknowns into bounded probes: [Empirical Unknowns and Probes](references/empirical-unknowns-and-probes.md)
