# Observation Limits

> **Evidence Bounds Claims. Observe Only What You Exercised.** State the exact property, entry, environment, dependency reality, and path before interpreting a pass or failure.

Evidence is trustworthy only when its conditions and claim ceiling are explicit.

## Claim states, not maturity levels

Use ordinary language such as:

```text
observed                  the run produced this result
supports                  the observation supports a bounded property
not observed              the surface did not exercise the property
contradicted              the observation falsified the property
not proven                available evidence is insufficient
```

These are evidence states, not project stages.

## Common overclaims

```text
unit test passed          -> provider integration works
fake passed               -> real dependency works
one browser path passed   -> whole product is accessible
restart test passed       -> all recovery is safe
static imports are clean  -> runtime composition is reachable
all tests passed          -> accepted product outcome is achieved
recent report             -> current authority
```

## State the conditions

A strong observation report identifies:

```text
property
command/path
environment and version
dependency realities
input/data scope
direct observation
strongest supported conclusion
unobserved or uncertain areas
```

No universal evidence envelope is required; preserve the meaning in the project's natural surface.

## Quality Boundary versus claim ceiling

```text
Quality Boundary  what the product must achieve and who can accept residual risk
claim ceiling     what current evidence allows the team to say
```

Weak evidence does not lower the Quality Boundary. Strong evidence does not choose the product goal.

## Negative evidence

A failure can be more informative than a pass when it reveals the exact violated assumption. Preserve counterexamples and first wrong states.

## Repetition and transfer

One successful run may be accidental. Repeat under the relevant state, timing, and dependency variation when the property depends on them. Do not generalize from one model, environment, or provider account without evidence.

## Related knowledge

- Use [Dependency realities](dependency-realities.md) to state what ran.
- Use [Choosing an observation surface](choosing-observation-surface.md) to avoid unnecessary realism.
- Use [Investigation and the first wrong state](investigation-and-first-wrong-state.md) for failures.
- Use `$product-definition` for the Quality Boundary.
- Return to the [Harness map](../SKILL.md).
