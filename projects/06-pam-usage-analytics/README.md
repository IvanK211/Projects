# PAM session-usage analytics

**Category:** Privileged access management  
**Archive status:** Offline implementation + collection specification

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Count session evidence by the initiating identity rather than by the privileged account used on the target system.

## Design and behavior

The normalized schema separates recording ID, initiating user, target user and start/end timestamps. Duplicate recordings are rejected, invalid durations fail validation, and unfinished recordings contribute to an unknown-duration count rather than zero seconds. A live recordings API adapter is intentionally not invented here; its pagination, permission and timestamp behavior must be verified for the chosen platform.

## Included implementation

- [labkit/pam.py](../../labkit/pam.py)
- [examples/pam-sessions.json](../../examples/pam-sessions.json)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python -m labkit sessions examples/pam-sessions.json local-output/pam-usage.json
```

## Workflow

1. Normalize an authorized recordings metadata export into the example schema; do not include recordings, transcripts, passwords or command content.

2. Choose a reporting window and establish whether timestamps represent UTC seconds, milliseconds or ISO strings before conversion.

3. Run the grouping and inspect missing initiating users, duplicate IDs and incomplete sessions.

4. Present session counts as activity evidence, not automatically as productivity, security quality, or total PAM adoption.

## Acceptance criteria

- The target account cannot accidentally become the human-usage grouping key.
- Open recordings do not contribute a fabricated duration.
- Retention limitations remain visible in the report narrative.

## Troubleshooting and limits

A recording count can differ from a user login count.

Missing recordings may result from policy, failure or retention; do not assume non-use.

Session metadata is still sensitive even without the recording file.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S05](../../docs/SOURCES.md#s05). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
