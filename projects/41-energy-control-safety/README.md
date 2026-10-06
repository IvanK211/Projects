# Household energy-control safety architecture

**Category:** Home automation and embedded systems  
**Archive status:** Concept only; no mains wiring or construction files

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Retain the systems-engineering considerations for remotely controlled high-power loads without reproducing an actual circuit, load rating or enclosure installation.

## Design and behavior

The concept distinguishes supervisory automation from protective devices and manual isolation. A software command is not a thermostat, overcurrent device, contactor rating, grounding system or emergency cutoff. This project intentionally contains no mains wiring instructions, component substitutions or printable enclosure claimed suitable for an electrical installation.

## Included material

A design worksheet, acceptance criteria and an operating sequence are provided below and in [RUNBOOK.md](RUNBOOK.md). No executable integration or recovered proprietary configuration is claimed.

## Workflow

1. Document the intended supervisory behavior using a low-voltage indicator rather than the real load.

2. Have a qualified professional assess the actual load, protection, switching device, enclosure and installation constraints.

3. Define independent timeout, feedback, manual override and fault states without treating the automation platform as a safety controller.

4. Retain installation approval and inspection evidence privately; never infer that a generic reference authorizes a real installation.

## Acceptance criteria

- Loss of control connectivity has a documented safe outcome.
- Protective functions remain independent of remote software.
- No actual electrical design or deployment information is published.

## Troubleshooting and limits

Printed plastic is not automatically a compliant electrical enclosure.

A relay headline rating may not describe the relevant load type or duty.

Remote status may not prove the physical load is de-energized.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
