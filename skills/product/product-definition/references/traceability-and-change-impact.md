# Traceability and Change Impact

Traceability is a risk-control tool, not a documentation ritual. Use the minimum depth that lets the team explain why a requirement exists, how it is accepted, and what must change when a decision moves.

## When traceability earns its cost

Use stronger traceability when one or more apply:

```text
regulated or safety-sensitive behavior
high privacy, financial, legal, or operational risk
several teams or vendors implement one workflow
frequent scope or policy change
long-lived product with migration obligations
formal business acceptance or auditability needs
complex permissions, state machines, or metrics
```

For a small low-risk product, source links and acceptance sections inside the PRD may be enough.

## Traceability chain

A full chain may be:

```text
source → source claim → issue/question → decision → requirement
→ rule/state/metric → acceptance criterion → test/UAT → release/runtime evidence
```

Product definition owns the chain through acceptance expectation. Delivery owners provide actual test, release, and runtime evidence. An RTM may reference a `$ai-coding-os-suite-contracts` Evidence Envelope or its `source_ref`/`evidence_refs`; the Product artifact does not copy Harness or execution-method status and does not promote current behavior into accepted target intent.

## Coverage questions

Ask:

```text
Does every material accepted requirement have a source, decision, or explicit product rationale?
Does every durable decision appear in the affected baseline or specification?
Does every high-risk rule or state transition have acceptance coverage?
Does every UAT scenario map to a business outcome rather than only a page?
Are future candidates excluded from current acceptance?
Are superseded decisions and requirements clearly retired?
```

## Stable identifiers

Identifiers should be:

```text
unique within the project scope
stable across file moves
human-readable enough to discuss
independent of sprint, ticket, page order, or implementation module
never silently reused after retirement
```

Use references such as `@PDR-<number>` when a mechanical scanner should verify them. Keep identifier schemes repository-specific when one already exists.

## Orphan patterns

Review:

```text
accepted decision with no updated specification
accepted requirement with no acceptance criterion where one is needed
acceptance criterion with no requirement or business rationale
UAT scenario that tests no accepted outcome
active PRD still referencing a superseded decision
metric or rule defined differently in several places
future candidate accidentally included in current acceptance
```

## Change-impact assessment

When accepted behavior changes, assess:

```text
version scope and roadmap
actors and responsibilities
object definition and relationships
workflow, handoff, state, and reversibility
rules, validation, calculations, and enumerations
permissions and data visibility
metrics and reporting
files, notifications, logs, and generated artifacts
quality attributes
migration, historical data, deprecation, and compatibility
design, architecture, API/data contracts, engineering, test, training, and operations
```

Product definition records product impact and required handoffs. Adjacent owners estimate and design their technical or operational changes.

## Closing a change

A change is product-complete when:

```text
the decision and effective version are clear
all affected product authorities are updated
superseded behavior is marked
acceptance and UAT are revised
adjacent handoffs are issued
remaining assumptions and delivery gaps are visible
```

Do not claim the feature delivered until the owning delivery process provides evidence. Even then, the evidence supports only its claim ceiling; Product acceptance, documentation lifecycle, execution-method completion, and release status remain separate owner decisions.

## Optional scanner convention

The included scanner recognizes explicit definitions such as headings or table rows beginning with supported IDs and explicit references written as `@ID`. It reports duplicate definitions and unresolved explicit references without interpreting semantic correctness.
