# Operating worksheet: SIEM health snapshot dashboard

**Scope:** Node snapshot viewer + live integration design. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Start the viewer from the repository root and open the loopback address documented in the project runbook.

**Step 2.** Check that liveness succeeds but readiness fails for the deliberately historical fixture.

**Step 3.** Normalize an authorized manager/indexer snapshot in a private workspace; never pass credentials or raw provider error bodies to the browser.

**Step 4.** Design independent subsystem timeouts and a bounded sample history before adding live API clients. Separate cumulative counters from per-second rates.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| A running server does not falsely imply a healthy SIEM. | Meets the stated criterion | Not run | Pending |
| A missing subsystem is unknown rather than silently green. | Meets the stated criterion | Not run | Pending |
| The browser renders snapshot content as text, not executable HTML. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
