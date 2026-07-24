---
name: ai-coding-os
description: User entrypoint that maps ambiguous or cross-cutting workspace work to the owning AI Coding OS skills.
disable-model-invocation: true
---

# AI Coding OS Router

Use this router as a capability map:

> **Router selects knowledge; agent selects strategy.**

Clear requests go directly to the owning specialist. Ambiguous or cross-cutting
requests use this router to identify the lead, supporting skills, repository
authority, and available Preset or execution surfaces.

## Routing Map

| Concern | Lead | Add when needed |
| --- | --- | --- |
| Docs placement, authority chain, indexes, cleanup | `$docs-governance` | semantic owner of the content |
| AI Coding OS cross-Skill precedence, shared vocabulary or schemas | `$ai-coding-os-suite-contracts` | specialist that owns the affected decision |
| Fact authority, transactions, backend modules, migration | `$evolvable-application-architecture` | frontend, Effect, or harness specialist |
| Monorepo, package promotion, source topology, naming vocabulary | `$evolvable-application-architecture` | `$evolvable-application-preset`, `$docs-governance` |
| Frontend state, feature topology, Query/store/realtime | `$frontend-architecture` | `$ui-product-harness` |
| Effect Service/Layer/Scope/runtime/API | `$effect-best-practices` | surrounding architecture owner |
| Discover, incrementally adopt, or upgrade reusable project defaults | `$evolvable-application-preset` | `$docs-governance` only for docs-home conflicts |
| Generate a managed Effect API slice | `$effect-api-app-kit` | architecture and Effect decisions first |
| Cross-surface harness vocabulary and coverage | `$product-harness-system` | headless or UI specialist |
| Headless command, fixture, replay, DB/restart proof | `$headless-product-harness` | `$evolvable-application-architecture` |
| Component, surface, or browser proof | `$ui-product-harness` | `$frontend-architecture` |
| Concrete frontend test lane | `$frontend-test-system` | `$ui-product-harness` |
| User-facing capability and interaction trace | `$interface-capability-planning` | frontend and harness specialists |
| Durable Goal Pack explicitly selected | `$goal-proof` | any needed specialist |

## Route Procedure

1. **Ground.** Read host instructions, repository `AGENTS.md`, and the nearest
   project authority. Complete when project rules and unresolved authority
   questions are named.
2. **Classify.** Choose the concern whose semantic authority would change.
   Complete when one lead skill is selected; use multiple leads only for truly
   orthogonal decisions.
3. **Compose.** Add specialists only for decision surfaces the lead does not
   own. Complete when every selected skill has a distinct contribution.
4. **Expose surfaces.** Name relevant Preset profiles, generators, checks, and
   harnesses already present. Complete when the implementation path can discover
   available execution surfaces without treating them as authority.
5. **Route or execute.** Return the compact route for an ambiguous request; for
   a clear request, invoke the specialist and continue the work. Complete when
   routing has produced action rather than another planning layer.

## Authority Resolution

Authority is claim-scoped, not one universal total order:

```text
1. host instructions and repository AGENTS.md
2. adopted project authority for the claim:
   current facts        -> docs/ssot/**
   executable rules     -> docs/standards/**
   accepted tradeoffs   -> docs/adr/**
   wire compatibility   -> project protocol/schema contract
3. executable reality for implementation claims:
   source, lockfiles, tests, and command evidence
4. unadopted Preset source or candidate, then specialist doctrine
5. router recommendation
```

An adopted Preset output is a project-owned file resolved through its docs
layer, not a lower-priority Preset object. When project authority and executable
reality disagree, expose the conflict instead of silently selecting one.
Discovery identifies candidates; project authority settles claims.

## Optional Goal Method

Route to `$goal-proof` only when the user selects Goal Proof / Goal Pack or the
repository declares it as the active method for the workstream. Task size alone
does not select it.

## Output

```yaml
classification: <concern>
lead:
  skill: <$skill-name>
  reason: <semantic authority affected>
supporting:
  - skill: <$skill-name>
    reason: <distinct contribution>
project_authorities_to_read:
  - <path>
available_surfaces:
  - <preset/profile/tool/harness>
boundary_notes:
  - <decision outside selected ownership>
```

Keep the route inline. Durable state belongs to the selected method or project.
