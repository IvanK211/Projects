# Operating worksheet: Presence, night-mode and lighting automations

**Scope:** Home Assistant YAML template; runtime unverified. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Copy the package into a disposable Home Assistant test configuration and replace fictional entities privately.

**Step 2.** Use an indicator lamp before controlling any meaningful load.

**Step 3.** Test sensor on/off, unavailable state, repeated motion, manual light changes and a controller restart.

**Step 4.** Decide explicitly whether manual overrides persist, and how delayed-off behavior should recover after a restart.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Night mode changes the selected brightness in the reference logic. | Meets the stated criterion | Not run | Pending |
| A stale or unavailable sensor is not assumed to mean a safe empty room. | Meets the stated criterion | Not run | Pending |
| Manual override and restart semantics are documented rather than implicit. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
