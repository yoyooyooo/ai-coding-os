# Audit Playbook

Use this playbook for an existing repository. Do not begin by proposing a new
folder tree.

## Reconnaissance

1. Read project instructions, SSoT, ADRs, public contracts, and current roadmap.
2. Inventory packages/modules and actual dependency edges.
3. Locate executables/bootstrap files and all composition roots.
4. Trace one command from transport/UI through application, persistence, event,
   and projection.
5. Trace one external candidate from provider/runtime/plugin through
   normalization and materialization.
6. Identify all mutable state owners, direct state access, global singletons,
   caches, and outcome registries.
7. Inspect transaction, idempotency, restart, event/outbox, realtime, replay,
   and migration paths.
8. Inspect tests and smoke code for alternate fact-creation paths.
9. Select the relevant language/scenario adapter.

## Pressure Map

Record each pressure as one of:

```text
authority leak
invariant leak
dependency inversion failure
global-state coupling
transaction ambiguity
adapter semantic leakage
composition/profile leakage
compatibility debt
projection/realtime divergence
proof or claim-ceiling gap
over-abstraction
```

## Severity

- **P0** — data integrity, authority, permission, privacy, or destructive risk.
- **P1** — central evolvability bottleneck or repeated repository-wide change.
- **P2** — architecture drift that raises cost but is locally containable.
- **P3** — cleanup, naming, packaging, or optional optimization.

Support findings with concrete paths, dependency edges, or traced behavior.
Separate observed facts from inference.

## Target Design

Describe:

- authority cells and their private state;
- command/query APIs;
- capability ports and adapter outputs;
- use-case transaction and materialization boundaries;
- composition profiles;
- durable migration and compatibility policy;
- proof and deletion gates.

Do not prescribe microservices or new packages unless the pressure map supports
them.

## Migration Waves

Prefer:

```text
Wave 0: close direct mutation/import escape hatches; add characterization proof
Wave 1: migrate one high-pressure command to typed use-case transaction
Wave 2: migrate external candidate materialization and post-commit projection
Wave 3: thin facade and partition module state/outcomes
Wave 4: move concrete adapter selection to composition profiles
Wave 5: evolve secondary modules and delete old paths
```

Adjust order to the repository, but each wave should leave the system runnable
and include its own deletion gate.

## Audit Output

```text
mode
sources_read
vertical_slice_traced
authority_map
pressure_map
findings_by_severity
target_model
migration_waves
compatibility_and_data_migration
proof_plan
deletions
auto_fix_candidates
human_decisions
not_claimed
```
