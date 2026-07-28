# Regression Placement

A defect should be manually discovered once. Place the permanent lesson at the lowest owner that can reliably prevent or expose the same class of failure.

## Candidate owners

```text
type or constructor            eliminate invalid representation
schema decoder                 reject untrusted shape at the boundary
semantic invariant             reject impossible product state
use-case guard                 enforce rule/permission before materialization
transaction/version check      prevent race or stale write
adapter translation            preserve provider failure semantics
resource Scope                 prevent leak or orphan work
architecture/import rule       prevent forbidden dependency
unit/property test             protect pure rule or state space
contract/integration test      protect collaboration boundary
browser/recovery scenario      protect host/user behavior
monitor/alert                  detect production-only condition
command/tool guard             prevent unsafe repeated operation
durable project knowledge      preserve non-executable reason or route
```

## Lowest does not mean smallest file

Choose the earliest owner that can enforce the property without duplicating knowledge. A high-level browser test may still be needed for a browser-only property.

## Avoid duplicate defenses without ownership

Multiple layers may intentionally reinforce a critical invariant, but one should own the meaning. Other checks are derived or defense-in-depth, not peer authorities.

## Test the defense

Introduce the known failure or a mutation to confirm that the new check, test, or monitor actually detects it.

## Remove coincidence fixes

A `sleep`, broad catch, retry loop, cache clear, or forced reload that merely reduces failure probability is not a regression defense unless its causal contract is understood.

## Related knowledge

- Use [Investigation and the first wrong state](investigation-and-first-wrong-state.md) to identify the cause.
- Use [Observation limits](observation-limits.md) to state what the defense proves.
- Use `$product-definition` for product invariants and Quality Boundary.
- Use `$evolvable-application-architecture`, `$frontend-architecture`, or `$effect-best-practices` for the owning implementation layer.
- Return to the [Harness map](../SKILL.md).
