# Current vs Future Classification

## Purpose

Prevent current authority from drifting ahead of code while preserving long-horizon product and architecture thinking.

## Five Classes

### Current Fact

Exists in at least one authoritative implementation surface:

```text
product behavior
source/domain type
schema/migration
public or internal contract
real command/query path
test/replay fixture that exercises current code
```

Current facts belong in Product, SSoT, Architecture, Standards or Protocols according to role. A fixture alone does not prove product availability.

### Current Binding

An adopted constraint that already governs present implementation even when the full future capability is incomplete.

Examples:

```text
Runtime output is candidate-only.
Ordinary multi-Agent work does not automatically create InteractionRun.
Visibility, wake and turn graphs are separate.
Future Smart Routing cannot select Runtime implementation.
```

Current bindings may live in SSoT/ADR/Architecture/Standards if they have an accepted owner and real current applicability. Mark implementation state honestly.

### Future Candidate

A product hypothesis, complete future object model, unadopted protocol, quality target or deployment shape that is not current authority.

Place it in a Roadmap capability capsule. Do not use future language to imply current support.

### Active Proof

A selected slice currently being implemented or validated. The repository's
selected tracker/spec/execution method owns objective, progress, evidence,
claim ceiling and completion review. Roadmap links to that owner but does not
copy status. When a repository explicitly adopts Goal Proof System for the
slice, its Goal Pack is that owner.

### Historical Evidence

Past delivery, audit, experiment, rejected design source or immutable proof record. Place in Reports or Goal evidence/source material; it must not appear as current authority.

## Decision Test

Ask in order:

1. Can a user/code path rely on this today?
2. Does current code already have to obey it?
3. Has the tradeoff/protocol been formally adopted?
4. Is it only a future possibility or target?
5. Is it active work/evidence or past evidence?

When uncertain, do not promote the claim. Record it as future-candidate or decision-needed and preserve the source.

## Mixed Documents

A document may contain current and future material only when its layer explicitly supports it and boundaries are labeled. Prefer splitting when future detail is large.

Allowed examples:

```text
Architecture: current topology + clearly labeled accepted seam.
ADR: accepted decision + implementation_status partial.
Product: stable north star + explicit not-current availability.
```

Disallowed:

```text
SSoT containing an entire unimplemented future object graph.
Standard with no current command/check/applicable path.
Protocol described as canonical before adoption.
Report presented as current truth.
```

## Evidence Discipline

Documentation alignment can establish terminology and ownership, not implementation completion. Mark unverified claims and require code/test/runtime evidence through the appropriate workflow.
