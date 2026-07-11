# Consistency and Authority Topologies

Use this reference when “one authority” appears to conflict with replication,
multiple writers, federation, CRDTs, event sourcing, or sagas.

## The Rule

```text
one canonical accepted fact
  -> one final acceptance or merge rule
     within a declared consistency domain and authority epoch
```

The rule identifies who or what decides acceptance. It does not require one
process, one replica, one storage row, or one candidate source.

## Single Writer or Leader Epoch

A leader may materialize facts while its lease/term/epoch is valid. Every write
must carry the epoch or fence. A demoted leader's late write is rejected.

Required proof:

```text
leader election or lease semantics
fencing token enforcement
split-brain rejection
recovery after failover
```

## Optimistic Multi-Proposer

Many callers may propose changes. One expected-version/CAS rule accepts at most
one transition from a given version; losers re-read, merge, or fail explicitly.

The proposers are not multiple authorities. The versioned acceptance rule and
owning cell are the authority.

## Event-Sourced Aggregate

The canonical event stream is accepted under one append rule. The reducer and
schema/epoch define state. Projections are derived and rebuildable under a
stated replay ceiling.

Do not claim event sourcing merely because events exist. A relational fact store
plus event/outbox is often enough.

## Federated or Imported Facts

Separate layers:

```text
remote source authority -> remote source claim
local import authority  -> accepted representation of that claim
local product authority -> business meaning or transition derived from it
```

Preserve source identity, version, provenance, and revocation/correction rules.
Do not silently rewrite an external claim into local truth without a decision.

## CRDT or Convergent State

For a CRDT, authority can be the declared operation/merge algebra plus
membership, schema version, and security policy. Replicas propose operations;
accepted state is the deterministic join of admitted operations.

Record:

```text
operation admission authority
replica identity and membership epoch
merge law and schema version
causal context / tombstone policy
permission and revocation semantics
compaction and snapshot proof
```

CRDT convergence does not solve authorization, semantic conflicts, privacy, or
business settlement. Keep non-commutative business transitions in an authority
cell even if adjacent collaboration state is convergent.

## Saga or Distributed Workflow

Each participant owns its local facts. A coordinator may own:

```text
process intent
step dispatch state
observed receipts
retry/reconciliation state
overall process disposition under an explicit policy
```

It does not directly own participant facts. Avoid pretending a saga is one
atomic transaction. Model unknown outcomes, compensation limits, and semantic
irreversibility.

## Derived Facts and Projections

A derived value may have its own materialization authority while remaining
rebuildable from source facts. State the dependency and staleness contract.
Caches and indexes are not alternate writers of the source fact.

## Ordering

Choose the weakest ordering that preserves semantics:

```text
no order / commutative
per-aggregate version
causal order
partition order
dense predecessor / certified gap closure
global total order only when product semantics require it
```

Worker arrival order is not product chronology. A global sequence should be a
last resort because it creates a scaling and availability authority.

## Authority Changes

When leadership, membership, schema, or policy changes, record an authority
epoch. Define:

```text
who may issue the new epoch
what fences the old epoch
how in-flight work is handled
how replicas and clients learn the change
what evidence proves no stale writer remains
```
