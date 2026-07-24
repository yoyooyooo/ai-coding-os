# Client Contract Evolution

Wire contracts, feature projections, and view models have different lifecycles.
Keep them distinct so backend and frontend can evolve without permanent DTO
mirrors.

## Layers

```text
wire schema / generated client contract
  -> decoded transport value
  -> feature projection/model
  -> view model
  -> surface
```

Generated contracts may be replaced. Feature projection and view-model naming
should follow product language rather than transport field layout.

## Change classification

```text
additive
  optional field, new endpoint, compatible event variant

behavioral
  same shape but different meaning, ordering, auth, retry, or completion semantics

breaking
  removed/renamed required field, narrowed enum, protocol/version change
```

Behavioral changes deserve the same care as shape-breaking changes.

## Long-lived clients

For browsers, desktop clients, offline workers, or cached tabs, plan a bounded
overlap when needed:

```text
server supports old/new read shape
client understands unknown enum/event fallback
new client stops producing old writes
telemetry proves old callers are gone
old shape is removed with deletion evidence
```

Avoid indefinite dual writes or silent fallback.

## Frontend migration

```text
characterize current behavior
-> add decoder/mapper compatibility at the edge
-> keep one feature projection owner
-> migrate query/realtime readers
-> stop new writes to old local mirrors
-> delete obsolete DTO/view state
```

## Evidence

Use the smallest relevant surface:

```text
schema/client compile
mapper test
query/store/realtime headless test
render wiring
browser path with real backend when required
```

Do not claim backend fact correctness from a frontend mock, or browser
continuity from a reducer-only test.
