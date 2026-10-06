#!/usr/bin/env bash
# Back up an already quiesced local directory. Never dumps live databases implicitly.
set -euo pipefail
umask 077
[[ $# -eq 3 ]] || { echo 'Usage: backup.sh SOURCE_DIRECTORY DESTINATION_DIRECTORY AGE_RECIPIENT' >&2; exit 2; }
for cmd in age tar realpath sha256sum mktemp; do command -v "$cmd" >/dev/null || { echo "Missing dependency: $cmd" >&2; exit 2; }; done
source_dir=$(realpath -e -- "$1")
destination=$(realpath -e -- "$2")
[[ -d "$source_dir" && -d "$destination" ]] || { echo 'Source/destination must exist.' >&2; exit 2; }
[[ "$source_dir" != / && "$destination" != "$source_dir" && "$destination" != "$source_dir/"* ]] || { echo 'Unsafe destination/source relationship.' >&2; exit 2; }
recipient=$3
[[ "$recipient" == age1* || "$recipient" == ssh-ed25519* || "$recipient" == ssh-rsa* ]] || { echo 'Use an approved age recipient; do not provide a private key.' >&2; exit 2; }
work=$(mktemp -d "$destination/.backup.XXXXXX")
trap 'rm -rf -- "$work"' EXIT
# No dereference: symlinks are stored, not followed. One filesystem limits surprises.
tar --one-file-system -C "$source_dir" -cf - . | age -r "$recipient" -o "$work/archive.tar.age"
name="snapshot-$(date -u +%Y%m%dT%H%M%SZ)-$$.tar.age"
[[ ! -e "$destination/$name" ]] || { echo 'Destination collision.' >&2; exit 1; }
mv -- "$work/archive.tar.age" "$destination/$name"
(cd "$destination" && sha256sum -- "$name" > "$name.sha256")
echo 'Encrypted snapshot and checksum created. Prove recoverability with an isolated restore test.'
