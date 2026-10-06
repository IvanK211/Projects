#!/usr/bin/env bash
# Tests integrity and decryptability without extracting an archive onto a live system.
set -euo pipefail
[[ $# -eq 2 ]] || { echo 'Usage: verify-backup.sh ARCHIVE.tar.age IDENTITY_FILE' >&2; exit 2; }
archive=$(realpath -e -- "$1")
identity=$(realpath -e -- "$2")
[[ -f "$archive.sha256" ]] || { echo 'Checksum file missing.' >&2; exit 2; }
(cd "$(dirname "$archive")" && sha256sum -c -- "$(basename "$archive").sha256")
age -d -i "$identity" "$archive" | tar -tf - >/dev/null
echo 'Checksum and archive listing passed. Application-level recovery still needs an isolated test.'
