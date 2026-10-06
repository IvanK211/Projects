# Privacy and publication boundary

## What is public

Only newly written reference code, generic documentation, independent fictional examples and newly generated demonstration meshes are intended for release. Example domains use the reserved example namespace. Sample IP observations use documentation ranges; loopback addresses are used for local demonstrations. These are explanatory values, not deployment recommendations.

No real architecture is shown. Separate container and automation examples must not be read as components of one existing environment. Product names are retained only to identify interfaces and transferable skills.

## What must remain private

Credentials, tokens, certificates, private keys, authentication headers, raw API responses, account identifiers, asset lists, internal URLs, device serials, usernames, real membership lists, alert messages, screenshots, backups, database files and organization-specific policies belong outside the published tree. Even sanitized aggregates can disclose sensitive small groups, incidents or operational capacity. Do not treat aggregation or replacement of names alone as anonymization.

Runtime exports should be stored in a separately access-controlled directory. `local-output/`, `local-data/` and `private/` are ignored by Git and omitted by the release packager, but this does not encrypt them or prevent accidental attachment elsewhere. Python JSON output files use a private temporary file before atomic replacement on POSIX. PowerShell exports require a destination folder with suitable OS ACLs. Restrict Windows folder permissions before collecting data.

## Before publishing

Run `python tools/privacy_scan.py`, `python tools/check_repository.py` and the tests. Inspect `git diff --cached` after staging. Review every new data sample and every domain. Look at file names and author metadata as well as contents. Never publish raw logs to demonstrate that a scanner passed. The scanner reports only file locations and rule labels, not matched values.

The built-in scanner flags common token patterns, private-key blocks, non-example email addresses, non-documentation IPv4 values, MAC addresses, UUID-like identifiers, embedded URL credentials and personal home paths. Unknown binary or large files fail the release check. Its rules are deliberately modest and auditable; it is **not a comprehensive secret detector, PII detector or proof of zero disclosure**. It does not recognize every opaque password, every personal name, every internal domain or every proprietary design.

A private, local denylist can complement the generic scan. Keep that list outside the repository and do not commit a redaction mapping: the mapping itself would reveal the information being protected. Automated checks were supplemented with a review of this edition; later edits invalidate that review.

## Git and archive metadata

Use a new repository. Old commits, branches, tags, reflogs, Git LFS objects and deleted files can retain secrets even when the current tree looks clean. This ZIP contains no `.git` directory. ZIP entry times and permissions are normalized; no author identity is injected into CAD or report files. The release manifest hashes only public candidate files, not original private material.

GitLab visibility and a clean source tree do not hide a commit author's name/email, account profile, issue discussion, CI job log or uploaded artifact. Select an appropriate public author identity and verified private/no-reply email in your own account settings. No identity is prefilled by this package.

## Incident response

When a secret has been published, revoke or rotate it first. Treat deletion and history rewriting as cleanup, not revocation. Review mirrors, forks, cached jobs and release attachments using the destination's procedures. Do not paste the secret into a public issue to ask for help. Publish only a minimal description of the problem and use an approved private reporting channel.

See [GitLab publishing](GITLAB.md), [threat model](THREAT_MODEL.md) and [security policy](../SECURITY.md).
