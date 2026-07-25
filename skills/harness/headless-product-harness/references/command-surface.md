# Command Surface

Use this reference when naming or auditing a headless product command surface.

## Naming

Prefer bounded capability names:

```text
pnpm verify boundary.imports
pnpm verify source.inventory
pnpm verify order.offline-import
cargo run -p xtask -- verify order.checkout.replay
just verify-channel-realtime-gap-recovery
```

Avoid progress labels or vague proof labels as primary names:

```text
smoke-mvp-0-1
phase-2-complete
current-status
smoke-all
```

A compatibility alias may remain when it delegates to a durable semantic
command and does not widen the reported conclusion.

## Command contract

For each stable command, make these properties discoverable in code, help text,
or a Harness Descriptor:

```text
name:
capability:
formal_entry_or_authority_used:
input:
output_format:
can_observe:
does_not_cover:
failure_codes:
default_ci:
opt_in_environment:
```

A run result should use:

```text
observed:
supports:
not_proven:
```

## Parameter rules

- Name parameters by semantic role, not internal type.
- Keep established names stable: `--source`, `--profile`, `--out`, `--format`,
  and `--limit` when those roles really exist.
- `--out` may write artifacts; stdout should still preserve the machine result
  when it is a command contract.
- A sampling `--limit` must not silently change a complete claim into a sampled
  claim.
- Common Agent paths must not depend on hidden process-global state.
- Failure uses a non-zero exit code and names the first useful boundary.

## Review questions

- Can a new Agent infer the capability and exercised surface from the name?
- Does the command drive the same formal path as production rather than a
  privileged Harness writer?
- Are `none`, `fixture`, `fake`, `replay`, `real_local`, and `real_external` dependencies clear, with `none` reserved for pure static proof?
- Does a pass avoid implying server, browser, DB, or `external_runtime` behavior
  that was not exercised?
- Is failure structured enough for the Agent to inspect and continue?
