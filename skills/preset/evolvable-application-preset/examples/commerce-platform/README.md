# Commerce Platform Preset Example

This example is the canonical rendered fixture for the Preset. It demonstrates:

- a thin project `AGENTS.md` entry;
- proposed Standards that require project-owner adoption rather than dynamic Preset inheritance;
- separate requested/defaults-added/dependency-added/resolved profile provenance and vocabulary filtered to that closure;
- candidate product language plus source-token aliases that reference rather than duplicate its meaning;
- a scoped Architecture `fact-authority-map`, not a global or SSoT Authority Map;
- actual Monorepo topology versus binding source-layout rules;
- Headless/UI Harness coverage that does not claim a real payment provider;
- a generated review-oriented architecture checker;
- an explicit broad `candidate-snapshot`: no generated file claims accepted/current status; only layers backed by overlay material are emitted, and child partitions or identity fields still require an earned-shape decision from `$docs-governance`.

Regenerate:

```bash
python3 ../../scripts/preset.py render \
  --input preset-input.yaml \
  --overlay project-overlay.yaml \
  --out expected \
  --force
```
