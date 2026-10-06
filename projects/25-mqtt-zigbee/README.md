# MQTT authorization and Zigbee integration lab

**Category:** Home automation and embedded systems  
**Archive status:** Configuration example + design guide

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Preserve messaging, pairing and troubleshooting patterns without publishing device identifiers, network keys or an installed sensor inventory.

## Design and behavior

The broker reference separates a controller identity from an observer identity and restricts them to fictional topic paths. Zigbee commissioning is documented as a separate trust step, not as an automatic extension of MQTT authentication. Retained messages, availability and device naming require their own lifecycle rules.

## Included implementation

- [projects/25-mqtt-zigbee/acl.example](../../projects/25-mqtt-zigbee/acl.example)
- [projects/22-container-blueprints/mosquitto.conf](../../projects/22-container-blueprints/mosquitto.conf)

## Workflow

1. Create broker accounts privately and verify that their names match the reviewed ACL entries.

2. Test permitted reads/writes and rejected cross-topic operations before adding automation.

3. Pair a disposable device during a bounded commissioning window and then disable joining.

4. Document retained-state cleanup, controller replacement, network-key backup and recovery in a protected operations record.

## Acceptance criteria

- Anonymous clients cannot publish to the reference broker.
- The observer cannot send control messages.
- A stale retained message cannot silently be treated as a fresh safety decision.

## Troubleshooting and limits

A Zigbee radio frequency match is not proof that a device supports the expected application profile.

Changing a friendly device name can break automations if identity mapping is not stable.

Network keys, coordinator backups and device IDs are private configuration.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S15](../../docs/SOURCES.md#s15). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
