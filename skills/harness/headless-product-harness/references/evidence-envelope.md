# Headless Harness Output

Use the shared Harness Result schema when machine interchange is useful. Keep
ordinary local output lightweight.

## Minimum

```text
harness
status
observed
supports
not_proven
```

Optional:

```text
command
environment
artifacts
claim_ceiling
provenance
```

## Observed versus supports

`observed` contains direct values, outputs, statuses, rows, versions, receipts,
or resource diagnostics from the executed path.

`supports` contains bounded conclusions the Agent derives by comparing those
observations with project authority and contracts.

Do not hide inference inside `observed`.

## Provenance levels

```text
current local self-verification
  command + environment + result may be enough

cross-Agent/commit or CI reuse
  add commit, scenario/fixture version, lockfile/runtime profile

release/audit/high-risk evidence
  add complete artifact references and immutable provenance
```

A rerun that passes after previous failures should retain the instability when
it matters. Do not erase evidence of flakiness by printing only the final pass.
