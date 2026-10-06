# Operating worksheet: Directory-role PIM request audit

**Scope:** Offline implementation + unverified live collector. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Run the synthetic filter and confirm that adminAssign is excluded while a denied selfActivate remains visible.

**Step 2.** Approve the documented endpoint permission and a supported directory role before any live use. The ReadWrite-named permission does not mean this script writes, but it is still a powerful grant.

**Step 3.** Use -ResolveNames only when the additional directory read access is justified. Review unresolved lookups rather than deleting their rows.

**Step 4.** Define the report as a request audit, document source retention, and separately derive success-only metrics from an agreed status mapping.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Dates include offsets and are compared in UTC. | Meets the stated criterion | Not run | Pending |
| Unknown principals keep their IDs and do not silently disappear. | Meets the stated criterion | Not run | Pending |
| Azure resource roles and PIM for Groups are explicitly outside the collector scope. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
