# Controlled measurement and solution-observation protocol

**Category:** Engineering methods  
**Archive status:** Experiment templates; no chemical-dosing automation

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Preserve the experimental method behind repeated water-quality troubleshooting without including historical readings, chemical amounts, product mixtures or reservoir details.

## Design and behavior

The protocol distinguishes sensor calibration, sampling, mixing, temperature, gas exchange and solution composition. It uses baseline/control comparisons and one-variable-at-a-time changes. pH, conductivity, alkalinity and oxidation-reduction readings are not treated as interchangeable quantities. The supplied material contains no peroxide, acid, disinfectant or concentrated-chemical dosing instructions.

## Included material

A design worksheet, acceptance criteria and an operating sequence are provided below and in [RUNBOOK.md](RUNBOOK.md). No executable integration or recovered proprietary configuration is claimed.

## Workflow

1. Define the hypothesis and the measurement that would distinguish it from alternatives.

2. Use a separate reference sample and keep sample context explicit; never compare different locations as though they were the same sample.

3. Record measurement time, temperature, instrument state and settling/mixing criteria before interpreting a drift.

4. For treatment decisions, use manufacturer instructions and qualified water analysis rather than deriving a chemical dose from one pH reading.

## Acceptance criteria

- The log can distinguish a system observation from a separate sample observation.
- The experimental design has a baseline and a stopping criterion.
- No apparent correlation is presented as a confirmed chemical mechanism.

## Troubleshooting and limits

pH alone does not describe buffering capacity.

Changing several variables at once makes causal interpretation weak.

Visible clarity or odor is not a validated microbial-safety test.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S18](../../docs/SOURCES.md#s18). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
