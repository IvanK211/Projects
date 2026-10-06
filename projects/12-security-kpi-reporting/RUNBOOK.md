# Operating worksheet: Security KPI and board-report pipeline

**Scope:** Offline implementation + presentation design. This is an unfilled public template.

## Before starting

Record the authorization, purpose, bounded inputs, required privileges and a clear stop condition in a private working note. Identify which included files are executable and which are only design material. Preserve a protected pre-change state whenever a live change is contemplated.

## Execution sequence

**Step 1.** Document each KPI definition, period, population, aggregation rule and data owner before ingestion.

**Step 2.** Run the summary, then python -m labkit html local-output/kpi-summary.json local-output/kpi-report.html --title "Synthetic KPI review".

**Step 3.** Inspect the missing-data case and the aggregation rule before adding narrative.

**Step 4.** Use the unbranded board outline to describe changes, uncertainty, risks and required decisions. Do not automate a success narrative from missing data.

## Evidence to retain privately

| Check | Expected outcome | Observation | Decision |
|---|---|---|---|
| A missing metric is distinct from a numeric zero. | Meets the stated criterion | Not run | Pending |
| Untrusted strings are escaped in generated HTML. | Meets the stated criterion | Not run | Pending |
| Report content has no remote dependencies or corporate branding. | Meets the stated criterion | Not run | Pending |

## Stop and recovery

Stop on scope ambiguity, invalid input, unexpected permissions, failed preconditions, missing safety controls or an unexplained result. Do not work around a failure by disabling certificate checks, enlarging access or forcing a write. For analytical tools, discard only the derived output and correct the input mapping. For a live change, inspect the private pre-change evidence and use a separately reviewed recovery plan; a failed batch does not imply earlier operations were reversed.

## Completion note

Record what was tested, what remained unknown and which version of the reference was used. Return temporary grants/settings to their approved state. Do not paste the private completion note, request IDs, paths or screenshots into a public issue.
