# Protected Failure Corpus

A protected failure records why a rule, interface, or boundary exists:

```text
failure_id and case family
observed behavior and impact
semantic owner
minimal reproducer or task
current protection
proof surface and evaluator
first fixed version
regression severity
```

Include historical human corrections, authority confusion, false proofs,
incorrect routing, silent assumptions, destructive migration risks, and context
failures that materially changed outcomes.

Do not protect every preference or one-off style choice. Retire a failure only
when its underlying pressure no longer belongs to the supported Suite or a
stronger mechanism replaces the instruction.
