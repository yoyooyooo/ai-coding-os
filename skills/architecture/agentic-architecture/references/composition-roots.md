# Composition Roots

A composition root assembles the system for a profile. It chooses adapters,
config, resource lifetimes, credentials, observability, and deployment-specific
policy. It should not own product facts or business rules.

## Good Responsibilities

Composition roots may own:

- selecting concrete adapter implementations;
- constructing dependency graphs;
- loading config and feature flags;
- binding runtime resources;
- wiring observability;
- selecting fake/replay/real profiles;
- starting servers, workers, CLIs, or daemons;
- applying deployment-only policy knobs.

## Forbidden Responsibilities

Composition roots should not own:

- domain object lifecycle;
- application-service business rules;
- permission decisions;
- memory acceptance;
- event-spine writes outside application services;
- route-specific product semantics;
- test-only shortcuts that become production behavior;
- provider/runtime semantics that leak into domain terms.

## Profile Model

Use one core with multiple profiles:

```text
core domain/application
  -> local profile
  -> cloud profile
  -> desktop profile
  -> test fake profile
  -> replay profile
  -> real-runtime opt-in profile
```

Profile differences should be visible in wiring and evidence, not hidden inside
domain code.

## Signs The Root Is Too Thick

- the binary/server/worker contains domain branching;
- tests need to duplicate production wiring manually;
- adapter-private errors change product behavior directly;
- deployment profile choice changes object authority;
- local and cloud paths have separate business semantics;
- adding a new provider requires touching unrelated domain objects.

## Split Guidance

Split a composition root when:

- two profiles have different deployment concerns but the same core;
- a daemon/relay/server/worker owns transport or supervision mechanics that
  should not leak into product facts;
- local package mode should not pull remote transport or cloud-only crates;
- test/fake/replay profile needs stable wiring for harness proof.

Do not split merely to satisfy a diagram. Split when it reduces authority
confusion, dependency inversion, profile leakage, or verification cost.
