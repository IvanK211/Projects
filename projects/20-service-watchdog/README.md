# Bounded Linux service watchdog

**Category:** Infrastructure and operations  
**Archive status:** Bash syntax-checked reference; service recovery unverified

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Observe a service and optionally attempt a bounded restart without hiding repeated failure in an infinite restart loop.

## Design and behavior

Observation is the default mode. Apply mode requires explicit arguments, approved root execution, a root-owned mode-700 state directory and a file lock. The cooldown tracks attempts rather than successful recovery, which prevents a consistently broken service from being restarted every timer tick. The systemd examples remain observation-only until adapted privately.

## Included implementation

- [projects/20-service-watchdog/watchdog.sh](../../projects/20-service-watchdog/watchdog.sh)
- [projects/20-service-watchdog/reference-watchdog.service.example](../../projects/20-service-watchdog/reference-watchdog.service.example)
- [projects/20-service-watchdog/reference-watchdog.timer.example](../../projects/20-service-watchdog/reference-watchdog.timer.example)

## Workflow

1. Run bash watchdog.sh SERVICE in a lab and inspect the status without allowing changes.

2. Investigate configuration, connectivity and vendor health checks before treating a restart as a fix.

3. Create and protect a dedicated state directory only after review; use --apply solely for a disposable or approved service.

4. Test the cooldown, concurrent invocation, invalid state and failed-restart paths before scheduling a timer.

## Acceptance criteria

- No restart occurs without --apply.
- Concurrent runs do not perform duplicate recovery actions.
- Persistent failure produces a failure exit rather than a false-success message.

## Troubleshooting and limits

A systemd active state does not prove application-level health.

Service restarts may interrupt users or erase useful diagnostic state.

Recovery state and logs must remain outside the public repository.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S12](../../docs/SOURCES.md#s12). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
