#!/usr/bin/env bash
set -euo pipefail
umask 077
[[ $# -eq 2 ]] || { echo 'Usage: save-image.sh APPROVED_LOCAL_IMAGE OUTPUT.tar.gz' >&2; exit 2; }
image=$1
output=$2
[[ ! -e "$output" && ! -e "$output.sha256" ]] || { echo 'Output exists; refuse overwrite.' >&2; exit 2; }
command -v docker >/dev/null || { echo 'Docker is required.' >&2; exit 2; }
docker image inspect -- "$image" >/dev/null
work=$(mktemp -d)
trap 'rm -rf -- "$work"' EXIT
docker save -- "$image" | gzip -n > "$work/image.tar.gz"
mv -- "$work/image.tar.gz" "$output"
(cd "$(dirname "$output")" && sha256sum -- "$(basename "$output")" > "$(basename "$output").sha256")
echo 'Export complete. Audit image layers, scan dependencies, and review metadata before transfer.'
