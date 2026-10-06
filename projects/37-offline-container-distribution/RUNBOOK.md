# Operating worksheet: Offline container-image distribution

**Scope:** Bash syntax-checked reference + transfer playbook. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Build only reviewed source with an approved base image and inspect the complete build context.

**Step 2.** Check layers and metadata for copied secrets, credentials, private certificates and repository history.

**Step 3.** Run the export and move only approved artifacts through the authorized transfer channel.

**Step 4.** Verify the checksum, load in a lab, check runtime configuration and health, then record the tested image identity privately.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| The output archive is not silently overwritten. | Meets the stated criterion | Not run | Pending |
| No environment file is bundled by the export helper. | Meets the stated criterion | Not run | Pending |
| The recipient verifies provenance as well as integrity. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
