# Security-awareness training audit

**Category:** Security reporting  
**Archive status:** Offline implementation

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Calculate expected training obligations by group and distinguish completed, assigned-but-incomplete and never-assigned requirements.

## Design and behavior

The tool joins an explicit active population with required module identifiers. Multiple supplied enrollments can satisfy one requirement, but do not inflate the obligation count. A completion in the bounded input satisfies the requirement. Time-window and recurrence policy are therefore deliberate preprocessing choices, not hidden assumptions inside a campaign-name substring match.

## Included implementation

- [labkit/awareness.py](../../labkit/awareness.py)
- [examples/training.json](../../examples/training.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit training examples/training.json local-output/training-audit.json
```

## Workflow

1. Define the reporting population, the required modules and the reporting period before exporting data.

2. Normalize provider module IDs and statuses into the synthetic schema; maintain a reviewed alias table outside this public repository when names differ.

3. Inspect detailed obligation rows before using grouped totals. Unassigned divisions remain an explicit category.

4. For recurrent training, split requirements by module plus period so an old completion cannot accidentally satisfy a new obligation.

## Acceptance criteria

- Missed equals incomplete plus not assigned.
- A zero-obligation group has an unknown completion rate, not a fabricated perfect score.
- Inactive users are excluded only by the explicit active flag.

## Troubleshooting and limits

Current group membership may differ from membership when training was assigned.

Friendly course labels are not stable provider identifiers.

A missing assignment and a missed assigned course require different corrective action.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S07](../../docs/SOURCES.md#s07). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
