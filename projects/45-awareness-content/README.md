# Authorized awareness-simulation content kit

**Category:** Security reporting  
**Archive status:** Static training page + campaign worksheet

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Provide a non-credential-collecting landing page and a planning worksheet for authorized security-awareness exercises.

## Design and behavior

The static page clearly identifies itself as a training example. It includes no forms, tracking pixels, scripts, cookies or external resources. The campaign worksheet defines approval, scope, learning objective, recipient safeguards, reporting behavior and debrief. It does not reproduce a real campaign, brand impersonation, recipient list or company communication.

## Included implementation

- [projects/45-awareness-content/simulation-landing.html](../../projects/45-awareness-content/simulation-landing.html)

## Workflow

1. Obtain explicit campaign authorization and define the learning objective before adapting any content.

2. Use a test population and synthetic business context for development.

3. Review accessibility, support impact, exclusions and how participants can report a suspicious message.

4. Debrief with aggregated outcomes using the phishing analytics project rather than exposing individual participants publicly.

## Acceptance criteria

- The shipped page cannot submit credentials.
- No external request is needed to render it.
- Campaign results remain private unless separately approved and de-identified.

## Troubleshooting and limits

Training effectiveness is not established by click rate alone.

An exercise can disrupt trust if its scope and debrief are poorly designed.

A legitimate simulation does not justify publishing participant identities.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S07](../../docs/SOURCES.md#s07). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
