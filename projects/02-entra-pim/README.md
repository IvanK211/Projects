# Directory-role PIM request audit

**Category:** Identity and endpoint security  
**Archive status:** Offline implementation + unverified live collector

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Produce a defensible activation-request report that retains justification, status, principal, scope and schedule information without confusing a request with a completed privileged session.

## Design and behavior

The collector paginates directory-role schedule requests and applies action/time filters locally. Failed, denied and pending requests are retained rather than silently counted as successful activations. Optional name resolution is a separate privilege choice. The reference preserves the original schedule object because expiration may be expressed as an end time, duration, or no-expiration mode.

## Included implementation

- [labkit/awareness.py](../../labkit/awareness.py)
- [projects/02-entra-pim/Export-PimRequests.ps1](../../projects/02-entra-pim/Export-PimRequests.ps1)
- [examples/pim.json](../../examples/pim.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit pim examples/pim.json local-output/pim.json --since 2001-01-01T00:00:00Z
```

## Workflow

1. Run the synthetic filter and confirm that adminAssign is excluded while a denied selfActivate remains visible.

2. Approve the documented endpoint permission and a supported directory role before any live use. The ReadWrite-named permission does not mean this script writes, but it is still a powerful grant.

3. Use -ResolveNames only when the additional directory read access is justified. Review unresolved lookups rather than deleting their rows.

4. Define the report as a request audit, document source retention, and separately derive success-only metrics from an agreed status mapping.

## Acceptance criteria

- Dates include offsets and are compared in UTC.
- Unknown principals keep their IDs and do not silently disappear.
- Azure resource roles and PIM for Groups are explicitly outside the collector scope.

## Troubleshooting and limits

A query cannot recover records already removed by retention.

A requested schedule is not a session recording or evidence that the user executed an action.

Consent scope and the signed-in user role are separate authorization requirements.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S02](../../docs/SOURCES.md#s02). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
