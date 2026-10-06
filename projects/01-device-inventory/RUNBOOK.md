# Operating worksheet: Managed-device inventory and snapshot reconciliation

**Scope:** Offline implementation + unverified live collector. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Run the supplied synthetic example first and inspect all three outcomes: Found, Duplicate and NotFound.

**Step 2.** For an authorized lab, install the Graph authentication module explicitly, protect the output directory with operating-system permissions, and supply the tenant ID only at runtime.

**Step 3.** Wrap the collected array with a requested list matching the example schema; preserve original IDs and UTC offsets.

**Step 4.** Compare snapshots with python -m labkit compare examples/inventory-before.json examples/inventory-after.json local-output/diff.json. Investigate added, removed and changed records separately.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| A short hostname does not match an unrelated hostname containing it. | Meets the stated criterion | Not run | Pending |
| A duplicate record is visible, even when a single newest record is selected. | Meets the stated criterion | Not run | Pending |
| A renamed stable ID appears as changed, and absent data does not establish an employee departure. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
