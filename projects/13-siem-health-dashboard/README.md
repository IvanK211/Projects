# SIEM health snapshot dashboard

**Category:** Security reporting  
**Archive status:** Node snapshot viewer + live integration design

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Expose a demonstrable local dashboard that separates process liveness from upstream health and keeps unavailable telemetry visible.

## Design and behavior

The dependency-free Node server reads a local JSON snapshot. It binds to loopback, serves a browser display, provides /healthz for process liveness and /readyz for a healthy recent snapshot, and labels stale data as unknown. The historical fixture is deliberately not healthy-now. The repository also includes a counter-rate function that rejects resets, time reversals and source changes. No live Wazuh connector is claimed.

## Included implementation

- [projects/13-siem-health-dashboard/server.mjs](../../projects/13-siem-health-dashboard/server.mjs)
- [labkit/telemetry.py](../../labkit/telemetry.py)
- [examples/siem-health.json](../../examples/siem-health.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
node projects/13-siem-health-dashboard/server.mjs
```

## Workflow

1. Start the viewer from the repository root and open the loopback address documented in the project runbook.

2. Check that liveness succeeds but readiness fails for the deliberately historical fixture.

3. Normalize an authorized manager/indexer snapshot in a private workspace; never pass credentials or raw provider error bodies to the browser.

4. Design independent subsystem timeouts and a bounded sample history before adding live API clients. Separate cumulative counters from per-second rates.

## Acceptance criteria

- A running server does not falsely imply a healthy SIEM.
- A missing subsystem is unknown rather than silently green.
- The browser renders snapshot content as text, not executable HTML.

## Troubleshooting and limits

Index rollover and daemon restart invalidate a simple counter subtraction.

An overall HTTP 200 health response is not enough for a readiness probe.

This local reference is not an authenticated production dashboard.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S09](../../docs/SOURCES.md#s09). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
