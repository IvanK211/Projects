# Operating worksheet: MQTT authorization and Zigbee integration lab

**Scope:** Configuration example + design guide. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Create broker accounts privately and verify that their names match the reviewed ACL entries.

**Step 2.** Test permitted reads/writes and rejected cross-topic operations before adding automation.

**Step 3.** Pair a disposable device during a bounded commissioning window and then disable joining.

**Step 4.** Document retained-state cleanup, controller replacement, network-key backup and recovery in a protected operations record.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Anonymous clients cannot publish to the reference broker. | Meets the stated criterion | Not run | Pending |
| The observer cannot send control messages. | Meets the stated criterion | Not run | Pending |
| A stale retained message cannot silently be treated as a fresh safety decision. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
