# Security KPI and board-report pipeline

**Category:** Security reporting  
**Archive status:** Offline implementation + presentation design

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Create reproducible metric summaries and an unbranded, offline report without publishing corporate workbooks, presentation themes or real performance figures.

## Design and behavior

Each metric declares whether observations are summed, averaged or represented by the last sample. Missing observations remain null. A second command creates a self-contained HTML report with escaped input and no external scripts, fonts or tracking. A slide/deck outline is included as a design guide; no original slide master or complete legacy deck generator is claimed to be recovered.

## Included implementation

- [labkit/reporting.py](../../labkit/reporting.py)
- [examples/kpis.json](../../examples/kpis.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit kpis examples/kpis.json local-output/kpi-summary.json
```

## Workflow

1. Document each KPI definition, period, population, aggregation rule and data owner before ingestion.

2. Run the summary, then python -m labkit html local-output/kpi-summary.json local-output/kpi-report.html --title "Synthetic KPI review".

3. Inspect the missing-data case and the aggregation rule before adding narrative.

4. Use the unbranded board outline to describe changes, uncertainty, risks and required decisions. Do not automate a success narrative from missing data.

## Acceptance criteria

- A missing metric is distinct from a numeric zero.
- Untrusted strings are escaped in generated HTML.
- Report content has no remote dependencies or corporate branding.

## Troubleshooting and limits

Mean exposure scores, total incidents and point-in-time coverage need different aggregation rules.

Thresholds are governance decisions and are not copied from any real program.

HTML generation is not a reviewed PowerPoint or spreadsheet export.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S08](../../docs/SOURCES.md#s08). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
