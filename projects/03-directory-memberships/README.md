# Directory group-membership audit

**Category:** Identity and endpoint security  
**Archive status:** Unverified live collector + analysis guide

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Export a bounded list of users and their group memberships while keeping direct and inherited relationships distinguishable.

## Design and behavior

The PowerShell collector takes an explicit local JSON array of user IDs. It uses a group type cast, optional name-prefix selection, and a separate switch for transitive membership. Output remains normalized JSON instead of generating an unbounded number of spreadsheet columns. A later presentation adapter may pivot this data for review without changing the relationship semantics.

## Included implementation

- [projects/03-directory-memberships/Export-GroupMemberships.ps1](../../projects/03-directory-memberships/Export-GroupMemberships.ps1)

## Workflow

1. Prepare the user-ID input in a protected private workspace; do not reuse any public example alias as a cloud identity.

2. Select direct membership for immediate assignments or transitive membership for inheritance, and record the choice with the review.

3. Approve Directory.Read.All only in a suitable test context; narrow the workflow further before a broad rollout.

4. Review disabled accounts, unexpected privileged memberships and ownerless groups using a separate decision record. This script never removes memberships.

## Acceptance criteria

- The input is a bounded list rather than a tenant-wide implicit sweep.
- Direct and transitive output contain an explicit relation label.
- A prefix filter does not change the underlying authorization model.

## Troubleshooting and limits

A group name is mutable and not a stable identifier.

Dynamic group membership should not be interpreted as a manual assignment.

A report is not approval to remove access.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S03](../../docs/SOURCES.md#s03). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
