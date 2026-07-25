---
name: docs-governance
description: >-
  Converges repository documentation Authority, Routes, Earned Shape, and
  Evidence. Use when current homes compete, claims need current/target/future
  classification, docs layers or partitions need admission, AGENTS.md or docs
  routers need convergence, documentation must be migrated or cleaned up, or
  source/evidence alignment needs audit.
---

# Docs Governance

Use four leading words:

```text
Authority    one canonical Current Home per claim, representation, and scope
Route        a discoverable edge to Authority, never a mandatory reading sequence
Earned Shape stable semantic layers, flat by default, structure under real pressure
Evidence     code, tests, runtime, schema, release, or other owning proof
```

A target is not Evidence. A review signal is not a migration order. An execution
artifact may cite Authority without becoming Authority.

## Operating Contract

```text
Owns:
  documentation layer and partition placement
  current / accepted-target / future classification
  multi-entry routes, indexes, and source alignment
  Earned Shape and identity admission
  retention, migration, cleanup, and resolved Preset placement
  context legibility, knowledge freshness, and stale-map disposition
  durable-assumption owner, scope, and invalidation hygiene
  thin AGENTS.md knowledge-network governance

Hands off:
  product, technical, security, legal, policy, release, and delivery decisions
  execution dependency, assignment, frontier, status, and completion lifecycle

Adjacent Suite owners, when installed:
  product semantics, decisions, requirements, acceptance -> `$product-definition`
  technical facts and target architecture -> the applicable architecture Skill
  reusable defaults, candidate snapshots, and adopted legacy snapshots -> `$evolvable-application-preset`

Block only the affected convergence, promotion, cleanup, or Current Home change when:
  two plausible Authorities remain unresolved
  cleanup risks unlinking Evidence
  resolution requires a new product, security, public-contract, or legal decision

Preserve competing sources and Evidence Routes, name the external decision, and
continue unaffected layer, link, classification, and cleanup work. Stop the
whole run only when Evidence cannot be preserved or continued mutation risks
irreversible repository-wide damage.
```

## Reasoning and Automation Boundary

The Agent decides semantic ownership, claim classification, admission, conflict
resolution, and promotion/demotion. Scripts exhaustively check declared
identities, links, markers, routes, repository boundaries, and source-path
existence. A script finding is review evidence, not semantic judgment. A registry
or schema appears only after durable routing, identity, or automation pressure
earns it. Ordinary reversible placement and route repairs follow current project
Authority directly. A durable unresolved-decision record belongs in an existing
project decision home and is created only when review or handoff pressure earns it.

## Governance Coverage

Cover every applicable decision below. The Agent may enter from a question,
code area, term, document, source, evidence result, repository entry, or docs
router and revisit decisions in any order.

### Discover

Locate the affected artifacts, project policy, semantic owner, direct Evidence,
competing current homes, and the smallest context route that exposes them. Follow only relevant edges; `AGENTS.md` and
`docs/README.md` are useful entry surfaces when present, not required traversal
nodes.

Use [Agent Entry and Preset](references/agent-entry-and-preset.md) for entry
ownership and [Docs Layer Model](references/docs-layer-model.md) for placement.

**Completion criterion:** every affected meaning has enough local context to
identify candidate Authority, Evidence, conflicts, freshness, and invalidation
without loading unrelated layers.

### Classify

For each affected meaning:

```text
claim class: source-input | current-fact | current-binding | accepted-target | future-candidate | historical-evidence
lifecycle: draft | in-review | accepted | superseded | archived
delivery/evidence: not-proven | partial | verified | released
semantic owner: one current Authority
knowledge basis: accepted | observed | source-derived | inferred | assumed | unknown
invalidates when: source, version, decision, migration, or time condition when material
```

Keep active execution state with the repository-selected execution method.
When Product, Harness, or execution evidence crosses into documentation, cite
its owning artifact directly unless a real machine consumer or durable repeated
handoff earns the optional claim-bounded `$ai-coding-os-suite-contracts`
Evidence Envelope. The source owner still decides source meaning; documentation
authority decides placement and lifecycle.

**Completion criterion:** claim class, lifecycle, knowledge basis, Evidence level,
semantic owner, and any material invalidation condition are honest and
non-equivalent.

### Admit

Apply three independent gates:

- **Layer Admission:** a top-level layer needs a durable Authority role that no
  existing layer can own clearly.
- **Partition Admission:** a child needs durable ownership, security, retention,
  lifecycle, release, reader routing, or sustained navigation pressure.
- **Identity Admission:** stable keys, sequential IDs, atomic IDs, or graph IDs
  need real citation, traceability, or automation pressure.

Use [Earned Shape](references/elastic-shape-and-identity.md). Candidate layer
vocabulary is a menu, not an initialization list.

**Completion criterion:** every new layer, partition, route, metadata field, and
identifier has a concrete Authority, reader, lifecycle, security, release, or
Evidence reason.

### Converge

Choose the smallest semantic change that restores one canonical Current Home for the affected claim, representation, and scope:

```text
promote | demote | split | merge | partition | flatten
bridge | retain | delete | block
```

Preserve useful source and Evidence backlinks. A stale map is re-grounded,
lowered, marked drifted, or superseded; it cannot silently retain current
Authority. A durable assumption keeps an owner, scope, and invalidation point. Routers expose edges and inherit
parent Authority; they do not copy current truth. Roadmap routes preserve future
delta and promotion gates without cloning Product, SSoT, Standards, ADR,
Architecture, or protocol authority. When an accepted decision changes another
Current Home, update it, record temporary drift, lower the affected claim, or
state why the impact does not apply; Docs Governance does not prescribe the
owners' implementation order.

Use [Lifecycle and Cleanup](references/lifecycle-cleanup.md) and, when future
material is involved, [Roadmap and Future Capsules](references/roadmap-and-future-capsules.md).

**Completion criterion:** each affected claim, representation, and scope has one canonical Current Home; retained source and
Evidence remain reachable, and no shadow Authority or unearned structure remains.

### Verify

Update affected routes and links. Check that discovery surfaces expose the
owners and current claims with proportionate context cost, and that stale claims
carry a disposition. Run the default audit when documentation
changed, convergence is claimed, or repository-wide mechanical coverage matters.
Run branch extensions only when the repository adopts them. Report blockers,
warnings, review signals, deliberate exceptions, and unproven claims.

**Completion criterion:** every declared route resolves, no unexplained blocker
remains, review signals have a disposition, and current claims have owning
Evidence or a lower classification.

## Local Claim Distinctions

```text
what implementation exists -> source, schema, migration, lockfile, generated artifact
what behavior was observed -> executed tests, Harness, runtime, release, operations
```

Product intent, shared semantics, binding rules, protocols, implementation, and
observed behavior remain question-scoped. A disagreement becomes documentation
drift, implementation gap, unaccepted implementation, obsolete source, or
missing Authority; it is not resolved by a universal file order.

## Optional References

- Current versus accepted-target/future classification: [Current vs Future](references/current-vs-future.md)
- Implementation-supported claims: [Source-Code Alignment](references/source-code-alignment.md)
- Explicit graph metadata or relation audit: [Artifact Graph](references/artifact-graph.md)
- Future capability routes: [Roadmap and Future Capsules](references/roadmap-and-future-capsules.md)
- Context cost, freshness, assumptions, and invalidation: [Knowledge Freshness and Context Legibility](references/knowledge-freshness-and-context-legibility.md)

## Default Audit

```bash
python3 scripts/run_docs_audit.py --repo <repo>
```

The audit is read-only and only blockers fail. Read the [package README](README.md)
for optional Artifact Graph/readability branches. Semantic Authority remains
Agent-reviewed.

## Output Contract

```text
classification table
question-scoped Authority decisions
Route / Layer / Partition / Identity admissions
moves, merges, flattening, retention, deletion, or blocks
current / accepted-target / future changes
source and Evidence backlinks
route and link updates
audits, exceptions, stale-map dispositions, invalidation triggers, unproven claims, and remaining decisions
```

Documentation convergence proves routing, ownership, and terminology. Runtime,
test, migration, release, and production claims require their owning Evidence.
