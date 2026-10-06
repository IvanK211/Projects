# Operating worksheet: Structured log triage and summary

**Scope:** Offline implementation. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Build a source-specific parser privately or manually normalize a small authorized sample.

**Step 2.** Keep a protected original if incident-handling requirements call for one; never use the public repository as an evidence vault.

**Step 3.** Inspect unrecognized severity and event labels, then run the aggregate summary.

**Step 4.** Compare time-normalized rates and recurrence after a corrective change, rather than comparing totals from unequal time windows.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Raw messages do not appear in the aggregate output. | Meets the stated criterion | Not run | Pending |
| Unknown labels remain visible. | Meets the stated criterion | Not run | Pending |
| No summary claims a root cause from frequency alone. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
