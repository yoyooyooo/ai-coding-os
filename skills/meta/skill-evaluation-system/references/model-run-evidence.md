# Model-run Evidence

A reproducible result records:

```text
skill source SHA and candidate lineage
target and optimizer Agent Capability Profiles
Harness, tool permissions, repository snapshot, environment
corpus manifest and split hashes
seed / sampling / reasoning settings when controllable
trajectory and direct observations
hard and soft scores with evaluator identity
context, latency, token, tool-call, and escalation cost
improved / regressed / persistent-fail / stable-success categories
best-on-selection and final checkpoint separately
rejected proposals and rollback anchor
not_proven and known noise floor
```

Do not use a retrospectively inspected Test maximum as a deployable checkpoint
selection rule.
