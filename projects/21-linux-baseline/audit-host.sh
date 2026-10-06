#!/usr/bin/env bash
# Read-only local audit. Its output may reveal infrastructure; never commit it.
set -euo pipefail
printf '=== Kernel and distribution ===\n'
uname -sr
[[ ! -r /etc/os-release ]] || grep -E '^(NAME|VERSION_ID)=' /etc/os-release
printf '\n=== Filesystems (no serial numbers) ===\n'
df -h -x tmpfs -x devtmpfs
printf '\n=== Block-device sizes (no serial numbers) ===\n'
command -v lsblk >/dev/null && lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
printf '\n=== Listening sockets (private operational data) ===\n'
command -v ss >/dev/null && ss -lntu
printf '\n=== Failed units ===\n'
if command -v systemctl >/dev/null; then systemctl --failed --no-pager; fi
printf '\n=== SSH configuration validation only ===\n'
if command -v sshd >/dev/null; then
    if [[ $EUID -eq 0 ]]; then sshd -t; else printf 'Run sshd -t separately with approved privileges.\n'; fi
fi
