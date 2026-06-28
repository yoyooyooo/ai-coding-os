---
name: docs-governance
description: >-
  Designs, converges, audits, and cleans repository documentation layers for long-running human-agent development. Use when creating or restructuring docs/*, separating current authority from future capability planning, preserving roadmap value without shadow SSoT, migrating obsolete planning trees, or validating links, indexes, lifecycle, evidence retention, and source-code alignment.
---

# Docs Governance

Converge documentation toward one current authority chain and one explicit future route. Do not own product truth, Goal Pack progress, implementation completion, or public protocol/security decisions.

## Operating Contract

```text
Owns:
  docs layer boundaries, placement, current/future classification,
  retention, indexes, source-code alignment audit and docs cleanup.

Does not own:
  product semantics, Goal Proof state/evidence, implementation status,
  legal/security retention or public API/protocol decisions.

Stop when:
  the highest authority is ambiguous, deletion risks unlinked evidence,
  or resolution requires a new product/security/public-contract decision.
```

## Workflow

1. Read `AGENTS.md`, `docs/README.md`, layer READMEs and any repo-local docs policy.
2. Classify every affected claim:
   - `current-fact` — exists in product/code/schema/tests/runtime path;
   - `current-binding` — adopted constraint that already governs current work;
   - `future-candidate` — not current authority;
   - `active-proof` — Goal Proof owns progress/evidence;
   - `historical-evidence` — report/source/evidence only.
3. Place by semantic owner; never keep two current homes.
4. For future work, preserve sequence/gates in Roadmap capability capsules rather than copying `future/ssot`, `future/standards`, or other shadow layers.
5. Before move/delete, assign lifecycle and retention verdict; preserve source/evidence backlinks.
6. Update layer README/index, conflict order, promotion/demotion path and code anchors.
7. Run the audit scripts and report blockers, warnings, deliberate exceptions and unverified claims.

## Placement

```text
current product meaning                -> docs/product/**
current object/fact authority           -> docs/ssot/**
current executable rule/check/command   -> docs/standards/**
adopted tradeoff                        -> docs/adr/**
current topology / accepted seam        -> docs/architecture/**
wire schema/profile/media type          -> docs/protocols/**
UI/UX/visual behavior                   -> docs/design/**
future sequence/gate/capability capsule -> docs/roadmap/**
active goal/progress/evidence            -> docs/goal-proof/**
past audit/delivery/validation           -> docs/reports/**
implementation checklist                -> root specs/** or Goal work item
```

## Future Rule

`docs/roadmap/future/<capability>/README.md` is an active route, not current authority. It uses the same governance questions as formal docs but does not reproduce their directory hierarchy. Promotion moves accepted authority into Product/SSoT/ADR/Architecture/Standards/Protocols and shrinks the capsule to remaining future delta.

## Required Reading

- Layer placement/conflict order: [Docs Layer Model](references/docs-layer-model.md)
- Current vs future classification: [Current vs Future](references/current-vs-future.md)
- Roadmap capsules/promotion: [Roadmap and Future Capsules](references/roadmap-and-future-capsules.md)
- Source/docs bidirectional alignment: [Source-Code Alignment](references/source-code-alignment.md)
- Retention/migration/deletion: [Lifecycle and Cleanup](references/lifecycle-cleanup.md)
- Human-agent operating flow: [Human-Agent SOP](references/human-agent-sop.md)
- Frontmatter/relations: [Artifact Graph](references/artifact-graph.md)

## Deterministic Audit

```bash
python3 scripts/run_docs_audit.py --repo <repo>
python3 scripts/scan_future_capsules.py --repo <repo>
python3 scripts/scan_docs_links.py --repo <repo>
python3 scripts/scan_source_doc_anchors.py --repo <repo>
python3 scripts/artifact_graph.py audit --repo <repo>
```

The reusable audit may report project-specific warnings. Repo-local wrappers may add policy or exceptions but must not fork generic layer doctrine or encode product truth.

## Output

Return:

```text
classification table
placement/retention decisions
moves/deletions/additions
authority and future-route changes
source/evidence backlinks
index/link updates
audit results and unresolved decisions
```

Do not claim implementation, tests, migration, browser, Runtime or production evidence merely because documentation was converged.
