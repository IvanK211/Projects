# Encrypted snapshot and restore verification

**Category:** Infrastructure and operations  
**Archive status:** Bash syntax-checked reference; encryption round-trip pending

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Create encrypted snapshots of a deliberately quiesced directory and verify recoverability without restoring over a live system.

## Design and behavior

The backup script streams tar into age using a supplied public recipient and writes a checksum alongside the encrypted file. It refuses the filesystem root and a destination nested within the source. The verify script checks the hash and decrypts into an archive listing rather than extracting. Application consistency, retention, off-site transfer and full restore remain separate operational responsibilities.

## Included implementation

- [projects/23-encrypted-backup/backup.sh](../../projects/23-encrypted-backup/backup.sh)
- [projects/23-encrypted-backup/verify-backup.sh](../../projects/23-encrypted-backup/verify-backup.sh)

## Workflow

1. Export databases using their supported backup method and quiesce changing application data before invoking this directory snapshot reference.

2. Choose a destination outside the source and validate its available space, access control and actual mount state.

3. Keep decryption identities separate from the repository and backup medium; document private recovery access.

4. Verify the archive, restore only in an isolated scratch environment with a reviewed safe extraction process, and test the application before treating the backup as successful.

## Acceptance criteria

- An encryption or tar failure returns a failed command.
- A destination inside the source is rejected.
- A successful archive listing is not reported as a completed application recovery.

## Troubleshooting and limits

A mounted share can disappear and leave an ordinary local directory at the same path.

Encrypted backups can still reveal filenames and metadata through sidecars or logs.

Changing live database files are not made consistent by tar alone.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S14](../../docs/SOURCES.md#s14). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
