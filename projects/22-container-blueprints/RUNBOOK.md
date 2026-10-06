# Operating worksheet: Independent container-service blueprints

**Scope:** Deployment templates; not Docker-runtime validated. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Select one blueprint rather than assuming all three are meant to run together.

**Step 2.** Choose a reviewed image version or digest and supply variables through a private environment file.

**Step 3.** Use docker compose config --quiet for validation; do not publish expanded configuration that contains local settings.

**Step 4.** Validate permissions, persistence, updates, restore behavior and any separately approved device/network access before use.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| Missing required variables stop interpolation rather than inventing defaults. | Meets the stated criterion | Not run | Pending |
| No public interface is exposed by a copied template. | Meets the stated criterion | Not run | Pending |
| An image update has a recorded rollback and data-compatibility check. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
