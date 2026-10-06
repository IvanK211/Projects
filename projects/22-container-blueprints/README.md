# Independent container-service blueprints

**Category:** Infrastructure and operations  
**Archive status:** Deployment templates; not Docker-runtime validated

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Provide independent service examples without revealing a real stack, service combination, bind mount, port allocation or network diagram.

## Design and behavior

Each Compose file is self-contained and requires locally chosen image references and host ports. Published listeners bind to loopback. Named volumes replace real storage paths. The templates do not request privileged mode, host networking or access to the Docker socket. This intentionally trades automatic discovery and hardware access for an explicit, reviewable starting point.

## Included implementation

- [projects/22-container-blueprints/compose.mqtt.yaml](../../projects/22-container-blueprints/compose.mqtt.yaml)
- [projects/22-container-blueprints/compose.home-automation.yaml](../../projects/22-container-blueprints/compose.home-automation.yaml)
- [projects/22-container-blueprints/compose.firmware-dashboard.yaml](../../projects/22-container-blueprints/compose.firmware-dashboard.yaml)
- [projects/22-container-blueprints/.env.example](../../projects/22-container-blueprints/.env.example)

## Workflow

1. Select one blueprint rather than assuming all three are meant to run together.

2. Choose a reviewed image version or digest and supply variables through a private environment file.

3. Use docker compose config --quiet for validation; do not publish expanded configuration that contains local settings.

4. Validate permissions, persistence, updates, restore behavior and any separately approved device/network access before use.

## Acceptance criteria

- Missing required variables stop interpolation rather than inventing defaults.
- No public interface is exposed by a copied template.
- An image update has a recorded rollback and data-compatibility check.

## Troubleshooting and limits

A container image with a moving tag is not reproducibly pinned.

Bridge networking may not provide automatic discovery.

An environment file is configuration storage, not encryption or a secret manager.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S13](../../docs/SOURCES.md#s13). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
