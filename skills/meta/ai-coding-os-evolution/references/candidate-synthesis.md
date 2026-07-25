# Candidate Synthesis

A Suite candidate may change one Skill or a coordinated bundle. It must name:

```text
change radius E0-E4
semantic owners affected
source, references, evals, contracts, templates, tooling, and docs coverage
protected failures
expected context/behavior effect
compatibility impact
rejected alternatives
verification and rollback
```

Do not let a central evolution Skill directly rewrite domain semantics without
their owner. Preserve rejected proposal reasons so later epochs do not repeatedly
rediscover disproven changes.
