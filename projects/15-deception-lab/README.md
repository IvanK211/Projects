# Defensive deception and canary lab

**Category:** Detection engineering  
**Archive status:** Local demonstration + design playbook

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Demonstrate interaction-triggered alerting without using real secrets, collecting credentials or exposing a decoy to the internet.

## Design and behavior

The supplied listener is loopback-only and records an event type, method and timestamp. It does not retain headers, query strings, bodies or client addresses. Broader decoy ideas for database, file-sharing, remote-access and messaging services are described as separate lab designs. No network placement, NAC rules, real honeytokens or decoy images are included.

## Included implementation

- [projects/15-deception-lab/canary.py](../../projects/15-deception-lab/canary.py)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python projects/15-deception-lab/canary.py --port 8098
```

## Workflow

1. Start the local listener and request its endpoint from the same machine to create a synthetic event.

2. Define detection ownership, permitted test sources and cleanup rules before any networked deception exercise.

3. Use clearly nonfunctional lab credentials and never make a decoy a route into a real environment.

4. Evaluate alert routing, false positives and containment independently from how convincing the decoy looks.

## Acceptance criteria

- One authorized interaction produces one minimal event.
- No command execution or credential submission path exists.
- Networked deployment remains an explicit future design review.

## Troubleshooting and limits

Discoverability, network segmentation and alert delivery are separate problems.

A decoy is not safe merely because it is intended to be fake.

Credential harvesting and production lateral-movement demonstrations are not part of this reference.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
