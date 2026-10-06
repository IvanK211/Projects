# Operating worksheet: Conditional-access and MFA rollout kit

**Scope:** Design and communication templates. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Map application access paths and dependency accounts in a private worksheet.

**Step 2.** Test the proposed requirement in report-only mode where supported; compare results with expected user journeys.

**Step 3.** Verify emergency access and administrative recovery before expanding a pilot.

**Step 4.** Publish a generic notice with the change window, expected behavior, prerequisite steps and support method filled only in a private copy.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Pilot success includes recovery and exception paths, not just a happy-path login. | Meets the stated criterion | Not run | Pending |
| Policy scope is documented before enforcement. | Meets the stated criterion | Not run | Pending |
| User communications do not leak internal URLs or device inventories. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
