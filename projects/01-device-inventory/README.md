# Managed-device inventory and snapshot reconciliation

**Category:** Identity and endpoint security  
**Archive status:** Offline implementation + unverified live collector

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Resolve a requested device list against an inventory without losing missing devices or hiding duplicate enrollment records. Compare two snapshots without treating a renamed device as automatically new.

## Design and behavior

Collection and analysis are separate. The optional PowerShell collector retrieves managed-device objects; the offline Python layer normalizes exact names, validates IDs and timestamps, and returns newest and oldest matching records. Null timestamps are retained and ranked below observed timestamps. Stable IDs are the preferred snapshot key. The assigned-user field is deliberately not renamed to legal owner.

## Included implementation

- [labkit/inventory.py](../../labkit/inventory.py)
- [projects/01-device-inventory/Export-ManagedDevices.ps1](../../projects/01-device-inventory/Export-ManagedDevices.ps1)
- [examples/inventory.json](../../examples/inventory.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit inventory examples/inventory.json local-output/inventory-report.json
```

## Workflow

1. Run the supplied synthetic example first and inspect all three outcomes: Found, Duplicate and NotFound.

2. For an authorized lab, install the Graph authentication module explicitly, protect the output directory with operating-system permissions, and supply the tenant ID only at runtime.

3. Wrap the collected array with a requested list matching the example schema; preserve original IDs and UTC offsets.

4. Compare snapshots with python -m labkit compare examples/inventory-before.json examples/inventory-after.json local-output/diff.json. Investigate added, removed and changed records separately.

## Acceptance criteria

- A short hostname does not match an unrelated hostname containing it.
- A duplicate record is visible, even when a single newest record is selected.
- A renamed stable ID appears as changed, and absent data does not establish an employee departure.

## Troubleshooting and limits

Primary/assigned user, registered owner, enrollment owner and business custodian are different concepts.

An empty inventory is not evidence that requested devices do not exist elsewhere.

CSV or spreadsheet exports need explicit column mapping; the JSON schema is intentional.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S01](../../docs/SOURCES.md#s01). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
