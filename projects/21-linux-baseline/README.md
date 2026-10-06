# Linux host baseline and diagnostics

**Category:** Infrastructure and operations  
**Archive status:** Read-only shell reference

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Collect a small, understandable operational baseline without automatically changing a firewall, SSH authentication or storage layout.

## Design and behavior

The script reports distribution/kernel information, filesystem and block-device sizes, listening sockets, failed systemd units and optional SSH configuration validation. It deliberately avoids serial-number inventory. Its output can still reveal sensitive infrastructure and must never be committed. Hardening changes are handled through a separate worksheet and tested recovery path.

## Included implementation

- [projects/21-linux-baseline/audit-host.sh](../../projects/21-linux-baseline/audit-host.sh)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
bash projects/21-linux-baseline/audit-host.sh
```

## Workflow

1. Read the script before executing it; redirect output only to a protected private location.

2. Inspect storage pressure and failed units before changing service settings.

3. For SSH changes, validate configuration, retain a recovery console and test a second session before closing the first.

4. For firewall changes, document required management flows and test rollback rather than applying a blanket rule set from a tutorial.

## Acceptance criteria

- The supplied script performs no policy writes or service restarts.
- Filesystem size is not confused with free space or partition capacity.
- A hardening proposal includes a tested administrative recovery route.

## Troubleshooting and limits

Listening sockets and mount points are operational details even without hostnames.

Firewall behavior for containers may differ from a simple host-only assumption.

Disabling password authentication before validating keys can lock out administration.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S12](../../docs/SOURCES.md#s12). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
