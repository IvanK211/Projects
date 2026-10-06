# Fail-safe low-voltage water-controller bench

**Category:** Home automation and embedded systems  
**Archive status:** ESPHome firmware template; hardware unverified

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Demonstrate local water-level interlocking and bounded actuator pulses without publishing actual wiring, pump ratings, schedules or network credentials.

## Design and behavior

The reference assumes a healthy float input closes a circuit to ground, making a disconnected input unsafe. The output is internal, starts off and accepts only a short bench pulse when the input is known and healthy. A local check and release action turn it off independently of Home Assistant. GPIO assignments are arbitrary reference choices, and software is not a safety-rated protection layer.

## Included implementation

- [projects/27-water-controller/controller.yaml](../../projects/27-water-controller/controller.yaml)
- [projects/27-water-controller/secrets.yaml.example](../../projects/27-water-controller/secrets.yaml.example)

## Workflow

1. Review the chosen board pinout and input/output electrical levels before connecting anything.

2. Use a low-energy indicator first; create real API, OTA and Wi-Fi secrets only in a private secrets file.

3. Confirm that unknown input, open wire, low level, network loss and reboot do not request an energized output.

4. Add pump-specific protection, independent hardware interlocking and a validated schedule only through a separate engineering review. No production irrigation schedule is supplied.

## Acceptance criteria

- The output starts off after firmware boot.
- A valid bench request terminates even without network connectivity.
- Removing the healthy input stops the pulse.

## Troubleshooting and limits

A relay can energize during boot before firmware configures a pin; external hardware must address this.

Active-low and active-high driver boards are not interchangeable.

The chosen two-second pulse is a bench demonstration, not crop or pump guidance.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S17](../../docs/SOURCES.md#s17). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
