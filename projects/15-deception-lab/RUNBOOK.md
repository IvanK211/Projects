# Operating worksheet: Defensive deception and canary lab

**Scope:** Local demonstration + design playbook. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Start the local listener and request its endpoint from the same machine to create a synthetic event.

**Step 2.** Define detection ownership, permitted test sources and cleanup rules before any networked deception exercise.

**Step 3.** Use clearly nonfunctional lab credentials and never make a decoy a route into a real environment.

**Step 4.** Evaluate alert routing, false positives and containment independently from how convincing the decoy looks.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| One authorized interaction produces one minimal event. | Meets the stated criterion | Not run | Pending |
| No command execution or credential submission path exists. | Meets the stated criterion | Not run | Pending |
| Networked deployment remains an explicit future design review. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
