# Operating worksheet: Phishing-simulation campaign analytics

**Scope:** Offline implementation. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Decide what constitutes failure and normalize provider events into one recipient outcome per campaign.

**Step 2.** Deduplicate campaign/group records before analysis; define handling for delivery failure, automated link scanning and incomplete populations.

**Step 3.** Run the fixture and compare the weighted result with the campaign mean to see why the headline definition matters.

**Step 4.** Keep untested or zero-delivery periods distinct from zero-failure campaigns. Use a documented reporting window for comparisons.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Counts cannot be negative, fractional or greater than delivered recipients. | Meets the stated criterion | Not run | Pending |
| Zero delivery produces an unknown rate. | Meets the stated criterion | Not run | Pending |
| The synthetic example yields different weighted and campaign-average rates. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
