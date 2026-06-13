import { readFileSync } from "node:fs";
import { appendEvidenceRecord, applyGoalProgress, loadGoalPack, validateGoalPack, validateGoalPackPreview } from "./lib/goal-pack.ts";

export function runAppendEvidence(goalRoot, { file = null, json = null, stdin = false, apply = false, check = false, dryRun = false } = {}) {
  const inputCount = [file, json, stdin].filter(Boolean).length;
  if (inputCount !== 1) throw new Error("evidence add requires exactly one input source: --file <path>, --json '<json>', or --stdin");

  const input = file ? readFileSync(file, "utf8") : stdin ? readStdin() : json;
  const evidenceRecord = JSON.parse(input);
  const recorded = appendEvidenceRecord(goalRoot, evidenceRecord, { dryRun });
  const applied = apply ? applyGoalProgress(goalRoot, { dryRun, evidenceRecord: dryRun ? evidenceRecord : null }) : null;
  const validation = check
    ? dryRun
      ? validateGoalPackPreview(goalRoot, {
        progressText: applied?.progress_text ?? null,
        evidenceRecord,
      })
      : validateGoalPack(loadGoalPack(goalRoot))
    : null;
  return {
    ...recorded,
    applied,
    check: validation,
    changed_paths: [
      ...(recorded.changed_paths || []),
      ...(applied?.changed_paths || []),
    ],
  };
}

function readStdin() {
  if (process.stdin.isTTY) throw new Error("--stdin requires JSON input on stdin");
  const input = readFileSync(0, "utf8");
  if (input.trim().length === 0) throw new Error("--stdin requires JSON input on stdin");
  return input;
}
