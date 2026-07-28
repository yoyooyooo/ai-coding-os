# Outcome and Accepted Meaning

> **Outcome Before Requested Means.** A feature request is a proposed intervention; the product question is which user outcome should improve and how success is recognized.

A requested feature is often a proposed means. Product definition begins by identifying the result the user or organization is trying to achieve and the conditions under which that result counts as success.

## Reframe the request

```text
requested feature  -> what work is the user trying to complete?
current pain        -> what prevents or degrades that work?
expected outcome    -> what should become easier, safer, faster, or more reliable?
success boundary    -> how will the user and accountable owner know it worked?
```

A request for an Excel export may really be a need to distribute exceptions and track resolution. A request for an AI summary may really be a need to make a high-risk decision with traceable evidence.

## Accepted meaning

Accepted meaning is the current product model approved by the accountable owner. It may be expressed in a capability document, product decision, SSoT term, acceptance scenario, or another project-owned surface.

It is not automatically created by:

```text
a stakeholder statement in isolation
legacy behavior
an implementation shortcut
a prototype or demo
one user session
one test or runtime observation
```

Those are inputs to learning.

## Outcome layers

Keep the following levels distinct:

```text
business outcome   the broader result the organization seeks
user outcome       what the user can accomplish or avoid
product capability the durable ability the system provides
feature/interface  one possible product expression
implementation     the current technical mechanism
```

A lower layer may change while the upper outcome remains stable.

## Quality Boundary

"Good enough" is an accepted boundary, not a developer excuse. Define:

```text
what must never fail or be lost
what roughness is temporarily acceptable
what performance, accessibility, privacy, safety, and reliability floors apply
who can accept residual risk
what feedback would justify more investment
```

Evidence can show whether a property was observed. It cannot lower the Quality Boundary by itself.

## Non-goals

Explicit non-goals protect focus and prevent a thin slice from being interpreted as a universal commitment. State the user-visible or semantic exclusion, not every implementation detail that happens to be absent.

## Stop condition

Stop speculative refinement when additional work no longer materially reduces known risk, satisfies an accepted need, or accelerates learning. Shipping enters a new feedback stage; it does not end responsibility.

## Related knowledge

- Use [Learning from sources and reality](learning-from-sources-and-reality.md) when inputs disagree.
- Use [Rules, permissions, quality, and metrics](rules-permissions-quality-and-metrics.md) to make the Quality Boundary concrete.
- Use [Default product knowledge shape](default-product-knowledge-shape.md) for a portable documentation home.
- Use `$product-harness-system` when the outcome requires runtime evidence.
- Return to the [Product Definition map](../SKILL.md).
