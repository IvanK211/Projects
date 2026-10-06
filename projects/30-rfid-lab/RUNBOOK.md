# Operating worksheet: MFRC522 checker, reader and guarded lab writer

**Scope:** Three Arduino sketches; hardware build unverified. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Check breakout supply and logic-level specifications; a board powered at the correct voltage can still receive an unsafe signal level.

**Step 2.** Install the upstream MFRC522 library and open the Serial Monitor at the sketch baud rate.

**Step 3.** Run Checker, then Reader, using a supported disposable tag. Investigate wiring and compatibility before assuming a tag is damaged.

**Step 4.** Use Writer only on a tag you own and can erase. Keep writes disabled until the code and block layout have been reviewed.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| No write is possible with the shipped compile-time flag. | Meets the stated criterion | Not run | Pending |
| Unsupported card types and failed authentication cause no fallback key attempts. | Meets the stated criterion | Not run | Pending |
| A successful write requires a matching read-back result. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
