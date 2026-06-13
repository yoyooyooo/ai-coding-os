# Evidence Harness

Evidence gates are part of architecture. They define which claims the system can
honestly make and where external output stops.

## Claim Ladder

Use the smallest honest level:

```text
static boundary check
unit / pure behavior
offline fixture
replay
adapter fake
db-backed / durable store
transport / projection
browser-visible / interface proof
real runtime opt-in
production-near smoke
```

A lower level can support a higher-level path, but it does not prove that higher
claim.

## Evidence Envelope

For meaningful architecture claims, capture:

```text
claim:
proof_path:
commands_run:
positive_tokens:
authority_checked:
boundary_checked:
fixtures_or_replay:
adapter_profile:
not_claimed:
not_proven:
diagnostics:
next_gap:
```

## Diagnostics

Diagnostics should answer:

- what happened;
- which authority accepted or rejected it;
- which candidate source produced it;
- which policy/version was used;
- which projection was updated;
- how to replay, invalidate, backfill, or recover;
- what sensitive data was excluded.

Do not store secrets, complete private prompts, full raw provider payloads, or
private reasoning as durable diagnostics unless a project explicitly requires
and secures that data.

## Harness Boundary

Harnesses can orchestrate checks, seed data, replay events, drive browsers, and
record evidence. They should not become an alternate materialization path for
business facts.

When harness support code needs privileged setup, state that it is setup only.
The proof path should still exercise the same application or product boundary
that production uses, unless the claim is explicitly lower.

## Not Claimed

Always state adjacent claims that a reader may over-infer.

Examples:

```text
real_runtime_claim=false
browser_ui_claim=false
production_auth_claim=false
provider_replaceability_claim=false
accepted_memory_write_claim=false
public_api_compatibility_claim=false
```

Use `not_proven` rather than `not_claimed` for boundaries that should be true
but were not checked.
