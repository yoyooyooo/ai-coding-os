# Frontend Adapter

This is the minimum frontend mapping for users who installed only this skill.
For directory topology, React, Query/store/realtime, naming, host composition,
and frontend harness rules, use `$frontend-architecture` when available.

## Baseline Mapping

```text
user intent
  -> frontend command adapter
  -> application authority

committed fact
  -> query or realtime projection
  -> decoder / mapper / cache
  -> view model and component
```

Frontend normally owns local interaction state, navigation, drafts, optimistic
proposals, cached projections, and resource status. It normally does not own
accepted business completion, durable permissions, audit history, settlement,
or server workflow truth.

Keep commands, queries, and realtime conceptually separate. A websocket frame,
provider event, or optimistic echo is not an accepted business fact. Reconcile
optimistic proposals with mutation IDs and authoritative projections; on gaps or
shape uncertainty, backfill rather than invent truth.

For offline-first or CRDT collaboration, the client may participate in a
declared merge authority. That does not make every UI store authoritative.
Preserve operation identity, membership/epoch, admission, and business-state
boundaries.

Create live/fake/replay clients and resource lifecycles at the host/app
composition boundary. Features consume capabilities; components do not
construct transport SDKs, live runtimes, or credentials.

A frontend client spanning unrelated product capabilities can become a god
object. Split it only when independent ownership, testing, replacement, or
lifecycle pressure exists; do not create dozens of interfaces for symmetry.
