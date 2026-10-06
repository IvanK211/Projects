# Operating worksheet: Low-energy output-control pattern

**Scope:** Arduino indicator sketch; hardware unverified. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Select a correctly rated indicator LED, resistor and board output according to component specifications.

**Step 2.** Check that startup and button release leave the output off.

**Step 3.** Measure the output behavior using the indicator before extending the state machine.

**Step 4.** For any other load, create a separate power-stage review with appropriate isolation, current limits, protection and fault analysis; do not attach it directly to the reference pin.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Startup output is zero. | Meets the stated criterion | Not run | Pending |
| The loop remains responsive during brightness changes. | Meets the stated criterion | Not run | Pending |
| The source does not contain a hazardous actuator integration. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
