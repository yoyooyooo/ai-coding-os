# 0.5.0-experimental.1 Upgrade Audit

## Scope

- Evaluated source: this distribution's `skills/**` and `docs/**`.
- Evaluated version: `0.5.0-experimental.1`.
- Evaluated at: 2026-07-26.
- Current basis: offline source inspection and deterministic local checks.

## Observed

- 17 Skill sources are present under the grouped layout.
- `$evolvable-application-architecture` is language-neutral at the core and contains a Rust projection.
- `$architecture-decision-system`, `$skill-evaluation-system`, and `$ai-coding-os-evolution` are present with Evals and References.
- Project Docs have Current Homes for Agent Legibility, ADIR, Skill evaluation, Suite evolution, Docs freshness, and Roadmap gates.
- Historical Goal Proof review-plan material was removed from the canonical current package because it no longer had an earned Current Home; accepted lessons remain in current ADRs, Standards, Evals, and Skill source.

## Supports

- The source package represents the accepted 0.5.0 experimental architecture and documentation model.
- The included offline checks can verify structure, links, schemas, profile closure, fixtures, source hygiene, deterministic packaging, and release provenance.

## Does Not Decide

- Whether the new Skills improve a particular model on real repository tasks.
- Whether Rust should already become an independent Skill.
- Whether ADIR should gain a portable machine Schema.
- Whether any candidate Suite may be auto-adopted.

## Not Proven

```text
independent model-run behavior
SkillOpt optimizer results
real Rust repository migration
cross-model transfer
production runtime behavior
automatic Suite evolution safety
```

## Final Verification

The exact executed commands, hashes, findings, and claim ceiling are recorded in `release/verification-summary.json`, `release/suite-audit.json`, `release/docs-audit.json`, and `release/manifest.json` in the delivered package. This report is invalidated if the source tree changes without regenerating those sidecars.
