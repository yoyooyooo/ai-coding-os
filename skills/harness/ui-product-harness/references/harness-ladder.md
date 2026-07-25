# UI Harness Selection

Use the smallest Proof Surface that can honestly observe the current property.
This is a selection menu, not a mandatory sequence.

## `surface_kind: interface_headless`

No full component render. Use for DTO/view-model mapping, event reducers,
optimistic acknowledgement and rollback, cache invalidation/backfill, local
interaction transitions, router state, and realtime decode/dedupe/gap recovery.

Typical focus and ceiling:

```yaml
proof_surface:
  surface_kind: interface_headless
  dependency_reality: [fixture]
  proof_focus: [projection_reconciliation]
```

This does not prove browser reachability or backend materialization.

## `surface_kind: render`

Use `proof_focus: [render_wiring]` for control dispatch, accessible roles and
names, and bounded pending/error/empty/success states.

```yaml
proof_surface:
  surface_kind: render
  dependency_reality: [fake]
  environment_class: local_process
  proof_focus: [render_wiring]
```

This does not prove reload, navigation through a real browser, backend facts, or
visual design approval.

## `surface_kind: browser`

Use a real browser for visible user paths, focus/keyboard, navigation/deep links,
reload, console/network, hydration, responsive spots, and visible recovery.

```yaml
proof_surface:
  surface_kind: browser
  dependency_reality: [fake]
  environment_class: local_stack
  proof_focus: [reload_consistency]
```

A browser surface does not reveal whether the backend or provider is real. Pair
with headless proof before claiming accepted business facts.

## Environment and external runtime

When real local or staged dependencies are required, change
`dependency_reality` and `environment_class`; do not invent a
`production_near` surface. Use `surface_kind: external_runtime` only when the
property is observed at an explicitly opted-in provider, device, or runtime
boundary. Name credentials, irreversible effects, and exclusions.

## Lifecycle

```text
candidate    useful but not a regression gate
accepted     stable enough for implementation guidance
regression   expected CI or release coverage
retired      replaced or intentionally removed with trace updated
```

Promote only when subjects and entrypoints are stable, paired fact proof exists
where needed, and flake risk is acceptable.
