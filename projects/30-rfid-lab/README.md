# MFRC522 checker, reader and guarded lab writer

**Category:** Home automation and embedded systems  
**Archive status:** Three Arduino sketches; hardware build unverified

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Provide separate reader diagnostics, public-UID reading and a deliberately disabled, fixed-data write demonstration for disposable owned tags.

## Design and behavior

The checker tests communication and identifies a compatible card type. The reader outputs the public UID without attempting protected-sector discovery. The writer requires a compile-time enable flag and a serial arming command, accepts only listed MIFARE Classic types, authenticates with the known factory lab key and writes block 4 followed by read-back verification. It never writes block 0 or a sector trailer.

## Included implementation

- [projects/30-rfid-lab/Checker/Checker.ino](../../projects/30-rfid-lab/Checker/Checker.ino)
- [projects/30-rfid-lab/Reader/Reader.ino](../../projects/30-rfid-lab/Reader/Reader.ino)
- [projects/30-rfid-lab/Writer/Writer.ino](../../projects/30-rfid-lab/Writer/Writer.ino)

## Workflow

1. Check breakout supply and logic-level specifications; a board powered at the correct voltage can still receive an unsafe signal level.

2. Install the upstream MFRC522 library and open the Serial Monitor at the sketch baud rate.

3. Run Checker, then Reader, using a supported disposable tag. Investigate wiring and compatibility before assuming a tag is damaged.

4. Use Writer only on a tag you own and can erase. Keep writes disabled until the code and block layout have been reviewed.

## Acceptance criteria

- No write is possible with the shipped compile-time flag.
- Unsupported card types and failed authentication cause no fallback key attempts.
- A successful write requires a matching read-back result.

## Troubleshooting and limits

MFRC522 compatibility is not universal across all RFID frequencies and protocols.

A UID is not a secure authentication mechanism.

No access-card cloning, key recovery or access-system bypass is included.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S19](../../docs/SOURCES.md#s19). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
