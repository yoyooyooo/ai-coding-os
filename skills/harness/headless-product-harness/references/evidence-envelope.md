# Evidence Envelope

Use this reference only when defining JSON / JSONL output shape for headless
proof commands.

Owner split:

- SSoT / Goal Proof own the cross-method Evidence Envelope Discipline.
- Headless Product Harness owns the command JSON / JSONL output shape for
  headless proof commands.

This file imports the canonical discipline; it does not define completion
review, harness promotion, or cross-method claim rules. For Goal Proof
completion reviews, use SSoT / Goal Proof wording. In those reviews, `changed
surfaces` and `not_proven` are narrative envelope concepts unless schema,
templates, and checkers are explicitly upgraded.

For headless proof commands, emit the JSON / JSONL envelopes below. Do not use
the command envelope as a checklist. It exists to keep command claims honest
without turning the command into product truth.

## Success Envelope

```json
{
  "ok": true,
  "command": "smoke offline-import",
  "target_slice": "offline-import-core",
  "claim_ceiling": {
    "level": "headless_product",
    "headless_sublevel": "offline_fixture",
    "environment": "local"
  },
  "positive_tokens": [
    "profile_loaded=true",
    "normalized_evidence_records_created=true"
  ],
  "not_claimed": [
    "browser_ui_claim=false",
    "real_runtime_claim=false"
  ],
  "not_proven": []
}
```

## Failure Envelope

```json
{
  "ok": false,
  "command": "source analyze",
  "error": {
    "code": "SOURCE_FILE_NOT_FOUND",
    "message": "source file does not exist"
  },
  "next_action": "check --source path or run source inventory"
}
```

Failure must return non-zero. Do not print uncaught stack traces, bare errors,
HTML, color logs, or mixed human prose as the default agent-facing output.

## JSONL Long Runs

Use JSONL only when the command streams progress. The final line must be a
terminal summary with `ok`, `command`, `target_slice`, `claim_ceiling`,
`positive_tokens`, `not_claimed`, and `not_proven`.

## Evidence Tokens

Evidence should be machine-readable and grep-friendly:

```text
target_slice=channel-realtime
snapshot_received=true
incremental_event_received=true
terminal_summary_seen=true
browser_ui_claim=false
```

Tokens may appear inside JSON fields or structured logs. They must reflect work
actually executed by the command.

Positive tokens require an executed path. Do not print a token for a state that
was assumed, skipped, hardcoded, or only described in a report. If a check is
manual, mark it as manual evidence and keep `claim_ceiling` explicit.

## Not Claimed

Include `not_claimed` tokens whenever adjacent surfaces are easy to overclaim:

```text
browser_ui_claim=false
db_claim=false
scheduled_sync_claim=false
runtime_mapping_ui_claim=false
real_runtime_claim=false
product_completion_claim=false
```

`not_claimed` tokens are not decoration. Emit one only when the command
actually checked or structurally bounded that surface. If the command did not
check the boundary, put it in `not_proven` or the report boundary instead of
printing a false token.

`not_claimed` limits what later agents may inherit from the evidence. It does not
prove product failure; it only says the current command did not prove that
surface.
