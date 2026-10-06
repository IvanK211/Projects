# Operating worksheet: Fail-safe low-voltage water-controller bench

**Scope:** ESPHome firmware template; hardware unverified. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Review the chosen board pinout and input/output electrical levels before connecting anything.

**Step 2.** Use a low-energy indicator first; create real API, OTA and Wi-Fi secrets only in a private secrets file.

**Step 3.** Confirm that unknown input, open wire, low level, network loss and reboot do not request an energized output.

**Step 4.** Add pump-specific protection, independent hardware interlocking and a validated schedule only through a separate engineering review. No production irrigation schedule is supplied.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| The output starts off after firmware boot. | Meets the stated criterion | Not run | Pending |
| A valid bench request terminates even without network connectivity. | Meets the stated criterion | Not run | Pending |
| Removing the healthy input stops the pulse. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
