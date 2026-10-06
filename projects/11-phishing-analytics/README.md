# Phishing-simulation campaign analytics

**Category:** Security reporting  
**Archive status:** Offline implementation

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Report simulation results with clearly named denominators instead of treating averages of different kinds as interchangeable.

## Design and behavior

The tool exposes both the exposure-weighted failure rate and the mean of nonempty campaign rates. Each campaign/group row is unique. Failed and reported counts represent unique recipients within that row, not raw click event counts. Repeated people across campaigns remain repeated exposures; this is explicitly not a distinct-person annual rate.

## Included implementation

- [labkit/awareness.py](../../labkit/awareness.py)
- [examples/phishing.json](../../examples/phishing.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit phishing examples/phishing.json local-output/phishing-summary.json
```

## Workflow

1. Decide what constitutes failure and normalize provider events into one recipient outcome per campaign.

2. Deduplicate campaign/group records before analysis; define handling for delivery failure, automated link scanning and incomplete populations.

3. Run the fixture and compare the weighted result with the campaign mean to see why the headline definition matters.

4. Keep untested or zero-delivery periods distinct from zero-failure campaigns. Use a documented reporting window for comparisons.

## Acceptance criteria

- Counts cannot be negative, fractional or greater than delivered recipients.
- Zero delivery produces an unknown rate.
- The synthetic example yields different weighted and campaign-average rates.

## Troubleshooting and limits

Averaging percentages without denominators can misstate overall exposure.

Campaign difficulty and recipient mix can confound a trend.

Reporting behavior is not the inverse of failure behavior; one person can do both.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S07](../../docs/SOURCES.md#s07). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
