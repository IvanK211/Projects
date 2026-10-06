# Operating worksheet: Historical IP-to-asset correlation

**Scope:** Offline implementation. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Normalize authorized source timestamps into explicit offsets and retain source identifiers privately.

**Step 2.** Choose an as-of time that matches the incident or question instead of automatically using the present.

**Step 3.** Run the correlation and review every matching identity in the relevant window.

**Step 4.** Investigate NAT, DHCP lease changes, clock skew and adapter duplication before assigning responsibility to a device or person.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| An address shared at different times keeps both observations. | Meets the stated criterion | Not run | Pending |
| Stale and future-dated records are separately marked. | Meets the stated criterion | Not run | Pending |
| No active network access occurs during analysis. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
