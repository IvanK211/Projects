# Operating worksheet: Directory group-membership audit

**Scope:** Unverified live collector + analysis guide. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Prepare the user-ID input in a protected private workspace; do not reuse any public example alias as a cloud identity.

**Step 2.** Select direct membership for immediate assignments or transitive membership for inheritance, and record the choice with the review.

**Step 3.** Approve Directory.Read.All only in a suitable test context; narrow the workflow further before a broad rollout.

**Step 4.** Review disabled accounts, unexpected privileged memberships and ownerless groups using a separate decision record. This script never removes memberships.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| The input is a bounded list rather than a tenant-wide implicit sweep. | Meets the stated criterion | Not run | Pending |
| Direct and transitive output contain an explicit relation label. | Meets the stated criterion | Not run | Pending |
| A prefix filter does not change the underlying authorization model. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
