# Historical IP-to-asset correlation

**Category:** Detection engineering  
**Archive status:** Offline implementation

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Correlate one IP address with timestamped observations while preserving ambiguity, source and staleness.

## Design and behavior

The reference validates address syntax, selects exact matches and records age, future-dated status and staleness for every observation. It intentionally does not choose a single winner or perform live DNS/network queries. This makes it suitable as a review stage for independently collected endpoint, DHCP, firewall or inventory data.

## Included implementation

- [labkit/telemetry.py](../../labkit/telemetry.py)
- [examples/ip-observations.json](../../examples/ip-observations.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit correlate examples/ip-observations.json local-output/ip-correlation.json --ip 192.0.2.10 --as-of 2001-01-02T12:00:00Z --max-age-hours 12
```

## Workflow

1. Normalize authorized source timestamps into explicit offsets and retain source identifiers privately.

2. Choose an as-of time that matches the incident or question instead of automatically using the present.

3. Run the correlation and review every matching identity in the relevant window.

4. Investigate NAT, DHCP lease changes, clock skew and adapter duplication before assigning responsibility to a device or person.

## Acceptance criteria

- An address shared at different times keeps both observations.
- Stale and future-dated records are separately marked.
- No active network access occurs during analysis.

## Troubleshooting and limits

Reverse DNS is supporting context, not authoritative ownership.

Multiple telemetry sources can describe the same underlying event.

A freshness threshold is an analysis choice and must be documented.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S04](../../docs/SOURCES.md#s04). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
