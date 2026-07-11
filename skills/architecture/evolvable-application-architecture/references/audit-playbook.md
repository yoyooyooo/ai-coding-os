# Audit Playbook

Use this playbook for an existing repository. Do not begin by proposing a new
folder tree.

## Select Mode

```text
quick-assessment       -> one risk and minimum correction
focused-boundary-review-> one authority/capability/transaction boundary
full-audit             -> repository-wide six-lens review
target-design          -> implementable target contracts and topology
migration-plan         -> vertical cutover, data, compatibility, deletion
```

Select a [Pressure Profile](pressure-profiles.md) for each traced slice.

## Reconnaissance

1. Read project instructions, SSoT, ADRs, public contracts, and roadmap.
2. Inventory packages/modules and actual dependency edges.
3. Locate executables/bootstrap files and composition roots.
4. Trace one Command from transport/UI through authority, persistence, event,
   and projection.
5. If applicable, trace one external Observation/Candidate through
   authentication, normalization, decision, and materialization.
6. Identify mutable state owners, direct state access, global singletons,
   caches, schedulers, and outcome registries.
7. Inspect transaction, idempotency, epoch/fencing, restart, event/outbox,
   realtime, replay, reconciliation, and migration paths.
8. Inspect tests and smoke code for alternate fact-creation paths.
9. Load the relevant language and scenario references.

Record `not_applicable` instead of inventing a candidate pipeline, distributed
workflow, or plugin boundary that the slice does not have.

## Six Lenses

```text
authority  -> accepted facts, consistency domain, epoch, forbidden writers
direction  -> dependency edges and SDK/infrastructure leakage
time       -> transaction, order, causality, retry, unknown outcome
topology   -> module, process, trust, replica, and deployment boundaries
lifecycle  -> construction, ownership, cancellation, migration, deletion
evidence   -> what each test actually proves and does not prove
```

## Pressure Map

Classify each issue as:

```text
authority or invariant leak
consistency / fencing ambiguity
dependency inversion failure
global-state coupling
transaction ambiguity
external capability semantic leakage
composition/profile leakage
compatibility or migration debt
projection/realtime divergence
proof or claim-ceiling gap
over-abstraction
```

## Severity

- **S0** — data integrity, authority, permission, privacy, financial, safety, or
  destructive risk.
- **S1** — central evolvability bottleneck, restart/consistency gap, or repeated
  repository-wide change.
- **S2** — architecture drift that raises cost but is locally containable.
- **S3** — cleanup, naming, packaging, or optional optimization.

Support findings with concrete paths, dependency edges, transactions, or traced
behavior. Separate observation from inference.

## Target Design

Describe only what the selected mode and pressure need:

- authority cells, consistency domains, and epochs;
- command/query APIs and candidate paths where applicable;
- internal typed collaboration versus outer capability ports;
- use-case transaction, external effect, and materialization boundaries;
- composition profiles and resource lifecycle;
- durable migration and compatibility policy;
- proof and deletion gates;
- deliberately omitted machinery.

Do not prescribe microservices, new packages, event sourcing, plugin systems, or
global buses unless the pressure map supports them.

## Migration Waves

A common sequence is:

```text
Wave 0: close direct mutation/import escape hatches; add characterization proof
Wave 1: migrate one high-pressure Command to typed use-case transaction
Wave 2: migrate applicable external candidate/effect and post-commit projection
Wave 3: thin facade and partition authority-cell state/outcomes
Wave 4: move concrete adapter selection to composition profiles
Wave 5: migrate data/callers, fence old writers, and delete old paths
```

Adjust order to the repository. Each wave must leave the system runnable and
include its own evidence and deletion gate.

## Output by Mode

### Quick Assessment

```text
pressure_profile
critical_authority
main_boundary_problem
minimum_correction
deliberately_not_needed
evidence_ceiling
```

### Focused Review

```text
sources_read
vertical_slice
observed_vs_inferred
findings_by_severity
target_contract
proof_and_deletion_gate
```

### Full Audit or Target Design

```text
six_lens_map
authority_map
pressure_map
findings_by_severity
target_boundaries
command_candidate_materialization
transaction_and_event_boundaries
composition_profiles
migration_waves
bridge_deletion_gates
evidence_plan
human_decisions
not_proven
not_claimed
```
