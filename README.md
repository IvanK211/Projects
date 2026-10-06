# Technical Projects - Public Reference Edition

A reusable engineering portfolio spanning security operations, identity, privileged access, reporting, Linux, containers, embedded systems and mechanical design.

**45 project folders. Synthetic data only. No original infrastructure inventory. No deployment claims.**

This is a newly reconstructed reference collection, not a dump of production source, private conversations, configurations or company reports. It preserves reusable methods while replacing the environment with independent, fictional examples. The projects are deliberately **not connected into a representation of any real setup**.

## Start here

Read the [project catalog](PROJECTS.md) to browse by topic, the [file index](FILE_INDEX.md) to locate every file, and the [validation record](docs/VALIDATION.md) to distinguish executed tests from untested integrations. The [coverage and provenance note](docs/COVERAGE.md) explains what reconstruction means and what is intentionally absent.

```text
tech-projects-public/
  README.md                 Entry point
  PROJECTS.md               45-project catalog with maturity/status
  FILE_INDEX.md             Navigable file inventory
  docs/                     Architecture, privacy, usage, sources and validation
  projects/                 Project-specific guides, runbooks and implementation files
  labkit/                   Dependency-free offline Python tools
  examples/                 Newly invented JSON inputs
  powershell/               Shared Graph read and export helpers
  tests/                    Offline regression tests
  tools/                    Demo, privacy scan, indexing and packaging utilities
  .gitlab/                  Issue and merge-request templates
  .gitlab-ci.yml            Non-deploying validation pipeline template
  MANIFEST.sha256           Release file integrity hashes
```

## Run the offline examples

From this directory, use Python 3.11 or newer. The core tools and tests need no third-party packages, account access or network connection.

```bash
python -m unittest discover -s tests -v
python tools/run_demo.py
python tools/privacy_scan.py
python tools/check_repository.py
```

The demo executes 17 command-line workflows in a temporary directory and removes their outputs. To inspect synthetic results, choose an ignored local folder:

```bash
python tools/run_demo.py --output local-output/demo
python -m labkit --help
python -m labkit inventory examples/inventory.json local-output/inventory.json
python -m labkit training examples/training.json local-output/training.json
python -m labkit pam-plan examples/pam-accounts.json local-output/plan.json --suffix example.invalid --port 8443
```

The PAM command above **only produces a plan**. It does not connect to a vault. Separate PowerShell files that can connect to external systems are explicitly labeled in their project guides.

## What the collection contains

| Area | Representative contents |
|---|---|
| Identity and endpoints | Managed-device reconciliation, PIM request reporting, memberships, Defender KQL, DLP and access-rollout guides |
| Privileged access | Reviewed port-change plans, a guarded apply template, initiating-user session analytics, onboarding and browser-connector checks |
| Vulnerability and awareness | Metadata classification, risk evidence, scan operations, training obligations and exposure-weighted phishing metrics |
| Security reporting | KPI calculations, HTML output, board-report outline, local SIEM snapshot viewer and structured-log summaries |
| Infrastructure | Linux diagnostics, bounded watchdog, endpoint-copy transformation, independent Compose profiles, encrypted-backup and offline-image scripts |
| Automation and hardware | MQTT ACLs, lighting automation, a fail-safe water-controller template, RFID lab sketches and a nonblocking event timer |
| Engineering | Sensor drift, flow and energy estimates, parametric enclosure sources, fit-coupon meshes, FDM worksheets and concept designs |

## Maturity and safe use

An **offline implementation** performs useful local work on a documented input. A **live collector/executor template** requires credentials, permissions, platform validation and a controlled test. A **firmware or configuration template** has not been proven on physical hardware or a deployed service. A **design/concept** describes an approach, not a completed product. See each `project.json` and the validation record; do not present all folders as deployed projects.

Do not substitute real input and then commit the generated output. A read-only export can still contain sensitive identity, asset, policy or activity data. Local operational files belong outside this public repository; ignored folders are a convenience, not a security boundary.

## Publishing to GitLab

Follow the [GitLab upload guide](docs/GITLAB.md). The archive contains no Git history, account identity, remote, CI secret or deployment target. Create a new repository rather than pushing an old working tree that may contain private history. Keep the initial project private while checking publication rights and Git author metadata.

The CI file is a portable template, not evidence of a successful GitLab pipeline. It uses synthetic fixtures and does not deploy or collect live data. Public container tags must be reviewed and pinned according to the destination's supply-chain policy.

## Documentation map

[Architecture](docs/ARCHITECTURE.md) / [Data contracts](docs/DATA_CONTRACTS.md) / [Dependencies](docs/DEPENDENCIES.md) / [Privacy](docs/PRIVACY.md) / [Threat model](docs/THREAT_MODEL.md) / [Sources](docs/SOURCES.md) / [Contributing](CONTRIBUTING.md) / [Security](SECURITY.md) / [License status](LICENSE)
