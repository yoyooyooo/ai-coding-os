# Ecosystem Projection Authoring Contract

Add an ecosystem projection only when it provides idiomatic, reusable guidance
beyond the generic doctrine.

## Required Sections

```text
1. Trigger and supported versions/toolchain facts
2. Mapping from EAA semantic roles to ecosystem constructs
3. Non-equivalences and common conceptual traps
4. Private/public/compilation/host/deployable promotion surfaces
5. capability contract and implementation-selection choices
6. resource, concurrency, cancellation, and shutdown ownership
7. wire / persistence / domain / provider type boundaries
8. public API and forward-evolution rules
9. composition-root mapping
10. claim-specific verification surfaces
11. eval cases and not-proven boundary
```

## Extension Boundary

The projection may own ecosystem idioms. It may not redefine:

```text
product meaning
fact authority
consistency domain
use-case acceptance semantics
migration policy
claim ceiling
```

Use owner-qualified concepts when contributing to `$architecture-decision-system`.
Do not require a central ADIR or a mandatory project template.

## Promotion to Independent Skill

Keep a projection inside EAA until it has:

```text
independent user intent and routing
substantial language/runtime decisions beyond mapping
its own stable version and compatibility pressure
independent eval corpus
clear non-overlap with EAA
```
