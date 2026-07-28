# Scope, Prototype, Tracer, and Estimation

> **Prototype Learns; Tracer Grows.** Keep disposable inquiry, retained end-to-end structure, current scope, and future possibility visibly distinct.

Scope and exploratory intent must remain explicit so that thin work is not mistaken for complete product capability.

## Scope surfaces

```text
current accepted scope   behavior the product is committed to now
explicit non-goals       behavior intentionally excluded
future candidate         possible later behavior not yet accepted
legacy behavior retained behavior temporarily preserved during transition
retirement target        behavior intended to disappear under stated conditions
```

Do not use version labels as a substitute for stating the actual semantic difference.

## Work intent

### Prototype: explore and discard

A Prototype exists to answer a small number of high-risk questions. State:

```text
what question it answers
what it intentionally does not validate
what data or dependencies are fake
what learning is retained
what code or artifact is discarded
```

A polished interface does not make it production-ready.

### Tracer: retain and grow

A Tracer is a thin but real end-to-end path through intended architecture and runtime constraints. It should have production-quality boundaries, failure handling appropriate to the slice, and a repeatable observation route.

### Operate and maintain

A capability intended for ongoing use must own real data, permissions, failure, recovery, observability, and maintenance obligations. This is not merely "a more complete prototype".

## MVP

MVP is a product-learning boundary: the smallest product that can test a value hypothesis with real users. It may use a Tracer implementation, but commercial learning and architecture learning are different questions.

## Estimation

An estimate is a model, not a promise. Make visible:

```text
scope and exclusions
assumptions
critical dependencies
uncertain parameters
range or scenarios
confidence and decision use
what thin slice will calibrate the model
```

AI may reduce local coding time without reducing product clarification, integration, verification, security, rollout, or organizational decision time.

## Feedback horizon

Break work where the next observation can still change direction cheaply. Small steps describe the relationship between action and feedback, not a fixed file count or duration.

## Related knowledge

- Use [Learning from sources and reality](learning-from-sources-and-reality.md) to revise scope from evidence.
- Use [Outcome and accepted meaning](outcome-and-accepted-meaning.md) to decide what the slice must preserve.
- Use `$product-harness-system` to choose the Tracer or Prototype observation surface.
- Use `$evolvable-application-architecture` for gradual replacement and takeover.
- Return to the [Product Definition map](../SKILL.md).
