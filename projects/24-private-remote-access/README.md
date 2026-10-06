# Private remote-administration design

**Category:** Infrastructure and operations  
**Archive status:** Design and recovery runbook

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Explain secure administrative access patterns without exposing peers, routes, keys, SSH usernames or real access-control policies.

## Design and behavior

The design compares direct local administration, a private overlay network and a gateway-mediated path as separate options. It documents identity, device trust, least-privilege reachability, key lifecycle and emergency access. No peer list, tailnet policy, firewall export or installed-agent configuration is included.

## Included material

A design worksheet, acceptance criteria and an operating sequence are provided below and in [RUNBOOK.md](RUNBOOK.md). No executable integration or recovered proprietary configuration is claimed.

## Workflow

1. List the minimum administrative flows in a private matrix and separate human access from machine-to-machine access.

2. Use independently authenticated identities and approve only the needed destinations and services.

3. Validate DNS, route selection and the recovery console before tightening SSH or firewall policy.

4. Test lost-device revocation, expired credentials, overlay outage and key replacement without exposing an administrative service publicly.

## Acceptance criteria

- A compromised peer does not automatically receive broad network reachability by design.
- A recovery method exists without depending on the same failed access path.
- Private keys and network topology never enter the public repository.

## Troubleshooting and limits

An encrypted tunnel does not replace application authentication.

A route announcement can broaden exposure beyond one service.

A successful connection is not proof that access policy is minimal.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S12](../../docs/SOURCES.md#s12). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
