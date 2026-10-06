# Operating worksheet: Parametric enclosure and fit-coupon sources

**Scope:** OpenSCAD source + rendered reference meshes. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Open the source in OpenSCAD and review the dimensional parameters before rendering.

**Step 2.** Render the base with openscad -o base.stl enclosure.scad; render the lid with -D part="lid" using shell-appropriate quoting.

**Step 3.** Print the fit coupon before committing to a complete enclosure and record material, orientation and machine conditions privately.

**Step 4.** Adjust design clearances rather than blindly scaling the whole assembly when mating features need dimensional accuracy.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| The mesh renderer reports a valid closed solid for each enclosure part. | Meets the stated criterion | Not run | Pending |
| The lid and base are separate printable parts. | Meets the stated criterion | Not run | Pending |
| No real board mounting pattern or physical-security mechanism is encoded. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
