# Causal Diagnosis and the First Wrong State

Architecture diagnosis should locate the earliest boundary where the system's state or assumption became wrong. Repairing only the final symptom leaves the cause free to reappear elsewhere.

## Separate observation and hypothesis

```text
Observation  directly captured input, state, error, timing, or output
Hypothesis   a causal explanation that can still be disproved
Finding      a hypothesis supported strongly enough to change the design
Decision     an accepted action and its owner
```

Fluent explanation is not evidence.

## Preserve the original failure

Before editing, capture:

```text
exact command or user path
input and operation identity
environment and dependency reality
version/commit/configuration
full error, Cause, stack, trace, or screenshot
exit status and timing
relevant state before and after
```

## Follow the causal chain

Typical change path:

```text
intent
  -> transport decode
  -> use-case precondition
  -> authoritative state read
  -> policy/invariant decision
  -> external capability
  -> materialization
  -> event/projection
  -> user-visible result
```

Look for the first point where actual state diverges from the accepted contract.

## Binary reduction

Reduce one dimension at a time:

```text
input set
commit range
call stack
service chain
concurrent actor set
configuration difference
real versus fake dependency
```

A repeatable failure turns guessing into experiments.

## Common architecture causes

- two writers believe they own the same fact;
- a candidate or cache is read as authoritative;
- provider failure is translated into the wrong product outcome;
- a resource outlives its host or is created twice;
- a retry duplicates an effect after unknown outcome;
- realtime ordering or gap behavior corrupts a projection;
- a compatibility bridge silently becomes the permanent path;
- an old document or generic name routes work to the wrong owner.

## Repair placement

After finding the cause, place the permanent defense at the lowest reliable owner:

```text
type or constructor
schema decoder
semantic invariant
use-case guard
transaction or version check
adapter translation
resource Scope
architecture import rule
test, monitor, or command
project knowledge route
```

## Related knowledge

- Use [Agent-legible change surface](agent-legible-change-surface.md) to expose causal routes.
- Use [Use cases, transactions, and idempotency](use-cases-transactions-and-idempotency.md) for write failures.
- Use [Composition roots and lifetimes](composition-roots-and-lifetimes.md) for leaks and duplicate resources.
- Use `$product-harness-system` for investigation mechanics and regression placement.
- Use `$docs-governance` when stale knowledge caused the wrong change path.
- Return to the [EAA map](../SKILL.md).
