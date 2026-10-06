#!/usr/bin/env bash
# Observe by default. A root-owned state directory is required for --apply.
set -euo pipefail
usage() { printf 'Usage: %s SERVICE [--apply STATE_DIRECTORY]\n' "$0" >&2; exit 2; }
[[ $# -eq 1 || $# -eq 3 ]] || usage
service_name=$1
[[ "$service_name" =~ ^[a-zA-Z0-9][a-zA-Z0-9_.@-]*$ ]] || usage
command -v systemctl >/dev/null || { echo 'systemd is required.' >&2; exit 2; }
if systemctl is-active --quiet "$service_name"; then echo 'Service active.'; exit 0; fi
[[ $# -eq 3 && "$2" == '--apply' ]] || { echo 'Observe-only: service is not active.'; exit 1; }
[[ $EUID -eq 0 ]] || { echo 'Apply mode requires approved root execution.' >&2; exit 2; }
state=$3
[[ -d "$state" && ! -L "$state" ]] || { echo 'Provide a pre-created protected state directory.' >&2; exit 2; }
[[ $(stat -c '%u' -- "$state") == 0 && $(stat -c '%a' -- "$state") == 700 ]] || { echo 'State directory must be root-owned mode 700.' >&2; exit 2; }
command -v flock >/dev/null || { echo 'flock is required.' >&2; exit 2; }
exec 9>"$state/watchdog.lock"
flock -n 9 || exit 0
stamp="$state/$service_name.last-attempt"
now=$(date +%s)
last=0
if [[ -f "$stamp" ]]; then read -r last < "$stamp"; fi
[[ "$last" =~ ^[0-9]+$ ]] || { echo 'Invalid state; refusing restart.' >&2; exit 2; }
(( now - last >= 900 )) || { echo 'Restart cooldown active.'; exit 1; }
# Record attempts, not successes: persistent failure must not create a restart storm.
printf '%s\n' "$now" > "$stamp"
systemctl restart -- "$service_name"
sleep 3
systemctl is-active --quiet "$service_name" || { echo 'Recovery failed; investigate privately.' >&2; exit 1; }
echo 'Service active after approved restart.'
