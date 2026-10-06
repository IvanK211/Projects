# Sensor calibration and drift logging

**Category:** Home automation and embedded systems  
**Archive status:** Offline implementation + measurement schema

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Keep sensor identity, units, time and sampling context explicit so apparent drift is not confused with a calibration problem.

## Design and behavior

The tool groups observations by sensor and unit, calculates extrema and median, and reports endpoint drift per hour only when a nonzero elapsed interval exists. It does not diagnose a physical cause from that arithmetic. The schema distinguishes reference samples, system samples and calibration buffers so they cannot silently be combined.

## Included implementation

- [labkit/telemetry.py](../../labkit/telemetry.py)
- [examples/sensors.json](../../examples/sensors.json)
- [projects/28-sensor-calibration/measurement-template.json](../../projects/28-sensor-calibration/measurement-template.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit sensors examples/sensors.json local-output/sensor-summary.json
```

## Workflow

1. Use the manufacturer calibration procedure and independently record reference condition, temperature and time.

2. Keep repeated readings from the same sample distinct from measurements of different samples.

3. Run the synthetic series and inspect units and timestamp offsets before introducing privately collected observations.

4. Change one experimental factor at a time and retain uncertainty, instrument resolution and stabilization criteria in the private log.

## Acceptance criteria

- Different units never share one statistical group.
- Non-finite readings and missing timestamps are rejected.
- Zero elapsed time gives unknown drift rather than a divide-by-zero or invented trend.

## Troubleshooting and limits

A reading in air may not be a meaningful measurement for a liquid-contact electrode.

Buffer contamination, temperature and sample mixing can imitate sensor failure.

A slope alone cannot identify a chemical or electrical mechanism.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S18](../../docs/SOURCES.md#s18). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
