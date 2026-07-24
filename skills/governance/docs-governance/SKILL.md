---
name: docs-governance
description: >-
  Documentation convergence for repository docs layers and AGENTS.md. Use when
  creating, restructuring, migrating, or auditing current authority, future
  candidates, Preset-resolved standards, indexes, links, retention, cleanup, or
  source-code alignment.
---

# Docs Governance

Converge documentation toward one current authority chain and one explicit
future route. This skill governs where information belongs and how it lives;
the semantic owner governs what it means.

## Ownership

```text
Owns:
  docs layer boundaries and placement
  current/future classification
  AGENTS.md operational-entry governance
  Preset-resolved standard placement and lifecycle
  retention, indexes, source alignment, cleanup, audit

Adjacent owners:
  application/source semantics -> owning architecture skill
  Goal Pack state -> $goal-proof when explicitly adopted
  Preset defaults -> $evolvable-application-preset
  product truth, contracts, security, and implementation -> project authority
```

Stop when the highest authority is ambiguous, retention policy is unresolved,
or the change requires a new product, security, public-contract, privacy, or
destructive decision.

## Convergence Pass

| Step | Completion criterion |
| --- | --- |
| Ground | `AGENTS.md`, `docs/README.md`, layer indexes, local policy, and affected sources are read. |
| Classify | Every affected claim is labeled `current-fact`, `current-binding`, `future-candidate`, `active-proof`, or `historical-evidence`. |
| Place | Each claim has one semantic owner and one current home; future candidates have one route rather than a shadow authority tree. |
| Retain | Every move, replacement, or removal has a lifecycle verdict and preserves required source/evidence backlinks. |
| Rewire | Nearest indexes, conflict order, promotion/demotion path, links, and code anchors point to the resulting authority. |
| Verify | Relevant audit scripts run; blockers, warnings, deliberate exceptions, and unverified claims are reported. |

## Placement

```text
current product meaning                -> docs/product/**
current object/fact authority          -> docs/ssot/**
current executable rule/check/command  -> docs/standards/**
adopted tradeoff                       -> docs/adr/**
current topology / accepted seam       -> docs/architecture/**
wire schema/profile/media type         -> docs/protocols/**
UI/UX/visual behavior                  -> docs/design/**
future sequence/gate/capability        -> docs/roadmap/**
active work/progress/evidence           -> configured execution method
past audit/delivery/validation         -> docs/reports/**
implementation checklist               -> root specs/** or owning artifact
```

## Orthogonal Ownership

For project files such as:

```text
docs/standards/architecture-profile.yaml
docs/standards/source-topology-and-naming.md
docs/standards/naming-vocabulary.yaml
```

`$docs-governance` owns placement, indexing, conflict, and lifecycle;
architecture skills own semantics; `$evolvable-application-preset` may provide
reusable defaults; the resolved project file is current authority.

## Topology Routing

```text
cross-project architecture meaning -> owning architecture skill
language/framework mapping -> technology specialist
binding directory/import/naming rule -> docs/standards/**
actual apps/packages/modules/runtime graph -> docs/architecture/**
fact/writer ownership -> docs/ssot/**
adoption reason -> docs/adr/**
future split or migration -> docs/roadmap/**
file-level implementation -> specs/** or selected execution method
```

## AGENTS.md

Keep `AGENTS.md` as a thin operational entry containing the adoption statement,
read-first path, stable working rules, resolved commands, language policy, and
an optional `$ai-coding-os` pointer. SSoT, complete Standards, topology, skill
registry, progress state, task history, and private tool configuration remain in
their owning homes.

A Preset may manage one marked section. The merged file belongs to the project.
Nested entries are admitted for real local command, lifecycle, security/write,
framework-path, or verification differences and describe only the delta.

## Preset and Future Boundaries

```text
skill doctrine
  -> reusable Preset defaults
  -> resolved project docs and AGENTS.md
  -> source/check/evidence alignment
```

Preset upgrades stage a candidate render and semantic diff against the current
resolved project. They never dynamically change project authority.

`docs/roadmap/future/<capability>/README.md` is a route, not current authority.
Promotion moves accepted meaning into Product, SSoT, ADR, Architecture,
Standards, or Protocols and leaves only the remaining future delta.

## Read When Needed

- Layer placement or conflict: [Docs Layer Model](references/docs-layer-model.md)
- Current versus future: [Current vs Future](references/current-vs-future.md)
- Roadmap capsules and promotion: [Roadmap and Future Capsules](references/roadmap-and-future-capsules.md)
- Source alignment: [Source-Code Alignment](references/source-code-alignment.md)
- Retention, migration, or cleanup: [Lifecycle and Cleanup](references/lifecycle-cleanup.md)
- Repository operating flow: [Human-Agent SOP](references/human-agent-sop.md)
- Frontmatter and relations: [Artifact Graph](references/artifact-graph.md)
- Agent entry or Preset adoption: [Agent Entry and Preset](references/agent-entry-and-preset.md)

## Audit Commands

```bash
python3 scripts/run_docs_audit.py --repo <repo>
python3 scripts/scan_agent_entry.py --repo <repo>
python3 scripts/scan_future_capsules.py --repo <repo>
python3 scripts/scan_docs_links.py --repo <repo>
python3 scripts/scan_source_doc_anchors.py --repo <repo>
python3 scripts/artifact_graph.py audit --repo <repo>
```

## Output

```text
classification
placement_and_retention
moves_replacements_additions
authority_and_future_route_changes
AGENTS_or_preset_snapshot_changes
source_and_evidence_backlinks
index_and_link_updates
audit_results
unresolved_decisions
not_claimed
```

Documentation convergence supports only documentation claims; implementation,
test, migration, browser, runtime, and production claims require their own
evidence.
