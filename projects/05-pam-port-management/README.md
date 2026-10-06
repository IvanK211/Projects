# PAM account-property change planning

**Category:** Privileged access management  
**Archive status:** Offline planner + unverified, guarded live executor

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Plan narrowly scoped port-property updates with a reviewable pre-change state and a separate, explicitly approved apply step.

## Design and behavior

The Python planner uses DNS-label boundaries and optional Safe scoping. It preserves other platform properties and emits a JSON Patch array. The PowerShell executor ignores supplied executable patch instructions, reconstructs the intended operation, re-fetches each account, rejects state drift, and verifies the new value. No live call occurs in review-only mode. There is no automatic schema-guessing retry sequence.

## Included implementation

- [labkit/pam.py](../../labkit/pam.py)
- [projects/05-pam-port-management/Apply-PamPortPlan.ps1](../../projects/05-pam-port-management/Apply-PamPortPlan.ps1)
- [examples/pam-accounts.json](../../examples/pam-accounts.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit pam-plan examples/pam-accounts.json local-output/pam-plan.json --suffix example.invalid --port 9443
```

## Workflow

1. Run the synthetic planner and confirm that notexample.invalid and unrelated suffixes are not selected.

2. Review the entire plan, including Safe, platform, address, original properties and proposed value. Keep real plans private.

3. Test one disposable account with the exact platform definition, TLS trust chain and approved PAM authentication method.

4. Apply only after review using -Apply and normal confirmation. The default batch limit is deliberately small. Read the rollback runbook before starting.

## Acceptance criteria

- One patch remains a JSON array rather than collapsing into an object.
- Other properties survive the operation and duplicate port casing is rejected.
- A failed update stops the batch; earlier successful operations are not described as rolled back.

## Troubleshooting and limits

Property name casing is platform-sensitive and must be reviewed.

Precondition checks reduce risk but cannot provide atomic cross-account transactions.

An HTTP success alone is weaker evidence than a subsequent state read.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S05](../../docs/SOURCES.md#s05). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
