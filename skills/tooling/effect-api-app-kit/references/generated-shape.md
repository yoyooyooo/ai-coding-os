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
  <subject>.<operation>.recovery.harness.ts
```

The module remains private to the host. Workspace package promotion is a
separate architecture decision and migration, not an `add-slice` side effect.
Generated source files become project-owned; only the manifest and host registry
remain managed.
