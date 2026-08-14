# Repository Agent Guide

## Project authority routes

- Product outcome and scope: `docs/product/product-brief.md`
- Shared doctrine, owners, and vocabulary: `docs/ssot/README.md`
- Current architecture of the Skill network: `docs/architecture/README.md`
- Binding documentation and Skill-writing conventions: `docs/standards/README.md`
- Accepted durable decisions: `docs/adr/README.md`
- Future candidates and promotion pressure: `docs/roadmap/README.md`
- Portable Skill entry points: `skills/**/SKILL.md`

## Stable local constraints

- Treat this repository as a self-navigating knowledge network, not a mandatory workflow.
- Keep the eight canonical semantic Skills and their ownership boundaries coherent.
- Treat `effect-server-module-design` as a model-visible supporting projection Skill, not a ninth semantic Owner.
- Use exact canonical English spellings for semantic anchors, paths, identifiers, and Skill prose.
- Project Docs use Chinese narrative prose while retaining canonical English terms where they carry shared meaning.
- Do not add a new Skill, template family, schema, registry, or first-level Docs Home without an earned pressure and an explicit owning Authority; a supporting projection must also state its upstream semantic Owners and non-owner boundary.
- Prefer improving project knowledge, source boundaries, commands, tests, logs, or tools before adding another instruction.

## Verification route

- Content and claim boundaries: `docs/standards/verification-policy.md`
- Source topology and naming: `docs/standards/source-topology-and-naming.md`
- Semantic compression rules: `docs/standards/semantic-compression.md`

## Intentional project choices

- This project keeps a small `roadmap/` only for genuine Future Candidates and their promotion pressure; it keeps no routine `reports/` Home because point-in-time release evidence is not part of the core knowledge surface.
- Architecture Decision Records use numeric filenames because durable decisions have stable citation pressure.
