# Default Project Verification Interface

Every project should make its verification surface discoverable through `AGENTS.md`, the root README, or the native command system. The portable contract is the command role, not one package-manager spelling.

## Default command slots

```text
install                      reproduce project dependencies
format/lint                  normalize and check local source conventions
static/type check            compile or validate types/schema without full runtime
unit/integration test        run the project's normal focused automated tests
architecture/boundary check  enforce import/public/ownership rules when present
affected verification        run the smallest trustworthy set for current changes
full verification            run the complete project-owned verification set
```

Not every repository needs a separate command for every slot. Map equivalent commands clearly.

## Preferred canonical aliases

When the project can expose stable scripts, prefer:

```text
verify:affected
verify
```

These may delegate to package-manager, Make, task runner, or repository scripts.

## Command properties

A durable command should have:

```text
stable exit status
readable text output
non-interactive default behavior
clean-environment reproducibility
--help or equivalent discovery
explicit dependency reality
bounded resource and timeout behavior
```

Destructive commands should default to read-only or `--dry-run` and require explicit opt-in.

## Verification output

Report enough to act:

```text
what command ran
what scope it covered
which dependencies were fixture/fake/replay/local-real/external-real
what failed first
where detailed output lives
what was skipped or remains unproven
```

Avoid a single opaque "all checks passed" wrapper that hides the failing boundary.

## Affected verification

Affected verification may use source graph, package boundaries, test selection, or explicit scope. It must fail closed or state uncertainty when it cannot determine impact reliably.

## Full verification

Full verification is the repository's broad confidence surface, not proof of product success. It should be scriptable from a clean checkout when practical.

## Project Standard

When command roles and claim boundaries are durable across contributors or CI, adopt them in `docs/standards/verification-policy.md` using the [verification policy template](../templates/verification-policy.md). Keep actual commands project-owned.

## Project override

Preserve existing commands when they are coherent. Record the mapping once in `AGENTS.md`. Do not rename working commands merely to match the aliases.

## Template and example

- Use the `$docs-governance` `AGENTS.md` template for project mapping.
- See the [verification interface example](verification-interface-example.md).

## Related knowledge

- Use [Command and probe design](command-and-probe-design.md) for individual commands.
- Use [Feedback horizon](feedback-horizon.md) for affected versus full verification.
- Use [Observation limits](observation-limits.md) for claims.
- Use `$docs-governance` for repository entry and command placement.
- Return to the [Harness map](../SKILL.md).
