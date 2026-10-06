# Operating worksheet: Endpoint identity and network hunting queries

**Scope:** KQL templates; not executed against a tenant. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Open a query in an authorized hunting workspace and check the current table schema before adapting it.

**Step 2.** Replace only the documented synthetic filter in a private copy, then choose a retention-compatible time window.

**Step 3.** Compare endpoint observations with other authorized network records before making attribution decisions.

**Step 4.** Document a missing-result investigation: onboarding, telemetry arrival, time window, product availability, and permissions.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| An IP lookup returns potentially multiple devices and time ranges. | Meets the stated criterion | Not run | Pending |
| Hostname selection uses equality rather than a broad contains match. | Meets the stated criterion | Not run | Pending |
| No query isolates a device, changes policy, or executes a response action. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
