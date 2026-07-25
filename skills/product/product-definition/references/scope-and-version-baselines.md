# Scope and Version Baselines

A scope baseline defines the accepted product target for a stated version or horizon. It is not a feature wish list, project plan, implementation inventory, or release proof.

## Required distinctions

Keep these categories explicit:

```text
current verified behavior       what exists now, whether accepted or not
retained current behavior       existing behavior intentionally kept in the target
new in-scope behavior           capability to be added or changed in this version
out of scope                    explicitly excluded from the version
future candidate                possible later capability without a current commitment
retiring or deprecated behavior existing behavior intended to be removed or migrated
blocked scope                   desired behavior awaiting a binding decision or dependency
```

## Version goal

A good version goal states an observable outcome, target users, and boundary. Avoid goals that simply repeat a list of pages or components.

Example shape:

```text
For <users>, enable <end-to-end outcome> within <scope boundary>,
while excluding <explicit non-goals> and depending on <named prerequisites>.
```

## Capability scope table

| Capability | Current status | Target treatment | Version | Users | Dependencies | Decision/source | Acceptance exit |
| --- | --- | --- | --- | --- | --- | --- | --- |

Target treatment values:

```text
retain
introduce
change
migrate
retire
exclude
defer
blocked
```

## Slice by outcome, not navigation

Prefer a thin end-to-end outcome over several disconnected pages. A usable version normally crosses the minimum set of actors, objects, rules, and handoffs required to complete a business result.

Check that the slice includes:

```text
entry trigger
actor ability to complete the main outcome
minimum required approvals or handoffs
state and exception handling
essential permissions and data visibility
required notifications, files, or generated artifacts
observable completion and acceptance
```

## Dependencies and assumptions

Each material dependency or assumption should include:

```text
owner
needed-by date
impact if unavailable
fallback or reduced-scope option
whether it blocks the whole version or only one capability
```

Temporary assumptions need an expiry or decision point. Do not let them silently become permanent requirements.

## Entry and exit criteria

A version baseline may define:

```text
entry criteria   decisions, source access, design input, technical feasibility, or data readiness needed to start
exit criteria    acceptance, UAT, migration, training, or operational conditions needed to claim the product outcome
```

Product definition owns the expected product exit, not the proof that delivery has passed it.

## Scope-change triggers

Use a change-impact assessment when a proposal changes one or more of:

```text
version goal
in-scope or out-of-scope capability
user group or market
business object meaning
workflow or state
permission boundary
business rule or metric definition
quality target
acceptance or roadmap promise
```

Do not update only the most visible PRD. Trace the change into all affected product artifacts.

## Roadmap honesty

A roadmap item is not a baseline unless its scope, owner, decision status, and version commitment are accepted. Label exploratory or future candidates honestly and avoid detailed pseudo-PRDs that make optional work look committed.
