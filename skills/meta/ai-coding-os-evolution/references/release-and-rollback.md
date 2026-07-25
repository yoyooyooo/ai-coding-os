# Release and Rollback

A Suite release retains:

```text
Capability Profile
source tree and candidate lineage hashes
protected corpus and split manifests
Current / Candidate / Minimal / No-Suite comparisons
static audit and model-run Evidence
accepted and rejected changes
compatibility and not-evaluated boundaries
release manifest and checksum
rollback anchor
```

The last generated candidate is not automatically selected. Stage before adopt.
Automatic adoption requires explicit project policy, clean held-out gates, and a
trusted rollback path; it is not the default.
