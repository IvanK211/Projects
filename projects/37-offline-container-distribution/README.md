# Offline container-image distribution

**Category:** Infrastructure and operations  
**Archive status:** Bash syntax-checked reference + transfer playbook

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Preserve the build-once, transfer-and-load workflow without including proprietary images, internal registry names, image layers or environment files.

## Design and behavior

The script saves an explicitly selected local image, compresses it reproducibly without a gzip timestamp and writes a checksum. It never builds a private source tree or publishes to a registry. The operational playbook separates source review, image scanning, manifest recording, transfer, verification and startup. A checksum detects modification but is not proof of a trusted signer.

## Included implementation

- [projects/37-offline-container-distribution/save-image.sh](../../projects/37-offline-container-distribution/save-image.sh)

## Workflow

1. Build only reviewed source with an approved base image and inspect the complete build context.

2. Check layers and metadata for copied secrets, credentials, private certificates and repository history.

3. Run the export and move only approved artifacts through the authorized transfer channel.

4. Verify the checksum, load in a lab, check runtime configuration and health, then record the tested image identity privately.

## Acceptance criteria

- The output archive is not silently overwritten.
- No environment file is bundled by the export helper.
- The recipient verifies provenance as well as integrity.

## Troubleshooting and limits

Deleting a secret in a later Docker layer does not remove it from earlier layers.

An offline host still needs a patch and vulnerability-review process.

A mutable tag can refer to different image content over time.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S13](../../docs/SOURCES.md#s13). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
