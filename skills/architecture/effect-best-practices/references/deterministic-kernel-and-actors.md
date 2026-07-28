# Deterministic Kernel and Actors

A pure deterministic kernel plus an Effect interpreter is a conditional pattern for long-lived state machines, replay, event reasoning, or mailbox-owned state. It is not the default shape for every Effect application.

## Candidate shape

```text
State + Command/Event
  -> pure transition
  -> new State + Decisions/Effects
  -> Effect interpreter performs external capabilities
  -> accepted results feed back as events
```

The kernel owns domain transition logic. The interpreter owns execution, resources, retries, and external failures.

## When it is useful

```text
one identity owns long-lived mutable state
legal transitions are central to correctness
replay or deterministic simulation matters
property/model-based testing has high value
concurrency should be serialized through a mailbox
external effects must remain outside the transition core
```

## When it is excessive

- ordinary request/response CRUD with simple transactions;
- pure transformations already easy to test;
- state has no durable identity or lifecycle;
- the pattern creates an event language more complex than the product.

## Actor discipline

An Actor has private state and processes messages serially. Other components send requests; they do not read or mutate internal state directly.

Define:

```text
mailbox capacity and ordering
message identity and duplicates
reply/timeout semantics
supervision and restart
state persistence/recovery
shutdown
```

## External effects

The transition may emit decisions such as `ChargePayment` or `PersistEvent`. The interpreter executes them. Unknown outcomes return as explicit events rather than being guessed by the kernel.

## Testing

Test the pure transition with examples and properties. Test the interpreter with capability fakes/replays and focused integration. Test restart and mailbox behavior in a Harness.

## Related knowledge

- Use [Structured concurrency, Queue, and Stream](structured-concurrency-queue-stream.md) for mailbox mechanics.
- Use [Errors, interruption, and unknown outcomes](errors-interruption-and-unknown-outcomes.md) for effect results.
- Use `$evolvable-application-architecture` for state authority and events.
- Use `$product-harness-system` for restart/replay observation.
- Return to the [Effect map](../SKILL.md).
