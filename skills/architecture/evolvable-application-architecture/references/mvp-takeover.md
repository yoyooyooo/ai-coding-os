# MVP Takeover

Use this mode when a prototype or AI-generated MVP must become maintainable and
production-capable while upstream product iteration continues.

Do not begin with a rewrite. First make the existing behavior legible and
harnessable.

## Takeover sequence

```text
inspect actual behavior
-> characterize important paths
-> inventory accepted-fact writers
-> classify durable vs disposable implementation
-> identify duplicated frontend/server truth
-> identify hidden external effects and resource owners
-> choose one productionization vertical slice
-> insert the smallest authority/use-case/capability seam
-> migrate readers and writers
-> fence and delete old paths
```

## Inventory

Record for the chosen slice:

```text
user intent
current entrypoints
all state writers
transaction boundary
external calls and unknown outcomes
projection/read path
frontend state owners
resource lifecycle owners
current harness/test surfaces
public contract and stored-data compatibility
```

## Durable versus disposable

A fast prototype may remain simple, but classify components:

```text
durable
  accepted facts, public contracts, migrations, user-visible behavior,
  permissions, audit, external effect identity

disposable
  temporary UI layout, in-memory fake, prototype provider, local-only route,
  copied fixture, generated glue without long-term contract
```

Do not preserve disposable internal APIs merely because they already exist.
Durable accepted facts receive a deliberate forward path.

## First production slice

Choose a slice with meaningful value and bounded risk. Add only required
pressure mechanisms:

```text
P0  private state, explicit functions, basic tests
P1  transaction, idempotency, expected version, durable receipt
P2  capability port, normalized candidate/observation, conformance
P3  outbox/inbox, replay, unknown outcome, recovery
P4  permission, approval, audit, privacy, irreversible-effect safety
```

The project lifecycle stage and pressure are independent. A P0 read-only page
may be productionized; a payment prototype may already carry P4 risk.

## Upstream iteration

Preserve a clear intake path for ongoing prototype changes:

```text
new UI/flow semantics
  -> candidate change
  -> map to current authority and contracts
  -> migrate one vertical slice
  -> prove through existing or thinnest new harness
```

Do not let upstream code reintroduce direct fact writers, projection mirrors, or
provider SDK types across the core.
