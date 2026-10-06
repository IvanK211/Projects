# Low-voltage runtime and energy-budget calculator

**Category:** Engineering methods  
**Archive status:** Offline implementation

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Estimate runtime from an explicit energy model without recommending an actual battery pack, charger or protection circuit.

## Design and behavior

The calculation multiplies nominal voltage and amp-hours to obtain watt-hours, then applies a usable-energy fraction and conversion efficiency before dividing by load power. Inputs are checked for finite positive values and fractions no greater than one. The result is a planning estimate, not proof of electrical or battery safety.

## Included implementation

- [labkit/engineering.py](../../labkit/engineering.py)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit energy --voltage 5 --amp-hours 2 --watts 1.5 --usable-fraction 0.8 --efficiency 0.85 local-output/energy.json
```

## Workflow

1. Measure the load over representative idle, active and startup conditions rather than relying on one nominal current.

2. Use consistent voltage and capacity definitions and make conversion losses explicit.

3. Run the reference example and compare estimates across reasonable operating assumptions.

4. Use only appropriately designed power systems; cell matching, charging, protection, conductor size and enclosure temperature require separate review.

## Acceptance criteria

- Zero load power and non-finite inputs fail validation.
- Fractions are restricted to physically meaningful ranges.
- Estimated hours are not presented as a guaranteed runtime.

## Troubleshooting and limits

Amp-hours at different voltages cannot be compared as energy without conversion.

Startup/inrush current can exceed the average budget.

A capacity calculation does not validate series/parallel battery construction.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
