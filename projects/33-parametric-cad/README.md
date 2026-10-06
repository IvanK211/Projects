# Parametric enclosure and fit-coupon sources

**Category:** Mechanical design and fabrication  
**Archive status:** OpenSCAD source + rendered reference meshes

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Provide editable, generic mechanical reference files without claiming to recover original CAD, customer models or hardware-specific dimensions.

## Design and behavior

The enclosure is a plain tray and lid with configurable dimensions, wall thickness and fit clearance. The coupon tests several hole clearances alongside a nominal peg. These are newly authored reference geometries. Rendered STL files are included for convenience, but the parametric sources remain the editable authority. No fit, material, ingress or load certification is implied.

## Included implementation

- [projects/33-parametric-cad/enclosure.scad](../../projects/33-parametric-cad/enclosure.scad)
- [projects/33-parametric-cad/fit-coupon.scad](../../projects/33-parametric-cad/fit-coupon.scad)

## Workflow

1. Open the source in OpenSCAD and review the dimensional parameters before rendering.

2. Render the base with openscad -o base.stl enclosure.scad; render the lid with -D part="lid" using shell-appropriate quoting.

3. Print the fit coupon before committing to a complete enclosure and record material, orientation and machine conditions privately.

4. Adjust design clearances rather than blindly scaling the whole assembly when mating features need dimensional accuracy.

## Acceptance criteria

- The mesh renderer reports a valid closed solid for each enclosure part.
- The lid and base are separate printable parts.
- No real board mounting pattern or physical-security mechanism is encoded.

## Troubleshooting and limits

A watertight mesh is not a waterproof print.

Shrinkage, anisotropy and machine calibration can change a nominal fit.

A source file is not proof of a physically tested enclosure.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S21](../../docs/SOURCES.md#s21). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
