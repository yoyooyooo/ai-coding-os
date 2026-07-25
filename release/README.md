# Release Evidence

This directory contains portable offline evidence for the complete source distribution.

- `manifest.json`: complete source identity, versions, counts, and verification routes.
- `verification-summary.json`: executed checks, supported claims, and explicit `not_proven`.
- `suite-audit.json`: canonical mechanical audit of `skills/**`.
- `docs-audit.json`: canonical Docs Governance audit of `docs/**` and project routes.
- `composition-eval-review.json`: declared cross-Skill composition contracts; independent model run remains `not_run`.
- `core-builder-evidence.json`: evidence from the deterministic Core builder; its temporary Core ZIP is intentionally not nested here.
- `SHA256SUMS`: hashes every delivered file except itself.

The SHA-256 of the complete outer ZIP is reported externally because an archive cannot contain its own final hash without circularity.
