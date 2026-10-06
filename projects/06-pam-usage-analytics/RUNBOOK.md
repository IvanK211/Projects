# Operating worksheet: PAM session-usage analytics

**Scope:** Offline implementation + collection specification. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Normalize an authorized recordings metadata export into the example schema; do not include recordings, transcripts, passwords or command content.

**Step 2.** Choose a reporting window and establish whether timestamps represent UTC seconds, milliseconds or ISO strings before conversion.

**Step 3.** Run the grouping and inspect missing initiating users, duplicate IDs and incomplete sessions.

**Step 4.** Present session counts as activity evidence, not automatically as productivity, security quality, or total PAM adoption.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| The target account cannot accidentally become the human-usage grouping key. | Meets the stated criterion | Not run | Pending |
| Open recordings do not contribute a fabricated duration. | Meets the stated criterion | Not run | Pending |
| Retention limitations remain visible in the report narrative. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
