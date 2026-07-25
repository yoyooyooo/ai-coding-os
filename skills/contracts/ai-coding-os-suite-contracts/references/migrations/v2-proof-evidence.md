# Suite Contracts v2 Migration

Suite Contracts v2 introduces orthogonal Proof Surface fields, a claim-bounded
Evidence Envelope, and one eval file schema. Later 2.x revisions close the v2
writer boundary and simplify cross-owner evidence.

## Harness Descriptor and Result

Writers emit `schema_version: 2` and replace legacy `surface` with:

```yaml
proof_surface:
  surface_kind: headless
  dependency_reality:
    - real_local
  environment_class: local_stack
  proof_focus:
    - persistence_restart
```

Readers may continue to accept `schema_version: 1` descriptors/results during
migration. The shared JSON Schemas validate both versions, while v2 validators
reject legacy `surface` / `environment`, known camelCase aliases, and Descriptor
`exercises` fields that would duplicate canonical snake_case facts. Do not copy a legacy surface
string into `dependency_reality`; use the mapping and uncertainty rules in the
Proof Surface reference. Pure static proof uses `dependency_reality: [none]`;
`none` cannot be combined with runtime dependency values.

V2 Harness Results also carry `claim_ceiling`; `evidence_refs` and
`verification_level` are available when the result must cross artifact systems.

## Evidence Envelope

Use an Evidence Envelope only when a real handoff, durable citation, or machine
consumer benefits. Existing Product, Docs, Harness, and selected
execution-method artifacts remain owner-local. Version-2 writers carry a stable
`source_ref` plus claim boundary and optional Proof Surface without directional
translation or source-kind registries. The schema retains finite version-1
reader compatibility and rejects mismatched legacy translation/source-kind
pairs. Workflow-specific states remain outside the Suite.

## Eval Assets

All `evals/*.json` files now use:

```text
schema_version + skill_name + evals[]
```

The former Product Definition top-level array and `expected` field migrate to
the shared object shape and `expected_output`. Numeric IDs remain supported;
new durable cases should prefer stable strings.

## Workflow-Specific Compatibility

Workflow-specific compatibility, templates, and CLI behavior stay with their
independent owner. They are not part of Suite Contracts v2 or the core Skill
roster. Legacy directional envelopes should migrate to the version-2 direction-neutral
shape when they next cross an owner boundary; historical records need not be
rewritten.
