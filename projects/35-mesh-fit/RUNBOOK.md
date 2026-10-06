# Operating worksheet: Uniform bounding-box fit calculator

**Scope:** Offline implementation. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Measure or extract source and target bounding boxes in the same units.

**Step 2.** Choose orientation before calculating; swapping axes changes the fit.

**Step 3.** Run the reference command and inspect the limiting dimension.

**Step 4.** For real mating geometry, use a parametric redesign when holes, wall thickness or external hardware must keep their size.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Zero/negative source dimensions are rejected. | Meets the stated criterion | Not run | Pending |
| Clearance that consumes the target is rejected. | Meets the stated criterion | Not run | Pending |
| Every scaled dimension fits within the reduced target bounds. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
