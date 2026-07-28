# Feedback Horizon

> **Feedback Horizon Sets the Safe Step Size — Do Not Outrun Your Headlights.** Do not outrun the distance at which a wrong change becomes visible and can still be stopped or recovered.

The safe size of an Agent's next change is determined by how quickly it can learn that it is wrong and how easily it can stop or recover.

## Horizon dimensions

```text
feedback latency       time from change to trustworthy result
failure localization   how precisely the result identifies the wrong boundary
reversibility          cost of stopping or reverting
external impact        whether data, money, users, or providers are affected
concurrency             whether other work can invalidate the observation
coverage honesty       whether the surface actually exercises the changed property
```

## Longer safe steps

An Agent may take a larger coherent step when:

```text
accepted meaning is clear
boundaries and ownership are discoverable
changes are local and reversible
focused verification is fast and precise
no irreversible external effect occurs
the working tree/diff provides a clear recovery point
```

## Shorter safe steps

Use a smaller step when:

```text
persistent data or public contracts change
provider outcome may be unknown
feedback is slow or flaky
many owners or state dimensions interact
recovery is uncertain
security, privacy, financial, or legal risk is material
```

One line can require a very short horizon if it is an irreversible migration. Many files can remain one safe step if they are a mechanical, strongly verified rename.

## Checkpoints are evidence boundaries

A useful checkpoint is a state where the project is understandable, the diff is reviewable, and the relevant property can be observed. Do not impose a fixed time or file count.

## Feedback must change the next action

A check that is recorded but ignored is not a feedback loop. When evidence contradicts the plan, revise the model or stop.

## Related knowledge

- Use [Default project verification interface](default-project-verification-interface.md) for fast command slots.
- Use [Choosing an observation surface](choosing-observation-surface.md) to select the property.
- Use [Observation limits](observation-limits.md) for evidence honesty.
- Use `$evolvable-application-architecture` for reversibility and migration.
- Return to the [Harness map](../SKILL.md).
