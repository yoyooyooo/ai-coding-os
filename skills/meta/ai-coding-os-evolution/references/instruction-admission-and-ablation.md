# Instruction Admission and Ablation

For each candidate instruction, ask:

```text
Which invariant or protected failure does it serve?
Is it applicable to most calls of this Skill?
Can an interface, Tool, type, test, or Reference own it better?
Does another Skill already own the same meaning?
What happens when it is removed or loaded only on demand?
What context and output cost does it create?
```

Run instruction and context ablations against protected cases. Preserve equal or
better behavior with less context. Avoid replacing one long rule with several
synonymous reminders.
