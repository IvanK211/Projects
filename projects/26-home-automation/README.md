# Presence, night-mode and lighting automations

**Category:** Home automation and embedded systems  
**Archive status:** Home Assistant YAML template; runtime unverified

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Provide a small lighting example and design guidance for presence/night-mode logic without describing a real home layout or sensor count.

## Design and behavior

The package separates a night-mode flag, motion-on behavior and delayed inactivity-off behavior. Entity names and brightness choices are arbitrary examples. Presence is treated as an observation that can be unknown, delayed or contradictory. Alarm-related ideas remain a design exercise and are not represented as a certified or dependable security alarm.

## Included implementation

- [projects/26-home-automation/lighting-package.yaml](../../projects/26-home-automation/lighting-package.yaml)

## Workflow

1. Copy the package into a disposable Home Assistant test configuration and replace fictional entities privately.

2. Use an indicator lamp before controlling any meaningful load.

3. Test sensor on/off, unavailable state, repeated motion, manual light changes and a controller restart.

4. Decide explicitly whether manual overrides persist, and how delayed-off behavior should recover after a restart.

## Acceptance criteria

- Night mode changes the selected brightness in the reference logic.
- A stale or unavailable sensor is not assumed to mean a safe empty room.
- Manual override and restart semantics are documented rather than implicit.

## Troubleshooting and limits

A state trigger with a duration does not preserve its timer across every restart/reload.

Multiple independent schedules can fight over the same actuator.

Convenience automation is not a substitute for life-safety or certified security systems.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S16](../../docs/SOURCES.md#s16). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
