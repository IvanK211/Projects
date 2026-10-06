# Safe local development and demonstration workflow

**Category:** Developer tooling  
**Archive status:** Operational checklist

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Preserve workstation and lab troubleshooting habits without distributing security-control bypasses or weakening a managed endpoint.

## Design and behavior

The guide separates convenience settings for an owned demonstration environment from organization-managed controls. It covers serial output troubleshooting, Python module invocation, local web-server binding, notebook handling and temporary presentation needs. It contains no automatic screen-lock disablement, endpoint-protection exclusion or credential-capture workaround.

## Included material

A design worksheet, acceptance criteria and an operating sequence are provided below and in [RUNBOOK.md](RUNBOOK.md). No executable integration or recovered proprietary configuration is claimed.

## Workflow

1. Confirm that the environment is an owned or explicitly authorized lab before changing a setting.

2. Check the selected serial port, baud rate and application output channel before changing firmware.

3. Bind demonstration web services to loopback and use synthetic data.

4. For presentation-related lock/sleep changes, use approved temporary settings and restore them afterward; do not override a managed security policy.

## Acceptance criteria

- A troubleshooting procedure starts with observation rather than disabling protections.
- Demo servers are not accidentally reachable from other machines.
- Temporary convenience changes have an explicit restoration step.

## Troubleshooting and limits

A local notebook can still read private files or load untrusted code.

A missing serial output can be a port or baud issue rather than a failed program.

A shell history or notebook output may contain secrets even when the source is clean.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S12](../../docs/SOURCES.md#s12). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
