# Workflow, State, and Exceptions

A product workflow is a domain model of work, time, responsibility, and state. It is not an Agent execution workflow and it should not be forced into a linear happy path when reality is concurrent or interruptible.

## Model the work, not the screen sequence

Ask:

```text
what product object is changing
which actor may request each action
what state or precondition allows it
what accepted event or fact transition results
what waits on time, another actor, or an external system
what happens on rejection, timeout, duplicate, cancellation, or partial success
how work resumes after interruption
what makes the lifecycle finally complete
```

Page order may change without changing the product workflow.

## State dimensions

Do not overload one status when independent dimensions exist:

```text
business lifecycle
approval lifecycle
processing/request lifecycle
visibility or permission
retention/archive state
external settlement or reconciliation
```

Separate dimensions when they can change independently or have different owners.

## Transition semantics

A material transition should make visible:

```text
current state
command or event
actor and authority
preconditions
next state or result
side effects
reversibility
failure and recovery behavior
```

This can be prose or a table. Do not require a state-machine artifact for trivial behavior.

## Time

Time is product meaning when it changes rights, availability, escalation, retention, or outcomes. Distinguish:

```text
deadline
expiry
cooldown
SLA target
scheduled activation
effective version
historical event time
processing time
```

Avoid using current clock time implicitly in deep business logic; make the time dependency testable.

## Concurrency and duplicates

Real workflows receive repeated clicks, retries, parallel actors, delayed events, and stale views. Define which actions are idempotent, rejected, merged, version-checked, or reconciled.

## Recovery

Recovery is user-visible product behavior when users can lose work, see an uncertain outcome, or need to continue after failure. Specify what is preserved, what is retried, what needs confirmation, and what is escalated.

## Exceptions reveal the model

An exception is not merely an error message. It often exposes a missing state, role, policy, or ownership boundary. Repeated "special cases" may be a second real workflow.

## Related knowledge

- Use [Product language and model](product-language-and-model.md) to name states and actors.
- Use [Rules, permissions, quality, and metrics](rules-permissions-quality-and-metrics.md) for transition rules and responsibility.
- Use [Interface obligations](interface-obligations.md) for user-visible waiting, failure, and recovery states.
- Use `$evolvable-application-architecture` for authoritative state transitions and idempotency.
- Return to the [Product Definition map](../SKILL.md).
