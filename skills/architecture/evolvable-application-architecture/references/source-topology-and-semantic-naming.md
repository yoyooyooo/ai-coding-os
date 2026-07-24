# Source Topology and Semantic Naming

Use **Bounded Semantic Flatness**:

> Coarse durable boundaries use directories and packages. Fine-grained local
> responsibility uses semantic dot-separated filenames.

```text
folders own
filenames explain
packages enforce
apps run
```

## Filename grammar

```text
<subject>[.<facet>...].<responsibility>[.<qualifier>...].<extension>
```

Use kebab-case inside one semantic segment and dots between dimensions.
Order from product meaning to implementation detail.

```text
order.create.use-case.ts
order.payment-gateway.stripe.live.ts
channel.client.browser.live.ts
order.checkout.restart.recovery.test.ts
```

Avoid splitting one phrase into multiple dot dimensions:

```text
use-case          # one semantic term
view-model
expected-version
```

Do not use:

```text
order.create.use.case.ts
order.payment.expected.version.policy.ts
```

## Dot prefixes are lexical clusters

```text
order.payment.*
```

is a **lexical capability cluster**. It improves search, tabs, and Agent context,
but it does not create privacy, dependency checks, lifecycle, fact authority,
package exports, or deployment isolation.

Promotion ladder:

```text
lexical cluster
  -> private submodule
  -> workspace package
  -> deployable process
```

Promote only when the next level's real pressure exists.

## Directory admission test

Create a directory when at least one is true:

```text
it represents a real capability or authority owner
it needs a different public/private import rule
it has independent resource lifecycle or composition
it can be replaced, tested, migrated, or promoted as a unit
a framework/tool requires the directory
it is a stable, growing, high-density lexical cluster
```

Do not create one-file directory chains for visual symmetry or because an
architecture diagram contains another layer.

A soft review signal:

```text
3-20 source files     semantic flat is usually readable
20-40 source files    inspect repeated stable prefixes
40+ source files      likely sub-capability pressure unless generated/protocol data
```

File count never decides authority by itself.

## Semantic segment length

Two to four semantic segments are common. Five is acceptable. More than five
triggers review because the name may be compensating for a missing boundary or
mixed responsibility. Test qualifiers and extensions are not counted as product
segments.

## Public and wiring surfaces

Prefer subject-qualified names:

```text
order.public.ts
order.wiring.ts
```

`order.public.ts` exposes ordinary collaboration: commands, queries, stable
contracts, and projections. It does not expose ORM records, live providers,
mutable state, or framework handlers.

`order.wiring.ts` exposes constructors, Layers, adapter factories, and host-only
assembly. Other business modules must not import it.

## Vocabulary

The portable Suite contract for canonical vocabulary, filename patterns, and
guarded terms is `$ai-coding-os-suite-contracts`. Do not resolve it through a
sibling repository path; installed Skill directories may be flat or otherwise
reorganized.

Architecture responsibility terms are relatively closed: an Agent should reuse
them rather than silently invent a synonym. New long-lived responsibility terms
must be registered with a definition and distinction.

Technology/provider qualifiers are semi-open. Product terms are open across
projects but canonical inside one project.

Project-specific language belongs in:

```text
docs/ssot/product-language.md
docs/standards/naming-vocabulary.yaml
```

## Naming and import rules are one standard

Names are not decoration. Link suffixes to dependency checks:

```text
*.policy.ts
  depends only on pure model/value/context contracts

*.use-case.ts
  may depend on model/policy/port/transaction contracts
  must not depend on *.live.ts, HTTP framework, or provider SDK

*.port.ts
  is application-owned and must not expose provider SDK types

*.live.ts
  may depend on infrastructure and is selected by wiring/composition

*.fake.ts
  is explicit test/harness implementation, never silent production fallback

*.http.*.ts
  decodes/maps/calls use cases; it does not write persistence directly

*.public.ts
  is normal cross-module surface

*.wiring.ts
  is host-only construction surface
```

Use package exports, import rules, TypeScript project references where useful,
and architecture tests to enforce the durable edges.

## Avoid file explosion

Do not mechanically create command/input/output/policy/mapper/use-case files for
every operation. A simple P0/P1 operation may keep types and implementation in:

```text
order.create.use-case.ts
```

Split when reuse, independent change, boundary, or proof pressure appears.

## Framework exceptions

Framework-controlled paths may use framework names:

```text
route/layout/page files
file-system routers
generated clients
database migrations
*.d.ts
```

Keep framework adapters thin and move product logic into named capability files.
