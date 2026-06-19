# Composition Roots

A composition root assembles one deployment profile. It selects concrete
adapters, resource lifetimes, credentials, configuration, observability, and
profile-specific policy knobs.

## Responsibilities

Composition roots may:

- instantiate adapters and clients;
- register capabilities and manifests;
- construct application modules and facades;
- bind clocks, IDs, transaction factories, and event publishers;
- load configuration and secrets;
- start servers, workers, daemons, CLIs, or frontend runtimes;
- select fake, replay, local, hosted, or real-provider profiles.

They must not own product transitions, permission decisions, accepted memory,
business completion, or direct event-spine writes.

## One Core, Multiple Profiles

```text
core application and authority cells
  -> local standalone
  -> server / worker
  -> desktop / daemon
  -> hosted / cloud
  -> test fake
  -> deterministic replay
  -> real provider/runtime opt-in
```

Profile changes alter assembly and evidence, not fact authority.

## Keep Vendor Enumeration Out of Core Libraries

A reusable daemon, server, or application library should not need an enum and a
match statement for every provider. Prefer registrations, factories, manifests,
or profile-specific constructors in the executable/bootstrap layer.

Adding an adapter should ideally require:

```text
new adapter implementation
+ profile registration
+ conformance evidence
```

It should not require unrelated domain edits.

## Registries

A registry is appropriate when implementations are selected dynamically. Keep
selection policy explicit and separate from the adapter collection.

State:

- whether unknown IDs reject or fall back;
- whether aliases are explicit;
- how capability snapshots are validated;
- who owns adapter lifecycle and concurrency;
- whether registrations are static, configured, or remotely discovered.

## Signs of a Thick Root

- business branching in `main`, server setup, or frontend bootstrap;
- vendor errors directly change product transitions;
- tests duplicate production wiring by hand;
- local and hosted profiles implement different product semantics;
- a profile imports adapters it cannot use;
- configuration or environment reads appear inside domain logic.

Use reusable profile builders for tests and production, but keep fixture-only
fact creation outside the public product API.
