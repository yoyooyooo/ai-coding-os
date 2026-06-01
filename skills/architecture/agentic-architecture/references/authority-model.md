# Authority Model

Authority is the right to define an accepted fact. Many layers can observe,
transport, cache, index, summarize, or display a fact without owning it.

## Authority Map

For every important object, write:

```text
fact:
owner:
allowed commands:
allowed projections:
candidate sources:
materialization path:
forbidden owners:
evidence:
not_claimed:
```

If this cannot be written, the architecture is not ready for broad agentic
automation.

## Common Fact Boundaries

### Domain Facts

Domain facts are owned by domain/application objects and accepted only through
application services, policy decisions, transactions, and audit paths.

Adapters, routes, UI state, runtime stdout, provider responses, memory search
results, logs, and caches are not domain fact authority.

### Memory Facts

Long-term memory should split at least these roles:

```text
source fact
-> memory candidate
-> policy decision
-> accepted memory entry
-> memory use / retrieval evidence
-> run context snapshot or equivalent resolved-input proof
```

External memory engines, vector stores, graph stores, search indexes, provider
native memory, file projections, and summaries may provide candidates or
retrieval evidence. They must not own accepted memory body unless the project
explicitly declares them as authority and accepts the security/replay cost.

### Runtime Facts

Agentic runtimes own opaque execution handles and protocol observations. They
do not own product completion, message truth, memory truth, permission grants,
or artifact provenance.

Runtime output should flow through:

```text
runtime event
-> normalized candidate
-> application materialization
-> event/audit/projection path
```

### Provider Facts

LLM providers can produce structured candidates, summaries, rankings, plans,
and usage diagnostics. They do not own domain facts merely because the response
is well-structured.

### Transport Facts

Transport owns delivery mechanics: pairing, signing, ack, reconnect, retry,
dedupe, cursor, or frame verification. It does not own business completion.

### Harness Facts

Harnesses prove claims under a stated ceiling. A harness command can prove a
slice of behavior; it does not become the product authority it tests.

## Stop Lines

Stop and ask, or require a higher-authority decision, when continuing would
change:

- product truth;
- public API, schema, protocol, or compatibility posture;
- security, permission, private-data, or retention posture;
- destructive or irreversible behavior;
- claim ceiling or completion standard;
- accepted authority for facts that currently have no owner.

Missing implementation detail is not automatically a stop line when a safe,
falsifiable proof path exists.
