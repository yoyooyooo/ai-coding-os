# Commerce Platform Preset Example

This example is the canonical rendered fixture for the Preset. It demonstrates:

- a thin project `AGENTS.md` entry;
- project-owned resolved Standards rather than dynamic Preset inheritance;
- canonical product language and source-token aliases;
- authority and writer mapping;
- actual Monorepo topology versus binding source-layout rules;
- Headless/UI Harness coverage that does not claim a real payment provider;
- a generated review-oriented architecture checker.

Regenerate:

```bash
python3 ../../scripts/preset.py render \
  --input preset-input.yaml \
  --overlay project-overlay.yaml \
  --out expected \
  --force
```
