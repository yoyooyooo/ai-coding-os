# State Roles and Ownership

> **Projection Is Not Authority. One State Role, One Owner.** Similar values may coexist as intent, proposal, projection, interaction, navigation, or continuity state, but each role needs one accountable owner.

Frontend state becomes difficult when several mechanisms hold similar values without a clear distinction in meaning or lifetime.

## State roles

```text
accepted fact       authoritative product state owned outside the frontend
remote projection   server-derived view cached for display and mutation lifecycle
optimistic proposal local candidate associated with an operation
interaction state   focus, selection, draft, expanded row, transient filter, wizard position
navigation state    URL, route, history, and shareable navigation intent
continuity state    sequence, cursor, dedupe, gap, reconnect, and backfill metadata
view model          pure combination of projection and interaction for one surface
```

Do not call all of these "app state".

## Default owner map

```text
router       URL and navigation authority
query cache  remote projection, freshness, dedupe, mutation lifecycle
local store  local interaction state only
realtime     continuity and projection-update coordination
Effect       execution, dependencies, resources, concurrency, typed failure
React        render tree and user-event adapter
```

Component state remains appropriate for local, short-lived interaction that no other owner needs.

## Server projection is not server truth

A query cache stores a projection. It may be stale, optimistic, invalidated, or incomplete. It should not become an independent business writer.

## Avoid mirrored owners

Common failure:

```text
query cache contains Order
store copies Order
component copies selected Order
a realtime handler mutates both
```

Instead, keep one remote projection owner and store only the local choice or derived view needed by the surface.

## URL state

Use URL/navigation authority for shareable, back/forward-sensitive, bookmarkable state. Do not put ephemeral focus or large unsaved drafts in the URL merely for consistency.

## Derived state

Prefer pure derivation over synchronized copies. If a value can be computed from projection and interaction state, make the relation explicit in a view model or selector.

## Project override

A project may use different libraries. Preserve the role map. Two libraries owning the same semantic state is not a harmless stylistic variation.

## Related knowledge

- Use [Intent, acknowledgement, and reconciliation](intent-acknowledgement-and-reconciliation.md) for optimistic proposals.
- Use [Realtime continuity and reload](realtime-continuity-and-reload.md) for projection updates.
- Use [Default frontend source conventions](default-frontend-source-conventions.md) for `.query.ts`, `.store.ts`, and `.view-model.ts`.
- Use `$evolvable-application-architecture` for final fact authority.
- Return to the [Frontend Architecture map](../SKILL.md).
