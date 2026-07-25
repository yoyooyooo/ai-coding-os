# Claim, Lifecycle, and Evidence Axes

Documentation governance keeps three independent axes separate. A field is optional; the repository only adopts metadata when it reduces a real ambiguity or supports a real traceability path.

## Claim Class

Claim class says what kind of statement an artifact makes:

| Class | Meaning |
|---|---|
| `source-input` | material supplied for interpretation, not yet adopted authority |
| `current-fact` | a current fact supported by the owning implementation, runtime, schema, test, or other evidence |
| `current-binding` | an adopted rule or constraint that governs present work |
| `accepted-target` | an adopted outcome delivery must satisfy, without claiming it is available now |
| `future-candidate` | a hypothesis, option, or future capability not adopted as current authority |
| `historical-evidence` | past proof, audit, experiment, source, or immutable record retained for traceability |

`active-proof` describes work in progress and belongs to the repository-selected execution/evidence method, not to the claim-class axis.

## Document Lifecycle

Lifecycle describes the document's editorial state:

```text
draft -> in-review -> accepted -> superseded -> archived
```

A repository may skip states or use a local equivalent. Lifecycle does not prove that the claim is current or implemented.

## Delivery / Evidence

Delivery and evidence describe what has been demonstrated:

```text
not-proven -> partial -> verified -> released
```

Use the owning test, runtime, migration, release, or operational evidence method. Do not require every Markdown file to carry a delivery field.

The distinctions are hard boundaries:

```text
accepted-target != current-fact
accepted-target != verified
accepted-target != released
current-fact != verified
verified != released
```

An accepted target may be the correct product decision authority while implementation evidence is partial or absent.

## Cross-system evidence

When `$ai-coding-os-suite-contracts` is installed, Product decisions, Harness
Results, and selected execution-method evidence may arrive through its Evidence Envelope.
Preserve `source_ref`, `claim_ceiling`, observations, supported interpretations,
`not_proven`, evidence refs, verification label, and Proof Surface when present.
Then classify the documentation claim locally.

```text
Product accepted -> may support accepted-target; delivery starts not-proven
verified current behavior -> may support current-fact for that question; not future intent
Harness pass -> evidence input; not execution completion or document acceptance
execution-method review -> bounded delivery evidence; not product acceptance
verified/released evidence -> not document lifecycle accepted
```

## Classification Test

Resolve every applicable axis; no axis is a mandatory first step:

1. Is this supplied source/input, a current fact, a current binding, an accepted target, a future candidate, or historical evidence?
2. What is the document lifecycle state?
3. What delivery/evidence level is actually supported?
4. Which repository-selected execution/evidence method owns active proof and completion?

When evidence is missing, lower the claim rather than promoting the prose.

## Mixed Documents

Mixed current and future material is acceptable when the layer supports it, boundaries are explicit, and the file remains the shortest coherent reading unit.

Allowed examples:

```text
Architecture: current topology + clearly labeled accepted seam.
ADR: accepted technical choice + partial implementation evidence.
Product: stable positioning + explicit not-current availability.
```

Split when future detail is large, uses a different reviewer, or creates a second authority chain.

## Question-scoped Authority

Use [Docs Layer Model](docs-layer-model.md) for the authority answer to a specific question. The compact rule is:

```text
what should it do       -> accepted product/business decision or baselined requirement
what implementation exists -> source/schema/migration/lockfile/generated artifact
what behavior was observed -> executed test/Harness/runtime/release/operations Evidence
what does a shared term mean -> SSoT and accepted decision
why was a choice made   -> product decision record or ADR by decision type
what does an interface accept -> adopted protocol/schema and contract tests
what is in progress     -> repository-selected execution/evidence method
```

Documentation alignment proves terminology, ownership, and accepted intent. Current availability requires owning evidence.
