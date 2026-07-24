---
name: effect-api-app-kit
description: >-
  Atomic Effect API scaffolding from an explicit Change Spec. Use after
  architecture and Effect-version decisions are settled to inspect, plan,
  apply, verify, or repair P0-P3 capability slices and managed registry state.
---

# Effect API App Kit

Generate a deterministic capability slice from settled decisions. This Kit
implements source shape and atomic managed-state updates; it does not infer
product architecture.

Open architecture questions go to `$evolvable-application-architecture`;
Effect API and version questions go to `$effect-best-practices`.

## Ownership

```text
Owns:
  explicit Change Spec parsing
  deterministic semantic filenames
  P0-P3 capability-slice shapes
  preflight conflict detection
  staged atomic multi-file apply and rollback
  managed manifest and module registry
  structural verification and repair

Project owns:
  product and fact authority
  pressure selection
  transaction and public API semantics
  exact installed Effect surface
  dependency installation
  docs authority
  claims beyond executed commands
```

## Change Spec

```yaml
schema_version: 1
change:
  id: add-order-create
  operation: add-slice
host:
  path: apps/api
  name: api
slice:
  module: orders
  subject: order
  operation: create
  pressure: P1
  persistence: postgres
  effect_profile: installed
http:
  enabled: true
external_capability: null
verification:
  commands:
    - pnpm --filter api typecheck
    - pnpm --filter api test
```

Shapes encode real semantic differences:

```text
P0  model + use case + public surface + focused test
P1  command/context + transaction/idempotency/persistence ports
    fake/live seam + expected version/receipt + wiring
P2  external port + observation/candidate + provider adapter
    materialization use case + conformance test
P3  outbox/inbox/replay/recovery harness placeholders
```

Spec fields select files; the Kit does not generate a complete suffix set by
symmetry.

## Kit Pass

| Step | Completion criterion |
| --- | --- |
| Inspect | Repository host, existing managed state, Effect version evidence, conflicts, and verification commands are known. |
| Plan | The complete patch, generated filenames, manifest delta, registry delta, and blockers are visible without writes. |
| Stage | Every output file is rendered and structurally validated in a temporary tree. |
| Apply | One lock and transaction journal cover source, manifest, and registry replacement; any failure restores all touched paths. |
| Verify | Manifest parses, hashes and files agree, registry matches, and no incomplete transaction remains. |
| Run | When `--run` is selected, recorded project commands execute and their actual statuses bound compile/test claims. |
| Repair | Managed drift is either reconstructed from the manifest or reported as a project-owned conflict. |

## Commands

```bash
python3 scripts/kit.py inspect --repo <repo>
python3 scripts/kit.py plan --repo <repo> --change <change.yaml>
python3 scripts/kit.py apply --repo <repo> --change <change.yaml>
python3 scripts/kit.py verify --repo <repo>
python3 scripts/kit.py verify --repo <repo> --run
python3 scripts/kit.py repair --repo <repo>
```

## Atomicity and Managed State

```text
inspect and validate
-> calculate full patch
-> stage and validate
-> acquire lock
-> journal previous state
-> replace source, manifest, and registry
-> rollback every touched path on failure
```

```text
.evo-kit/manifest.yaml
.evo-kit/transactions/<txid>/journal.json
<host>/src/host/generated.modules.ts
```

The manifest and generated registry stay managed. Newly created capability
files become ordinary project source and are not silently overwritten.

Default `verify` supports structural-integrity claims only. `verify --run` adds
only the claims supported by the recorded commands.

## Read When Needed

- Applying or recovering a transaction: [Atomic Patch Protocol](references/atomic-patch-protocol.md)
- Inspecting generated files: [Generated Shape](references/generated-shape.md)
- Authoring input: [Change Spec Schema](schemas/change-spec.schema.json)
