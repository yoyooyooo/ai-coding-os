# Generated Shape

Default target:

```text
apps/api/src/modules/<module>/
  <subject>.model.ts
  <subject>.<operation>.use-case.ts
  <subject>.public.ts
  <subject>.wiring.ts
  ...pressure-specific files...

apps/api/src/host/generated.modules.ts
.evo-kit/manifest.yaml
```

## Pressure-specific shape

```text
P0
  <subject>.model.ts
  <subject>.<operation>.use-case.ts

P1+
  <subject>.<operation>.command.ts
  <subject>.command-context.ts
  <subject>.<operation>.receipt.ts
  <subject>.repository.port.ts
  <subject>.transaction.port.ts
  <subject>.idempotency.port.ts
  <subject>.repository.<technology>.<live-or-fake>.ts

P2+
  <subject>.<capability>.candidate.ts
  <subject>.<capability>.port.ts
  <subject>.<capability>.<provider>.live.ts
  <subject>.<capability>.materialize.use-case.ts
  <subject>.<capability>.contract.test.ts

P3
  <subject>.outbox.ts
  <subject>.inbox.ts
  <subject>.<operation>.recovery.harness.yaml  # Descriptor v2 bound to a project-provided Harness entry
```

The module remains private to the host. Workspace package promotion is a
separate architecture decision and migration, not an `add-slice` side effect.
Generated source files and the P3 Harness Descriptor become project-owned; only
the manifest and host registry remain managed. P3 requires a pre-existing
project Harness entry and an explicitly supplied command, observables,
exclusions, and claim ceiling. The Descriptor records that binding in `uses`;
Schema validity or a successful generic command does not prove its declared
recovery coverage.
