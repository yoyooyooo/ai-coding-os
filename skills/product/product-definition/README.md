# product-definition

Version: **2.2.2**

A project-agnostic Skill for turning ambiguous product inputs into honest version baselines, coherent product models, decision-ready alignment, modular PRDs, measurable acceptance, and proportionate traceability. It infers ordinary reversible detail from current Authority, isolates only materially undecidable claims, and distinguishes source-derived implementation from observed behavior.

It is designed to complement documentation-governance, design, architecture, engineering, security, data, QA, and release skills without taking over their authority. Its artifacts are destination-neutral: place them wherever the repository already establishes product, decision, SSoT, design, architecture, or quality homes.

## Core model

```text
Baseline   accepted product target for a version
Model      actors, objects, workflows, states, rules, permissions, artifacts, metrics, and quality
Challenge  conflicts, gaps, assumptions, edge cases, drift, and risks
Trace      source and decision links through requirement and acceptance
```

## Entry point

Read `SKILL.md`. Load only the reference and template needed for the current product pressure.

## Included references

- artifact selection and baseline readiness
- source synthesis and product-truth promotion
- scope and version baselines
- product modeling
- workflow, exception, and recovery modeling
- business rules, permissions, metrics, and quality attributes
- challenge, recommendation, and decision preparation
- stakeholder alignment and decision closure
- PRDs, acceptance criteria, and UAT
- traceability and product change impact
- product boundaries and handoff to adjacent owners

## Included templates

See [`templates/README.md`](templates/README.md) for the selection guide. The package includes product briefs, source synthesis, scope baselines, clarification registers, decision packets, PDRs, product models, workflow and state specifications, rule catalogs, RACI and permission matrices, metric dictionaries, quality requirements, module PRDs, design handoffs, acceptance criteria, UAT scenarios, traceability matrices, change-impact assessments, and alignment meeting packs.

## Self-check

```bash
python3 scripts/self_check.py
```

The self-check uses only the Python standard library. It validates required package files, JSON/YAML-like metadata shape used by the Skill, local Markdown links, template inventory, and Python compilation without leaving bytecode in the Skill tree.

## Optional product artifact audit

```bash
python3 scripts/scan_product_artifacts.py --root /path/to/repository
```

The scanner is deliberately conservative and structure-neutral. It scans common text artifact formats for:

- duplicate explicit product identifiers;
- unresolved explicit references written as `@ID`;
- accepted Markdown artifacts that still contain obvious placeholders;
- malformed local Markdown links.

Use `--json` for machine-readable output. Use `--strict` to return exit code 1 for duplicate definitions, unresolved explicit references, or broken local links. The scanner does not judge semantic product truth, approval, implementation, or release status.

## Dependencies

No third-party runtime dependencies are required.
