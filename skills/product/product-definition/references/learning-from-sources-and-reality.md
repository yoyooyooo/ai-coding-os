# Learning from Sources and Reality

> **Requirements Are Learned, Not Mined. Accepted Meaning Comes from Accountable Decision.** Sources, current behavior, and observation reveal the problem; accountable decisions turn that learning into accepted meaning.

Product understanding is synthesized from evidence, not copied from the loudest or newest input.

## Input classes

```text
stakeholder statement       intention, pain, expectation, or proposed solution
legacy document             historical model that may still contain domain knowledge
current implementation      executable reality, including drift and accidental behavior
runtime observation         bounded evidence from real use
external policy or law      binding only within its actual scope and effective version
prototype or AI-generated UI candidate interaction and vocabulary, not production truth
support/operations data     recurring pain and exceptions, not automatically the preferred solution
```

## Separate fact, interpretation, and decision

For each material claim, distinguish:

```text
Observed fact     what was directly seen or supplied
Interpretation    what the evidence may mean
Decision          what the accountable owner accepts as product meaning
Unknown           what could change the decision
```

Do not turn interpretation into fact through fluent prose.

## Contradictions are valuable

When sources conflict, do not prematurely average them. The conflict may reveal:

- different scopes or user groups;
- current behavior versus desired behavior;
- policy versus implementation;
- terminology drift;
- an exception that the main flow ignored;
- a legacy workaround that users now depend on;
- an unresolved authority dispute.

Preserve the conflict until the product meaning can be scoped and decided.

## Tacit expectations

Users often omit what feels obvious to them:

```text
who may see the data
what happens after interruption
whether partial work is preserved
what "complete" means
how exceptions are escalated
which manual workaround remains necessary
what counts as legal or acceptable evidence
```

Observe real work, ask for concrete examples, and examine recovery behavior rather than relying only on meeting-room descriptions.

## Current implementation as a learning surface

Source can reveal hidden concepts, state transitions, and user dependencies. It also contains historical accidents. Ask:

```text
is this behavior intentionally accepted?
who depends on it?
what rule or constraint explains it?
what would break if it changed?
is there evidence beyond the code path itself?
```

## Feedback revision

Requirements remain revisable. When real use changes understanding:

```text
preserve the new observation
identify which accepted meaning it challenges
update the product model through the accountable owner
align affected source, tests, and documentation
```

A signed document proves that a document was signed; it does not prove shared understanding forever.

## Related knowledge

- Use [Outcome and accepted meaning](outcome-and-accepted-meaning.md) to distinguish requested means from outcomes.
- Use [Product language and model](product-language-and-model.md) to stabilize concepts exposed by sources.
- Use [Decision boundaries and responsibility](decision-boundaries-and-responsibility.md) when authority is unclear.
- Use `$docs-governance` for Current Homes, source roles, and freshness.
- Return to the [Product Definition map](../SKILL.md).
