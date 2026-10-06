# Operating worksheet: Low-voltage runtime and energy-budget calculator

**Scope:** Offline implementation. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Measure the load over representative idle, active and startup conditions rather than relying on one nominal current.

**Step 2.** Use consistent voltage and capacity definitions and make conversion losses explicit.

**Step 3.** Run the reference example and compare estimates across reasonable operating assumptions.

**Step 4.** Use only appropriately designed power systems; cell matching, charging, protection, conductor size and enclosure temperature require separate review.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Zero load power and non-finite inputs fail validation. | Meets the stated criterion | Not run | Pending |
| Fractions are restricted to physically meaningful ranges. | Meets the stated criterion | Not run | Pending |
| Estimated hours are not presented as a guaranteed runtime. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
