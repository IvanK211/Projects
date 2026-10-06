# Dependencies and compatibility

| Component | Requirement | Installation behavior |
|---|---|---|
| `labkit`, tests, repository tools | Python 3.11+; only standard library | No package install or network needed |
| Snapshot dashboard | Node.js 22-compatible built-ins | No npm packages or lockfile needed |
| Graph collectors | PowerShell 7.2+ and `Microsoft.Graph.Authentication` | Explicit operator installation; no auto-install or automatic consent |
| PAM apply template | PowerShell 7.2+ | Uses built-in REST calls and the local helper module |
| Linux references | Bash and documented local utilities; systemd where applicable | No automatic service installation |
| Encrypted backup | `tar`, `age`, `sha256sum`, normal POSIX file tools | Operator-provided recipient and quiesced source |
| Container examples | Reviewed Docker/Compose installation and approved images | Image names/digests and host paths must be set locally |
| Automation examples | Compatible Home Assistant / ESPHome deployment | YAML alone is not runtime schema or hardware validation |
| RFID sketches | Arduino-compatible toolchain, SPI and upstream MFRC522 library | Library is not vendored; choose and record a reviewed release |
| Other sketches | Compatible Arduino board/core | Pin assignments are arbitrary bench examples |
| CAD | OpenSCAD for source rendering; STL viewer for inspection | Generated meshes are generic examples, not board-specific parts |

The archive does not use `requirements.txt` to install unnecessary dependencies. No vendored libraries, proprietary plugins, font files, bundled executables or production container layers are present. A real integration project should record and pin its own reviewed toolchain and dependency versions after testing.

The CI images are convenience tags, not a statement that those tags are immutable or vulnerability-free. Pin an approved digest and set an update process locally. GitLab execution additionally requires an available runner and a permitted image source. The included pipeline has not been run in a GitLab instance.

Documentation references were checked during preparation. A public vendor documentation URL containing `latest` or `current` is not the version of any actual deployment. Verify the destination platform before relying on request fields, permission names, policy behavior or firmware syntax. The [validation record](VALIDATION.md) lists the toolchains actually exercised for this edition.
