# Headless Harness Output

Use the shared Harness Result v2 schema when machine interchange is useful.
Keep ordinary local output proportional to the claim.

## Minimum

```text
harness
status
proof_surface
claim_ceiling
observed
supports
not_proven
```

Optional:

```text
command
evidence_refs
artifacts
verification_level
provenance
```

`proof_surface` separates `surface_kind: headless` from fixture/fake/replay/local
or external dependencies, environment class, and a focus such as
`persistence_restart`.

## Observed versus supports

`observed` contains direct values, outputs, statuses, rows, versions, receipts,
or resource diagnostics from the executed path.

`supports` contains bounded conclusions derived by comparing observations with
project fact authority and applicable API/product contracts. Do not hide
inference inside `observed`.

## Cross-system handoff

When an actual machine consumer, durable citation, or repeated cross-owner
handoff needs one shared shape, use the direction-neutral version-2
`$ai-coding-os-suite-contracts` Evidence Envelope. Otherwise cite the Harness
Result directly. The receiver preserves source and claim ceiling, then decides
local sufficiency; Harness `not_proven` never becomes an execution method's
explicit scope exclusion automatically.

## Provenance levels

```text
current local self-verification
  command + result may be enough

cross-Agent/commit or CI reuse
  add commit, scenario/fixture version, lockfile/runtime profile

release/audit/high-risk evidence
  add complete artifact references and immutable provenance
```

A rerun that passes after previous failures should retain instability when it
matters. Do not erase flakiness by printing only the final pass.
