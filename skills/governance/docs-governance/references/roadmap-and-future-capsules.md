# Roadmap and Future Capability Capsules

## Roadmap Owns

```text
long-horizon product evolution sequence
capability prerequisites and promotion gates
current launch/coverage gates
future capability routes
links to Goal Proof and evidence
```

Roadmap does not own step-by-step implementation, current object authority or duplicated Goal progress.

## Preserve Long-Horizon Value

Do not delete a Roadmap merely because it is not currently implemented. Retain it when it still:

- constrains product evolution order;
- prevents unsafe early implementation;
- defines a falsifiable promotion gate;
- links current foundations to a future objective;
- is referenced by the active roadmap or capability matrix.

Examples such as Product Evolution Sequence are durable route documents, not stale execution plans.

## Capability Capsule Home

```text
docs/roadmap/future/<capability>/README.md
```

Organize by capability, not by duplicated layers. Forbidden shadow homes include:

```text
docs/roadmap/future/ssot
docs/roadmap/future/standards
docs/roadmap/future/adr
docs/roadmap/future/architecture
docs/roadmap/future/product
docs/roadmap/future/protocols
```

`future/ssot` is a semantic contradiction and creates a second authority chain.

## Required Capsule Questions

Every capsule should answer:

```text
Product Hypothesis
Candidate Capability Boundary
Reusable Current Foundations
Current Non-authority
Candidate Authority Model
Candidate Architecture
Prerequisites
Promotion Gates
First Falsifiable Proof
Forbidden Early Implementations
Promotion Targets
Sources And Evidence
```

Use `templates/future-capability-capsule.md`.

## Frontmatter

Recommended:

```yaml
---
node_id: roadmap-future-<capability>
artifact_type: roadmap
status: open-candidate
authority_scope: future-candidate
objective: ...
claim_limit: Future candidate only; no current availability claim.
evidence_contract: ...
next_action: ...
---
```

## Promotion

```text
Future capsule
  -> smallest falsifiable proof / Goal Pack
  -> accepted ADR, when a tradeoff becomes binding
  -> Product / SSoT / Architecture / Standard / Protocol
  -> update capability matrix and indexes
  -> remove promoted authority from capsule
```

Promotion is a move, not a copy. After promotion, retain only remaining future delta, unmet gates and source/evidence backlinks.

## Delete or Merge

A capsule may be deleted or merged when:

- it has been fully absorbed into formal current layers;
- another capsule completely supersedes it;
- product direction is explicitly rejected and the reason is retained in ADR/Report;
- it has no route, gate, source, evidence or decision value.

Do not delete simply because implementation has not started.
