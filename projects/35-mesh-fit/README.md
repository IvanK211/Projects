# Uniform bounding-box fit calculator

**Category:** Mechanical design and fabrication  
**Archive status:** Offline implementation

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Calculate a uniform scale that fits one bounding box inside another with explicit per-side clearance.

## Design and behavior

The calculation subtracts twice the clearance from each target dimension, computes each axis ratio and uses the smallest ratio as the uniform scale. It reports the scale, percentage and resulting dimensions. It does not parse a mesh, infer orientation or determine whether a functional interface remains valid after scaling.

## Included implementation

- [labkit/engineering.py](../../labkit/engineering.py)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit fit --source 60 40 30 --target 90 70 50 --clearance 0.5 local-output/fit.json
```

## Workflow

1. Measure or extract source and target bounding boxes in the same units.

2. Choose orientation before calculating; swapping axes changes the fit.

3. Run the reference command and inspect the limiting dimension.

4. For real mating geometry, use a parametric redesign when holes, wall thickness or external hardware must keep their size.

## Acceptance criteria

- Zero/negative source dimensions are rejected.
- Clearance that consumes the target is rejected.
- Every scaled dimension fits within the reduced target bounds.

## Troubleshooting and limits

Bounding-box fit does not guarantee collision-free assembly.

Uniform scaling changes screw holes and wall thickness too.

An apparent fit may still lack assembly clearance or account for print variation.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
