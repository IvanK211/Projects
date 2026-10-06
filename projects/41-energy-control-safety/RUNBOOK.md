# Operating worksheet: Household energy-control safety architecture

**Scope:** Concept only; no mains wiring or construction files. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Document the intended supervisory behavior using a low-voltage indicator rather than the real load.

**Step 2.** Have a qualified professional assess the actual load, protection, switching device, enclosure and installation constraints.

**Step 3.** Define independent timeout, feedback, manual override and fault states without treating the automation platform as a safety controller.

**Step 4.** Retain installation approval and inspection evidence privately; never infer that a generic reference authorizes a real installation.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Loss of control connectivity has a documented safe outcome. | Meets the stated criterion | Not run | Pending |
| Protective functions remain independent of remote software. | Meets the stated criterion | Not run | Pending |
| No actual electrical design or deployment information is published. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
