# Nonblocking two-team event timer

**Category:** Home automation and embedded systems  
**Archive status:** Arduino reference sketch; hardware build unverified

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Preserve the reusable user-interface and timing logic of a two-team timer without including hazardous accessories, actual event rules or a real enclosure design.

## Design and behavior

The reference uses two team buttons, a pause button and a board LED. Inputs are debounced without delay-based waiting. The elapsed-time calculation uses unsigned subtraction for timer wraparound, and simultaneous team presses resolve to pause rather than a hidden priority. Time is reported through serial so display wiring is not assumed.

## Included implementation

- [projects/31-embedded-timer/TeamTimer/TeamTimer.ino](../../projects/31-embedded-timer/TeamTimer/TeamTimer.ino)

## Workflow

1. Compile for a reviewed Arduino-compatible board and verify the arbitrary reference pin assignments.

2. Test the state transitions with no external actuators connected.

3. Compare measured elapsed time with an independent clock during rapid team changes and long pauses.

4. Add a display through a separate adapter and document restart/persistence behavior before using the timer in an event.

## Acceptance criteria

- The timer starts paused and a pause press stops accumulation.
- Holding a button does not generate repeated state-change events.
- Timing continues without blocking while input debouncing runs.

## Troubleshooting and limits

Restarting loses volatile counters in this reference.

Software timing is not a calibrated official timing system.

Battery packs and enclosure wiring need a separate electrical review.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S20](../../docs/SOURCES.md#s20). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
