# Proof Surface Contract

Use four orthogonal dimensions when proof information crosses Skill boundaries:

```yaml
proof_surface:
  surface_kind: headless
  dependency_reality:
    - real_local
    - fake
  environment_class: local_stack
  proof_focus:
    - persistence_restart
    - idempotent_retry
```

## Dimensions

- `surface_kind` names where the property was observed: `headless`,
  `interface_headless`, `render`, `browser`, or `external_runtime`.
- `dependency_reality` names every material dependency reality present in the
  path: `fixture`, `fake`, `replay`, `real_local`, or `real_external`. Pure
  static checks use `none`; it cannot be combined with another value.
- `environment_class` locates execution without turning environment proximity
  into an observation surface.
- `proof_focus` carries open owner-local labels such as `render_wiring`,
  `projection_reconciliation`, or `persistence_restart`.

A browser run may still use fake dependencies. A headless run may exercise a
real local database. A typecheck, schema lint, or import-boundary scan can use
`surface_kind: headless`, `dependency_reality: [none]`, and a precise
`proof_focus`. Neither dimension implies the other. Concrete test lanes remain
owned by the relevant testing Skill.

## Legacy Mapping

| Legacy label | Canonical representation |
| --- | --- |
| `interface-headless`, `interface_headless` | `surface_kind: interface_headless` |
| `render-wiring`, `render_wiring` | `surface_kind: render` plus `proof_focus: [render_wiring]` |
| `browser-visible`, `browser_visible` | `surface_kind: browser`; visibility belongs in observations or proof focus |
| `external-runtime`, `external_runtime` | `surface_kind: external_runtime` |
| `production-near`, `production_near` | describe the actual `environment_class` and dependency realities; do not preserve it as a surface |
| `db_backed` | normally `dependency_reality: [real_local]` plus a persistence proof focus; state the actual database in local details |

Migration must not infer dependency reality from a surface label. If legacy
material does not say whether dependencies were fake, replayed, local, or
external, record the gap rather than guessing.
