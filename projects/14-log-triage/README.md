# Structured log triage and summary

**Category:** Security reporting  
**Archive status:** Offline implementation

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Summarize normalized operational events without copying raw messages, addresses or account names into the report.

## Design and behavior

The implementation counts event types and severity labels from a JSON event list. Raw message fields are intentionally dropped. It is an observation aid, not a forensic collection tool or a generic parser for every daemon format. A private normalization stage should preserve source timestamps and parsing failures before data reaches this public-safe aggregation pattern.

## Included implementation

- [labkit/telemetry.py](../../labkit/telemetry.py)
- [examples/logs.json](../../examples/logs.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit logs examples/logs.json local-output/log-summary.json
```

## Workflow

1. Build a source-specific parser privately or manually normalize a small authorized sample.

2. Keep a protected original if incident-handling requirements call for one; never use the public repository as an evidence vault.

3. Inspect unrecognized severity and event labels, then run the aggregate summary.

4. Compare time-normalized rates and recurrence after a corrective change, rather than comparing totals from unequal time windows.

## Acceptance criteria

- Raw messages do not appear in the aggregate output.
- Unknown labels remain visible.
- No summary claims a root cause from frequency alone.

## Troubleshooting and limits

Custom event labels can themselves contain private details and require review.

Dropped or malformed log lines can bias conclusions.

Clock offsets and duplicate ingestion affect apparent event ordering.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
