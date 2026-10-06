# Operating worksheet: Safe local development and demonstration workflow

**Scope:** Operational checklist. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Confirm that the environment is an owned or explicitly authorized lab before changing a setting.

**Step 2.** Check the selected serial port, baud rate and application output channel before changing firmware.

**Step 3.** Bind demonstration web services to loopback and use synthetic data.

**Step 4.** For presentation-related lock/sleep changes, use approved temporary settings and restore them afterward; do not override a managed security policy.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| A troubleshooting procedure starts with observation rather than disabling protections. | Meets the stated criterion | Not run | Pending |
| Demo servers are not accidentally reachable from other machines. | Meets the stated criterion | Not run | Pending |
| Temporary convenience changes have an explicit restoration step. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
