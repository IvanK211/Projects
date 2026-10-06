# FDM print quality, maintenance and material selection

**Category:** Mechanical design and fabrication  
**Archive status:** Design and maintenance worksheets

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Collect reusable troubleshooting methods for noise, fit, leakage, material handling and post-processing without copying a printer profile or machine-specific calibration.

## Design and behavior

The worksheet separates mechanical condition, material condition, slicer settings and geometry. Changes are treated as experiments with a baseline and one controlled variable. Manufacturer limits take precedence over a generic recipe. The guide avoids fixed material temperatures, lubricant prescriptions, enclosure modifications and unsupported food-contact claims.

## Included material

A design worksheet, acceptance criteria and an operating sequence are provided below and in [RUNBOOK.md](RUNBOOK.md). No executable integration or recovered proprietary configuration is claimed.

## Workflow

1. Record the symptom and create a small representative test rather than repeatedly printing a full assembly.

2. Check the machine manual for maintenance points, compatible consumables and safety limits.

3. Inspect dimensional accuracy, layer adhesion and leakage independently; success in one does not establish the others.

4. For post-processing, follow the material and product safety documentation, ventilation requirements and cure conditions. Keep real profiles and maintenance history private.

## Acceptance criteria

- A test isolates one variable and records the outcome.
- A fit coupon is used before a functional mating part.
- No material suitability claim is based solely on a filament marketing name.

## Troubleshooting and limits

Changing speed can also change cooling, flow and adhesion.

A composite material may require different wear-resistant components.

A replacement build surface must match usable area, thickness and retention method, not just a nominal printer family.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S21](../../docs/SOURCES.md#s21). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
