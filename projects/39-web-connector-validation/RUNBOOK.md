# Operating worksheet: Browser connector and authentication validation

**Scope:** Design and troubleshooting matrix. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Document supported authentication modes and whether the requested integration is session access, password verification, change or reconciliation.

**Step 2.** Validate the application manually from the authorized connector context using a disposable account.

**Step 3.** Test timing, pop-ups, redirects, page changes, expired credentials and explicit logout independently.

**Step 4.** Capture only redacted synthetic UI states for public documentation; retain real traces and selectors privately.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| A session-only integration is not claimed to rotate passwords. | Meets the stated criterion | Not run | Pending |
| The connector fails clearly when UI or authentication behavior changes. | Meets the stated criterion | Not run | Pending |
| Credentials do not appear in command lines, screenshots, logs or published selectors. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
