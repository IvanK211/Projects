# Operating worksheet: Nonblocking two-team event timer

**Scope:** Arduino reference sketch; hardware build unverified. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Compile for a reviewed Arduino-compatible board and verify the arbitrary reference pin assignments.

**Step 2.** Test the state transitions with no external actuators connected.

**Step 3.** Compare measured elapsed time with an independent clock during rapid team changes and long pauses.

**Step 4.** Add a display through a separate adapter and document restart/persistence behavior before using the timer in an event.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| The timer starts paused and a pause press stops accumulation. | Meets the stated criterion | Not run | Pending |
| Holding a button does not generate repeated state-change events. | Meets the stated criterion | Not run | Pending |
| Timing continues without blocking while input debouncing runs. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
