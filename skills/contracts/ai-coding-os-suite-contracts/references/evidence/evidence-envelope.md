# Claim-Bounded Evidence Envelope

The Evidence Envelope is an optional direction-neutral pattern for carrying a
bounded observation between owner-local systems. Use it only when an actual
handoff, durable citation, or machine consumer benefits from one shared shape.
Do not create an Envelope merely because two Skills are adjacent.

Version 2 writers carry only:

```yaml
schema_version: 2
source_ref: <stable local or external reference>
claim_ceiling: <largest honest conclusion>
observed: {}
supports: []
not_proven: []
evidence_refs: []
proof_surface: {} # optional; only when a surface was exercised
```

The receiver decides relevance, classification, and sufficiency. The Envelope
never mutates the source artifact, grants new Authority, imports workflow or
document lifecycle, or states a routing direction.

## Safe Interpretation

- An accepted product decision can support an `accepted-target`; it does not
  prove implementation, runtime behavior, or release.
- Source, schema, migration, and generated artifacts support implementation or
  static-structure claims, not runtime observation by themselves.
- A Harness Result supports only its declared Proof Surface and claim ceiling.
- Harness `not_proven` means the path did not cover a property; it does not say
  that property is false or excluded by another owner.
- Execution evidence can support a bounded delivery claim under the selected
  execution method; it does not accept Product or documentation artifacts.
- Ticket state, blockers, release state, and document lifecycle stay with their
  owners; the Envelope carries evidence, not workflow state.

## Non-equivalences

```text
Harness pass != execution-method completion
Harness not_proven != execution-method exclusion
accepted product target != verified implementation
observed current behavior != accepted future product target
execution status != product or document acceptance
Docs verified/released != document acceptance
```

## Compatibility

The schema retains finite version-1 reader compatibility for the previous
`translation` plus `source_ref.kind` shape and now rejects mismatched legacy
translation/source-kind combinations. Version-2 writers must not emit those
fields. Migrate by preserving the stable source reference and claim boundary,
not by preserving the old directional matrix.

See the three examples under `examples/` for Harness observation, product
decision, and selected-execution evidence. The forbidden-promotions file records
semantic promotions that every receiver must reject.
