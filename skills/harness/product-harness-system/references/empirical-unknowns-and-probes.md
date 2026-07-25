# Empirical Unknowns and Probes

A Probe Request closes an empirical gap without pretending to decide product or
architecture semantics.

```text
question
scope and decision it may inform
formal entrypoint or observation boundary
dependency reality and environment
controlled variation or failure injection
direct observations to capture
supports if observed
does_not_decide
not_proven
claim ceiling
```

Examples:

```text
Can the provider complete after local timeout?
Does duplicate delivery survive process restart?
Does realtime cursor recovery backfill a missed projection?
Does graceful shutdown wait for owned child tasks?
```

A probe can establish behavior. It cannot decide whether the product should
allow another retry, what completion means to a user, or which policy is
accepted.
