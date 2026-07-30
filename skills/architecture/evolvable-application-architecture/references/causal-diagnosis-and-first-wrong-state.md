# Causal Diagnosis and the First Wrong State

_Architecture-specific lens._

Use `$product-harness-system` to preserve the original failure, build a reproducible observation, reduce the search space, and place regression evidence. This reference adds the architecture-specific question:

> At which fact-authority, use-case, capability, consistency, composition, or migration boundary did the observed path first diverge from the accepted contract?

## Start from observed reality

Do not redesign from the final symptom alone. Carry forward the Harness observation:

```text
exact command or user path
input and operation identity
environment, dependency, version, and configuration reality
full error/Cause/trace and timing
relevant state before and after
reproduction limits
```

A fluent architecture explanation is still a hypothesis until the path supports it.

## Follow the application change path

```text
intent
  -> transport decode
  -> governed use-case precondition
  -> authoritative state read
  -> policy/invariant decision
  -> application-owned capability
  -> consistency boundary and materialization
  -> event/projection
  -> user-visible result
```

Locate the first point where actual state, authority, dependency, or lifetime diverges from the accepted contract.

## Architecture-specific causes

- two writers believe they own the same accepted fact;
- a candidate, cache, import, projection, or provider result is treated as authority;
- a use case bypasses authorization, invariant, or commit ownership;
- provider failure or unknown outcome is translated into the wrong product Outcome;
- a transaction boundary is named by a module but cannot contain all invariant participants;
- Port and live/provider details collapse into one dependency surface;
- parallel Port and Service contracts drift for the same capability;
- a resource outlives its host, is created twice, or is rebuilt inside ordinary work;
- a retry duplicates an effect after unknown outcome;
- realtime ordering or gap behavior corrupts a projection;
- a compatibility bridge silently becomes the permanent path;
- an old document, stale Skill snapshot, or generic name routes work to the wrong Owner.

## Architecture repair placement

Once the cause is observed, place the semantic repair at the lowest architecture Owner that can keep it true:

```text
fact-authority boundary
use-case guard or Outcome
consistency scope / database constraint
application Port or adapter translation
composition root / resource Scope
public surface or import rule
migration fence and deletion condition
project knowledge route
```

The permanent executable defense may still belong to a type, decoder, test, probe, or monitor. Use `$product-harness-system` to choose and verify that regression layer.

## Related knowledge

- Use [Agent-legible change surface](agent-legible-change-surface.md) to expose causal routes.
- Use [Fact authority and candidate boundaries](fact-authority-and-candidate-boundaries.md) for writer/candidate mistakes.
- Use [Use cases, transactions, and idempotency](use-cases-transactions-and-idempotency.md) for write, replay, and unknown-outcome failures.
- Use [Capability boundaries and adapters](capability-boundaries-and-adapters.md) for provider translation.
- Use [Composition roots and lifetimes](composition-roots-and-lifetimes.md) for leaks and duplicate resources.
- Use [Forward evolution and migration](forward-evolution-and-migration.md) for bridge and fencing failures.
- Use `$product-harness-system` for general investigation mechanics, reproduction, and regression placement.
- Use `$docs-governance` when stale knowledge caused the wrong change path.
- Return to the [EAA map](../SKILL.md).
