# Artifact Graph

Artifact Graph is an opt-in navigation inventory for repositories where direct routes no longer make source, candidate, report, specification, decision, or roadmap lineage discoverable. It is not a default Docs Governance surface and is never an execution graph.

## Does Not Own

```text
product truth
requirement identity
planning/frontier/dependency state
assignment or scheduling
execution methods, trackers, and releases
readiness/completion
automatic promotion
```

Use a repository-selected execution method for blockers, dependencies, queues and completion. A graph link can preserve provenance; it cannot establish workflow status.

## Admission

Add metadata only when direct links cannot adequately show one of:

- source/evidence lineage across durable artifacts;
- a rename-resistant citation needed by multiple readers;
- a generated navigation view that materially reduces discovery cost;
- a cross-method relation whose source and target remain semantically distinct.

Ordinary Product, SSoT, Architecture, Design, ADR, PRD, or source files usually need no graph metadata.

## Example Frontmatter After Admission

```yaml
---
node_id: web-channel-projection-proposal
artifact_type: proposal
status: candidate
related_to:
  - web-channel-source-synthesis
source_material:
  - docs/reports/research/web-channel-notes.md
evidence: []
---
```

`node_id` is unique only within opted-in roots. It is not a universal document ID.

Suggested broad types:

```text
seed proposal source brief decision spec report roadmap
```

Suggested lifecycle labels:

```text
candidate current future historical superseded retired
```

Projects can extend vocabulary only through a local documented schema.

## Relations

```yaml
related_to:
supersedes:
source_material:
evidence:
```

Relations describe durable discoverability/provenance, not causal execution edges. Omit an uncertain relation instead of inventing one.

## Identity Separation

```text
semantic path          -> ordinary document identity
sequential ADR ID      -> append-only citation
requirement/control ID -> traceability where earned
node_id                -> optional graph navigation identity
business number        -> runtime/domain identity
```

## Audit Limits

`scan_artifact_graph.py` checks duplicate IDs, malformed metadata and declared target existence. It does not infer semantic correctness, readiness, blockers, promotion, completion or scheduling.
