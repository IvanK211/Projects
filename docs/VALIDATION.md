# Validation record

Edition 0.1.0. Checks performed on 2026-10-06 using synthetic data only. No real account, device, organization, household system or GitLab project was contacted for integration testing.

## Executed checks

| Check | Result | What this establishes |
|---|---|---|
| Python regression suite | 89 tests passed | Local normalization, calculations, negative cases, safe output behavior and privacy-rule examples |
| Offline CLI demo | 17 workflows passed | Entry points accept bundled fixtures, write parseable results and complete without network access |
| Node syntax and local HTTP | 11 HTTP checks passed | Loopback viewer handles liveness, stale/empty/future snapshots, readiness, invalid input, route/method boundaries and safe text rendering |
| Bash syntax | 5 files passed `bash -n` | Shell grammar only; no service restart, host audit, backup or Docker operation was executed |
| YAML parsing | 7 files parsed | YAML syntax, with an explicit handler for the firmware secret-reference tag; not runtime schema compatibility |
| CAD generation | 3 STL files rendered | OpenSCAD could evaluate the newly authored models |
| Mesh inspection | 3 closed meshes with positive volume | Basic geometric integrity, not printability, load capacity or board-specific fit |
| Repository checks | Python AST, JSON, relative links and project counts checked | Structural consistency and readable source formats |
| Publication checks | Generic scanner plus a private known-identifier review | No findings from the applied checks; not an exhaustive anonymization proof |

The Python suite ran on Python 3.13.5. The local viewer was checked with Node.js 22.16.0. These are test-tool versions, not versions of a user's actual systems. The core code targets Python 3.11+; other supported versions were not independently exercised.

## Important negative coverage

Tests include exact-name matching, duplicate identities, missing timestamps, timezone offsets, zero denominators, non-finite numbers, inactive users, repeated enrollments, invalid ports and suffixes, retained PAM property maps, unknown session duration, counter resets, source changes, stale/future IP observations, HTML escaping, rejected input overwrite and scanner behavior. The suite uses fixtures created specifically for this release.

The SIEM viewer's bundled timestamp is deliberately historical. It therefore reports unknown/stale, not a fabricated live green state. Separate temporary fixtures were used to test healthy and failed states. The local listener and temporary files were removed after testing.

## Not validated

PowerShell is supplied as reviewed source, not interpreter-tested code. Microsoft Graph authorization, pagination responses, PIM retention, PAM property semantics, browser connectors, Defender KQL and other provider integrations were not executed against a tenant or vault. The Graph helper's empty-array and advanced-query handling were reviewed but still require a PowerShell and authorized API test.

Docker images were not pulled or started. Compose examples require local image/port/file/identity configuration and runtime testing. `age` encryption/decryption and an application-consistent restore were not executed. Systemd behavior, host audit results and service-recovery behavior were not tested on a target machine.

Home Assistant and ESPHome configurations were syntax-parsed only. Arduino sketches were not compiled, flashed or tested with real tags. No GPIO output, pump, battery pack, mains appliance or printed part was operated. Mesh closure does not qualify an enclosure for electrical, food-contact, waterproof or structural service.

The GitLab pipeline is a template. No GitLab job, repository push, native secret-detection configuration or visibility change was performed.

## Reproduce the offline checks

```bash
python -m unittest discover -s tests -v
python tools/run_demo.py
python tools/privacy_scan.py
python tools/check_repository.py
python tools/check_shell.py
python tools/check_node.py
```

The first four commands require only Python. Shell checking additionally needs Bash; the HTTP check additionally needs Node. Optional mesh inspection and YAML parsing were release-preparation checks, not dependencies of the offline Python suite. The mesh sources can be rendered with OpenSCAD and inspected in a suitable viewer.

See the [machine-readable results](validation-results.json) and [source references](SOURCES.md). This record applies to the supplied edition; update it after modifications rather than retaining old passing counts.
