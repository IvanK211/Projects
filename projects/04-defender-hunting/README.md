# Endpoint identity and network hunting queries

**Category:** Identity and endpoint security  
**Archive status:** KQL templates; not executed against a tenant

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Provide reusable read-only queries for current observations, exact hostname selection, and historical IP-to-device investigation.

## Design and behavior

Each query carries its own lookback window. Device records are keyed by DeviceId rather than a name that may be reused. Network address arrays are parsed before expansion, and historical observations remain timestamped. The examples use documentation-only names and addresses; they do not describe an actual endpoint population.

## Included implementation

- [projects/04-defender-hunting/latest-device-identity.kql](../../projects/04-defender-hunting/latest-device-identity.kql)
- [projects/04-defender-hunting/ip-to-device.kql](../../projects/04-defender-hunting/ip-to-device.kql)
- [projects/04-defender-hunting/exact-hostnames.kql](../../projects/04-defender-hunting/exact-hostnames.kql)
- [projects/04-defender-hunting/device-network-history.kql](../../projects/04-defender-hunting/device-network-history.kql)

## Workflow

1. Open a query in an authorized hunting workspace and check the current table schema before adapting it.

2. Replace only the documented synthetic filter in a private copy, then choose a retention-compatible time window.

3. Compare endpoint observations with other authorized network records before making attribution decisions.

4. Document a missing-result investigation: onboarding, telemetry arrival, time window, product availability, and permissions.

## Acceptance criteria

- An IP lookup returns potentially multiple devices and time ranges.
- Hostname selection uses equality rather than a broad contains match.
- No query isolates a device, changes policy, or executes a response action.

## Troubleshooting and limits

A last-observed address is not necessarily a current address.

DHCP, NAT, adapters and VPNs can make a single-IP identity claim misleading.

No rows may indicate a collection or scope problem rather than a clean environment.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S04](../../docs/SOURCES.md#s04). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
