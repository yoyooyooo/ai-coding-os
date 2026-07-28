# Source Topology and Semantic Naming

This reference owns portable source naming and directory defaults. It preserves semantic roles while allowing each ecosystem to use idiomatic enforcement.

## Naming invariant

Names should reveal:

```text
product subject
operation or facet
semantic responsibility
provider, transport, or host qualifier when needed
```

Avoid generic buckets such as `service`, `manager`, `common`, `core`, `utils`, `helpers`, and `types` when a governed responsibility can be named.

## TypeScript segment grammar

```text
kebab-case inside one semantic segment
dots between semantic dimensions
```

Examples:

```text
order.submit.use-case.ts
order.repository.port.ts
order.repository.postgres.live.ts
order.repository.memory.fake.ts
payment.authorize.command.ts
payment.risk.policy.ts
order.http.contract.ts
order.http.handlers.ts
api.composition.ts
```

## Default TypeScript semantic filenames

```text
<subject>.<operation>.command.ts
<subject>.command-context.ts
<subject>.<operation>.use-case.ts
<subject>.<read-purpose>.query.ts
<subject>.<decision>.policy.ts
<subject>.<capability>.port.ts
<subject>.<capability>.<provider>.live.ts
<subject>.<capability>.memory.fake.ts
<subject>.transaction.port.ts
<subject>.idempotency.port.ts
<subject>.http.contract.ts
<subject>.http.handlers.ts
<subject>.public.ts
<subject>.wiring.ts
<host>.config.ts
<host>.composition.ts
<host>.main.ts
<host>.shutdown.ts
```

Do not generate the complete suffix family. A simple capability may keep command, outcome, and implementation in one `*.use-case.ts` file.

## Responsibility vocabulary

| Role | Default suffix | Meaning |
| --- | --- | --- |
| model | `.model.ts` | cohesive product/domain values and behavior; not ORM or wire shape by default |
| command | `.command.ts` | authoritative intent requesting a controlled transition |
| query | `.query.ts` | read of an authoritative projection without creating accepted facts |
| use case | `.use-case.ts` | authorization, validation, transition, and commit boundary |
| policy | `.policy.ts` | pure or explicitly contextual decision logic |
| Port | `.port.ts` | application-owned outer capability contract |
| live implementation | `.<provider>.live.ts` | selected provider/storage/transport implementation |
| fake | `.memory.fake.ts` or a project-qualified equivalent | deterministic behavioral substitute, never silent fallback |
| mapper | `.mapper.ts` | pure conversion between explicitly named representations |
| schema | `.schema.ts` | runtime decoding of untrusted or wire data |
| transport contract | `.<transport>.contract.ts` | adopted request/response or message shape |
| transport handlers | `.<transport>.handlers.ts` | decode, invoke use case, and map result |
| event | `.event.ts` | stable notification of an accepted change or named occurrence |
| projection | `.projection.ts` | read-oriented representation derived from accepted facts |
| public surface | `.public.ts` | deliberate cross-module collaboration surface |
| module wiring | `.wiring.ts` | module-local constructors or adapter factories |

Qualify generic words. Prefer `order.repository.port.ts` to `repository.ts`, and `payment.wire-to-projection.mapper.ts` to `mapper.ts`.

## Test and Harness filenames

Use the smallest role that communicates the observation:

```text
<subject>.<role>.unit.test.ts
<subject>.<role>.contract.test.ts
<subject>.<role>.integration.test.ts
<subject>.<case>.recovery.test.ts
<subject>.<case>.e2e.test.ts
<subject>.<case>.harness.ts
```

Follow the project's test-runner suffix when it is coherent. Co-locate focused unit or contract tests with the owning capability when the ecosystem supports it. Put cross-capability integration, recovery, browser, or end-to-end tests under a discoverable project test/Harness surface such as `tests/`; do not create a global fixture dump with no owner.

## Generated, vendored, and migration material

- mark generated source with a clear directory or suffix such as `generated/` or `*.generated.ts`, and expose the regeneration command;
- keep vendored or externally generated material visibly separate from project-authored source;
- place data migrations in the owning store/framework's conventional `migrations/` surface and use its stable ordering scheme;
- generated, vendored, and migration directories do not gain product authority by placement.

## Public and private surfaces

Prefer a named `*.public.ts` surface for a feature/module boundary. Use `index.ts` only when tooling or package convention requires it, and keep the export list explicit. Broad barrels that expose internals are not a public API.

`*.wiring.ts` is a module-level composition helper when useful; host-level implementation selection belongs in `<host>.composition.ts`.

## Directories

Name directories after product capabilities or host roles:

```text
orders/
payments/
identity/
api/
worker/
```

Avoid directories named after generic architectural nouns unless they have a clear local scope. A top-level `services/` containing unrelated product areas is weaker than `modules/orders/` and `modules/payments/`.
Inside a capability, keep semantic dot files flat until a durable sub-capability or local boundary earns another directory. Do not mirror abstract layers such as `domain/application/infrastructure` mechanically in every module.

## Import defaults

```text
*.model.ts / *.policy.ts
  no HTTP, database, SDK, live adapter, or process-environment import

*.use-case.ts
  may import model, policy, Port, and transaction contracts
  must not import *.live.ts or framework handlers

*.port.ts
  must not expose provider SDK or ORM types

*.http.*.ts
  decode -> map -> call use case -> map result
  must not write product facts directly

*.public.ts
  normal cross-module surface

*.wiring.ts / <host>.composition.ts
  select implementations; ordinary business modules do not import them
```

## Ecosystem projection

Rust should use idiomatic module, visibility, facade, crate, and binary naming rather than imitating TypeScript dots. Other ecosystems use their normal module/public API/build surfaces while preserving the same semantic roles.

## Project Standard

When these rules bind more than one capability, adopt them in `docs/standards/source-topology-and-naming.md`. Use the [project Standard template](../templates/source-topology-and-naming.md), record compact selected defaults in [architecture-profile.yaml](../templates/architecture-profile.yaml) only when a structured profile has a real consumer, and use [naming-vocabulary.yaml](../templates/naming-vocabulary.yaml) only when stable terminology lookup has an actual consumer.

## Project override

Preserve a coherent existing grammar. Record the mapping once in `AGENTS.md` or an applicable Standard. Do not introduce a second dialect beside it.

## Related knowledge

- Use [Default repository profile](default-repository-profile.md) for directory topology.
- Use [TypeScript backend projection](typescript-backend-projection.md) for runtime and persistence detail.
- Use [Rust projection](rust-projection.md) for idiomatic Rust shape.
- Use `$frontend-architecture` for frontend-specific suffixes.
- Use `$product-harness-system` for verification command semantics.
- Return to the [EAA map](../SKILL.md).
