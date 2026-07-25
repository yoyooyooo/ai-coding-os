# Corpus and Split Integrity

## Splits

```text
Discovery / Train
  visible to reflection and candidate generation

Selection
  chooses or rejects candidates; answers hidden from optimizer

Sealed Release Test
  never used for candidate selection

Transfer / Canary
  other model profiles, Harnesses, repositories, or field use
```

Group semantic siblings into one `case_family`. Rephrasing one bug, cloning one
repository task, or generating variants from one answer does not create
independent samples.

## Contamination Ledger

Record:

```text
case_id and case_family
source and derived_from
split
seen_by_optimizer
seen_by_candidate_author
seen_by_evaluator
first_exposed_at
retired_or_rotated
corpus_manifest_sha256
```

Fail closed when sealed cases enter reflection or candidate context. An empty
Train/Selection set is safer than silently falling back to Test.
