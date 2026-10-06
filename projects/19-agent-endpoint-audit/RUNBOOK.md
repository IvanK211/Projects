# Operating worksheet: Region-aware agent and API endpoint review

**Scope:** Offline transformation tool + connectivity runbook. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Verify the provider-specific portal, API, authentication and agent endpoints in current documentation.

**Step 2.** Build a local mapping of only the exact approved hostnames; do not use a universal domain string replacement.

**Step 3.** Run the review, then create a new protected copy with --write-copy and inspect the complete file privately.

**Step 4.** Use a vendor-supported migration or repair procedure for installed agents; this tool never modifies an agent in place or migrates an organization between regions.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Unrelated URLs are unchanged. | Meets the stated criterion | Not run | Pending |
| The original file is never overwritten. | Meets the stated criterion | Not run | Pending |
| Only hostnames are counted in diagnostics; URL queries and credentials are not printed. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
