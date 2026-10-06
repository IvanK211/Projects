# Operating worksheet: Sensor calibration and drift logging

**Scope:** Offline implementation + measurement schema. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Use the manufacturer calibration procedure and independently record reference condition, temperature and time.

**Step 2.** Keep repeated readings from the same sample distinct from measurements of different samples.

**Step 3.** Run the synthetic series and inspect units and timestamp offsets before introducing privately collected observations.

**Step 4.** Change one experimental factor at a time and retain uncertainty, instrument resolution and stabilization criteria in the private log.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Different units never share one statistical group. | Meets the stated criterion | Not run | Pending |
| Non-finite readings and missing timestamps are rejected. | Meets the stated criterion | Not run | Pending |
| Zero elapsed time gives unknown drift rather than a divide-by-zero or invented trend. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
