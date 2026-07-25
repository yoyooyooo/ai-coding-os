# Harness Claim Ceilings

A Harness Result supports conclusions only up to the exact Proof Surface it
exercised. The ceiling describes evidence capability; it does not force a
linear ladder.

## Orthogonal axes

```text
surface_kind
  headless | interface_headless | render | browser | external_runtime

dependency_reality
  none | fixture | fake | replay | real_local | real_external

environment_class when material
  isolated | local_process | local_stack | staging | production

proof_focus when material
  owner-local label such as render_wiring, persistence_restart,
  projection_reconciliation, or idempotent_retry
```

Examples:

```yaml
proof_surface:
  surface_kind: browser
  dependency_reality: [fake]
  environment_class: local_stack
  proof_focus: [reload_consistency]
```

```yaml
proof_surface:
  surface_kind: headless
  dependency_reality: [replay, real_local]
  environment_class: local_stack
  proof_focus: [persistence_restart]
```

The first example does not prove backend fact materialization. The second does
not prove browser reachability. A local stack does not prove production auth,
public deployment, or real-provider behavior.

## Reporting

A useful result states:

```text
Proof Surface exercised
direct observations
supported bounded conclusions
not_proven adjacent properties
claim_ceiling
```

Use `$ai-coding-os-suite-contracts` when the machine-readable schema or a
cross-system Evidence Envelope is needed.
