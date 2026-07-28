# Rules, Permissions, Quality, and Metrics

> **Quality Boundary Is Not Claim Ceiling.** Product and risk authority define the required floor; observation only limits what can currently be claimed about that floor.

Rules and quality are part of product meaning. They should not remain hidden in UI conditions, scattered code, or vague adjectives.

## Rule structure

A durable rule may need:

```text
subject and scope
trigger or condition
required or forbidden behavior
exceptions
priority when rules conflict
effective version or time
accountable owner
observable result
```

Keep the expression as simple as the rule allows. A rule catalog is conditional, not a default artifact.

## Semantic invariant, policy, configuration

### Semantic invariant

A property whose violation changes the meaning of the product, for example:

```text
the same payment operation must not create two charges
an unapproved investigation cannot be presented as an accepted finding
an archived record remains historically attributable
```

### Policy

A changeable accountable choice such as threshold, approval tier, retention period, or regional exception. Policy should have an owner, scope, and effective version.

### Operational configuration

Deployment and runtime choices such as endpoints, capacity, log level, or feature exposure. Configuration must not silently redefine invariant or policy.

## Permission is more than visibility

Model separately:

```text
may discover that the object exists
may view which fields
may perform which action
may approve or accept risk
may delegate
may act only under a condition or time window
may retrieve historical versions
```

Hiding a button is not authorization.

## Responsibility roles

Use role distinctions only when they change decisions:

```text
Semantic Owner  decides what the product means
Execution Owner implements or operates the change
Evidence Owner  produces or interprets evidence
Risk Owner      can accept residual business/safety/privacy/operational risk
```

These need not become a central registry.

## Quality Boundary

Translate vague quality into observable conditions:

```text
correctness and data-loss floor
latency/throughput conditions and percentile
availability and recovery expectations
accessibility behavior
privacy and retention constraints
security and abuse resistance
explainability, auditability, or human appeal
allowed roughness and its expiration condition
```

## Metrics

A metric is useful only when its definition, population, time window, owner, and decision use are clear. Distinguish:

```text
outcome metric    whether the user or business result improved
health metric     whether the capability operates reliably
guardrail metric  whether improvement causes unacceptable harm
activity metric   work performed, often weak evidence of value
```

Avoid turning a proxy into the product goal.

## Related knowledge

- Use [Outcome and accepted meaning](outcome-and-accepted-meaning.md) for success and Quality Boundary.
- Use [Workflow, state, and exceptions](workflow-state-and-exceptions.md) for transition conditions.
- Use [Decision boundaries and responsibility](decision-boundaries-and-responsibility.md) for risk acceptance.
- Use `$product-harness-system` to observe quality properties.
- Return to the [Product Definition map](../SKILL.md).
