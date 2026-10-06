# Portable project notes and workflow scaffolding

**Category:** Developer tooling  
**Archive status:** Markdown templates + repository-index utility

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Keep technical notes portable between a Git repository and note-taking tools without embedding account IDs, shared workspace links or private task history.

## Design and behavior

The project-note template captures goals, decisions, experiments, test evidence and follow-up issues in plain Markdown. The index builder derives a repository file inventory from public candidates only. The notes can be manually imported into a workspace, but no Notion API integration, authentication flow or automatic upload is asserted to exist.

## Included implementation

- [projects/36-developer-productivity/project-note-template.md](../../projects/36-developer-productivity/project-note-template.md)
- [tools/build_index.py](../../tools/build_index.py)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python tools/build_index.py
```

## Workflow

1. Create a new note from the supplied template and describe the problem in generic terms.

2. Separate public reasoning from private operational evidence before adding attachments or links.

3. Regenerate the file index after adding approved source files.

4. Use issue templates for follow-up work and document validation level explicitly rather than writing a general done label.

## Acceptance criteria

- Notes remain readable without a hosted account.
- No workspace identifiers or real task records are required.
- The generated index includes source paths, not local private data.

## Troubleshooting and limits

A public note can leak an internal URL even when the attached file is absent.

An imported page may acquire workspace-specific metadata; do not re-export it blindly.

Convenient automatic sync is not implemented by this template.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
