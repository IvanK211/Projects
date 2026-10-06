# Operating worksheet: Bounded Linux service watchdog

**Scope:** Bash syntax-checked reference; service recovery unverified. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Run bash watchdog.sh SERVICE in a lab and inspect the status without allowing changes.

**Step 2.** Investigate configuration, connectivity and vendor health checks before treating a restart as a fix.

**Step 3.** Create and protect a dedicated state directory only after review; use --apply solely for a disposable or approved service.

**Step 4.** Test the cooldown, concurrent invocation, invalid state and failed-restart paths before scheduling a timer.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| No restart occurs without --apply. | Meets the stated criterion | Not run | Pending |
| Concurrent runs do not perform duplicate recovery actions. | Meets the stated criterion | Not run | Pending |
| Persistent failure produces a failure exit rather than a false-success message. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
