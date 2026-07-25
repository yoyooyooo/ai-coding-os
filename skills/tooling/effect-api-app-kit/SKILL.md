---
name: effect-api-app-kit
description: >-
  Atomic Effect API scaffolding from an explicit Change Spec. Use when settled
  architecture and Effect-version decisions need a P0-P3 capability slice to
  be inspected, planned, applied, verified, or repaired with managed registry
  state.
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
  product decision authority and fact authority
  pressure selection
  transaction and public API semantics
  exact installed Effect surface
  dependency installation
  docs authority
  claims beyond executed commands

Adjacent Suite owners, when installed:
  product requirements and acceptance -> `$product-definition`
  architecture and source-shape decisions -> `$evolvable-application-architecture`
  Effect version and runtime constraints -> `$effect-best-practices`
  reusable default adoption -> `$evolvable-application-preset`
```

## Change Spec

`plan` and `apply` consume the local
[Change Spec schema](schemas/change-spec.schema.json). When authoring one, read
the [worked example](examples/add-order-create.yaml); when reviewing P0-P3 file
selection, read [Generated Shape](references/generated-shape.md). Spec fields
select semantic files rather than a symmetrical suffix set. P3 requires an
existing project Harness entry plus an explicit command, observable set,
exclusions, and claim ceiling. The Kit binds those project-owned declarations
into a canonical Harness Descriptor v2; it does not invent recovery coverage.

## Kit Pass

| Step | Completion criterion |
| --- | --- |
| Inspect | Repository host, existing managed state, Effect version evidence, conflicts, and verification commands are known. |
| Plan | The complete patch, generated filenames, manifest delta, registry delta, and blockers are visible without writes. |
| Stage | Every output file is rendered and structurally validated in a temporary tree. |
| Apply | One lock and transaction journal cover source, manifest, and registry replacement; any failure restores all touched paths. |
| Verify | Manifest parses, hashes and files agree, registry matches, and no incomplete transaction remains. |
| Run | When `--run` is selected, recorded project commands execute under a bounded timeout; exit/timeout observations do not prove that a Descriptor exercised every declared claim. |
| Repair | Managed drift is either reconstructed from the manifest or reported as a project-owned conflict. |

## Commands

```bash
python3 scripts/kit.py inspect --repo <repo>
python3 scripts/kit.py plan --repo <repo> --change <change.yaml>
python3 scripts/kit.py apply --repo <repo> --change <change.yaml>
python3 scripts/kit.py verify --repo <repo>
python3 scripts/kit.py verify --repo <repo> --run --timeout-seconds 120
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

Default `verify` supports structural-integrity claims only. `verify --run`
records bounded command exit/timeout observations; semantic Descriptor coverage
still requires a Harness Result or equivalent project evidence. Expected input,
filesystem, commit, and rollback failures return structured JSON without a raw
traceback.

Read [Atomic Patch Protocol](references/atomic-patch-protocol.md) when an apply
or recovery path needs transaction detail.
