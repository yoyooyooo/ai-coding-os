# Release Evidence

> Historical pre-import evidence. These files do not describe or verify the current content-only 8-Skill network.

`release/` intentionally contains only five files:

- `manifest.json`: source identity、12/6 invocation surface、verification routes、Core archive hash 和 Claim Ceiling。
- `suite-audit.json`: canonical mechanical audit of `skills/**`。
- `docs-audit.json`: canonical Docs Governance audit。
- `SHA256SUMS`: delivered source and sidecar hashes。
- `README.md`: this boundary。

Static Eval corpora、per-case migration maps、coverage matrices、unexecuted behavior
plans and duplicate change reports are not release Evidence. `behavior_evidence`
remains `not_run` in the manifest unless a claim-bounded model run actually exists.
