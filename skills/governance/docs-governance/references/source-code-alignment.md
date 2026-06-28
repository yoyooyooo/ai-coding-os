# Source-Code and Docs Bidirectional Alignment

## Goal

Current docs should neither lag important public/domain changes nor describe capabilities that source and product paths do not support.

## Source to Docs

Review docs when code introduces or changes:

```text
public/domain object or authority owner
typed command/query/commit
schema or migration
runtime/relay/protocol contract
composition root/deployment profile
permission/visibility/trust boundary
product output lane or failure behavior
scenario proof/claim ceiling
```

Minimum owners:

- object/authority change -> SSoT and possibly ADR;
- execution topology -> Architecture;
- enforceable rule/command -> Standard;
- wire contract -> Protocol;
- user-visible semantic -> Product/Design/Interface capability;
- future but not current -> Roadmap capsule.

## Docs to Source

For each current claim, find at least one anchor:

```text
source file / type / function
schema / migration
command / route / DTO
current test or fixture
real runtime/product evidence, when availability is claimed
```

An accepted seam may be documented without full implementation, but must say what exists and what is not implemented.

## Alignment Matrix

For substantial convergence, produce a table:

| Claim | Class | Docs owner | Source/evidence anchor | Gap |
|---|---|---|---|---|
| ... | current-fact/current-binding/future | ... | ... | ... |

## Common Drift

```text
source object exists, docs omit authority owner
SSoT still describes deleted object
Architecture presents a library seam as production composition
Product says feature is available when only fixture exists
Standard has no current checker/command
Roadmap duplicates Goal status
Report/evidence is cited as current truth
future capsule repeats formal authority after promotion
```

## Audit Rules

- Validate relative Markdown links.
- Validate referenced repo paths when written as code anchors.
- Check duplicate current owners for the same term.
- Check ADR numbering and status.
- Check Future capsule names/indexes and shadow directories.
- Check current docs for phrases that overclaim implementation or production readiness.
- Check code concepts with no current docs owner; report, do not auto-invent product truth.

## Claim Ceiling

A docs-only pass may claim documentation convergence and static consistency. It cannot claim compile/test/migration/browser/runtime/production success unless corresponding evidence was actually executed and recorded.
