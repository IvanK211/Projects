# Operating worksheet: Encrypted snapshot and restore verification

**Scope:** Bash syntax-checked reference; encryption round-trip pending. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Export databases using their supported backup method and quiesce changing application data before invoking this directory snapshot reference.

**Step 2.** Choose a destination outside the source and validate its available space, access control and actual mount state.

**Step 3.** Keep decryption identities separate from the repository and backup medium; document private recovery access.

**Step 4.** Verify the archive, restore only in an isolated scratch environment with a reviewed safe extraction process, and test the application before treating the backup as successful.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| An encryption or tar failure returns a failed command. | Meets the stated criterion | Not run | Pending |
| A destination inside the source is rejected. | Meets the stated criterion | Not run | Pending |
| A successful archive listing is not reported as a completed application recovery. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
