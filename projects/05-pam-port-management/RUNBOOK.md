# Operating worksheet: PAM account-property change planning

**Scope:** Offline planner + unverified, guarded live executor. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Run the synthetic planner and confirm that notexample.invalid and unrelated suffixes are not selected.

**Step 2.** Review the entire plan, including Safe, platform, address, original properties and proposed value. Keep real plans private.

**Step 3.** Test one disposable account with the exact platform definition, TLS trust chain and approved PAM authentication method.

**Step 4.** Apply only after review using -Apply and normal confirmation. The default batch limit is deliberately small. Read the rollback runbook before starting.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| One patch remains a JSON array rather than collapsing into an object. | Meets the stated criterion | Not run | Pending |
| Other properties survive the operation and duplicate port casing is rejected. | Meets the stated criterion | Not run | Pending |
| A failed update stops the batch; earlier successful operations are not described as rolled back. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
