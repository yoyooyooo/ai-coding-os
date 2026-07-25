# Skill Eval Contract

Every `evals/*.json` file uses one shape:

```json
{
  "schema_version": 1,
  "skill_name": "skill-name",
  "evals": [
    {
      "id": "stable-case-id",
      "prompt": "User request",
      "expected_output": "Behavior and boundary expected from the Skill",
      "expectations": ["Optional independently reviewable behavior"],
      "files": ["Optional fixture or source hints"]
    }
  ]
}
```

`id` may remain an integer for compatibility with existing files or use a
stable string. IDs are unique across all eval files belonging to one Skill.
`expected_output` describes behavior, handoff, claim boundary, and refusals when
material; it is not a keyword snapshot.

Composition cases use the same schema and belong to the Router's eval assets.
That placement tests routing and owner separation without making the Router an
execution engine.
