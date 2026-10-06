# Operating worksheet: Security-control evidence and operational assurance

**Scope:** Reusable templates; not a compliance opinion. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Describe the control objective in plain language before choosing an artifact.

**Step 2.** Store real evidence in an approved private location and link only an internal reference within the private worksheet.

**Step 3.** Record the reviewer, collection period and limitations; distinguish a designed control from an operating control.

**Step 4.** Use the monitoring-capability template to explain prevention, detection, escalation, response and evidence retention without disclosing topology.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Each statement has an evidence owner and validation method. | Meets the stated criterion | Not run | Pending |
| No real audit status or certification claim is inferred from this repository. | Meets the stated criterion | Not run | Pending |
| Evidence retention and access are explicit decisions. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
