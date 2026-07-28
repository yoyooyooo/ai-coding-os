# Reading and Taking Over Existing Systems

Takeover begins by recovering the current system's behavior and authority, not by projecting a preferred architecture onto unfamiliar code.

## Read from real entry points

Start from one meaningful capability or failure:

```text
user/API entry
formal use case or hidden orchestration
fact writer and storage
external capabilities
background work and host composition
frontend projection when applicable
run/test/reproduction surface
```

This is a reading lens, not a required audit sequence.

## Classify what you find

```text
accepted behavior       intentionally supported product meaning
accidental behavior     current implementation with no accepted obligation
legacy contract         compatibility users still rely on
prototype scaffold      disposable learning code
Tracer skeleton         thin real path worth retaining
operational necessity   mechanism required by actual runtime constraints
unknown                 behavior or dependency not yet explained
```

Do not preserve all source as architecture merely because it is deployed.

## AI-generated MVP and POC signals

- polished UI with fake or local-only data;
- direct transport-to-database writes;
- provider calls spread through components or handlers;
- authorization expressed as hidden buttons;
- no operation identity, recovery, or restart behavior;
- generated folders and abstractions with no independent pressure;
- no stable command to reproduce core behavior;
- tests that verify snapshots but not product invariants.

## Preserve and re-earn

Preserve:

```text
accepted product meaning
real data and identity
public compatibility
critical invariants
valuable tests and observations
useful names and domain knowledge
```

Re-earn:

```text
packages, Services, Layers, registries, templates, generators
provider abstractions
state stores and event systems
host/deployment topology
```

## Establish a first Tracer

When the system is too tangled to change safely, recover or build one thin real path with explicit fact authority, external capability, host lifetime, and verification. Use it to grow the replacement and expose migration boundaries.

## Record uncertainty honestly

Do not fill missing explanations with generic best practice. Mark what is known from source, what is observed, what is inferred, and what still needs product or runtime evidence.

## Related knowledge

- Use [Agent-legible change surface](agent-legible-change-surface.md) as the target project property.
- Use [Forward evolution and migration](forward-evolution-and-migration.md) to replace without a flag day.
- Use [Causal diagnosis and the first wrong state](causal-diagnosis-and-first-wrong-state.md) for live failures.
- Use [Scenario examples](scenario-examples.md) for takeover mappings.
- Use `$product-definition` to distinguish accepted meaning from current behavior.
- Return to the [EAA map](../SKILL.md).
