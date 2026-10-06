"""Offline PAM change planning. No credentials or live mutation in this module."""
from __future__ import annotations
from copy import deepcopy
from collections import defaultdict
from .common import count, normalized, timestamp

def normalize_suffix(value: str) -> str:
    suffix = str(value).strip().lstrip(".").rstrip(".").casefold()
    if not suffix or "." not in suffix or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789.-" for c in suffix):
        raise ValueError("Use an explicit DNS suffix with at least two labels; no wildcards")
    if any(not label or label.startswith("-") or label.endswith("-") for label in suffix.split(".")):
        raise ValueError("Malformed DNS suffix")
    return suffix

def port_plan(accounts: list[dict], suffix: str, new_port: int, safe: str | None = None) -> dict:
    target = normalize_suffix(suffix)
    port = count(new_port, "port")
    if not 1 <= port <= 65535:
        raise ValueError("Port must be within 1..65535")
    rows = []
    seen = set()
    for account in accounts:
        identity = str(account.get("id", "")).strip()
        if not identity or identity in seen:
            raise ValueError("Missing/duplicate account ID")
        seen.add(identity)
        address = normalized(account.get("address")).rstrip(".")
        # Label boundary prevents matching notexample.invalid for example.invalid.
        if not (address == target or address.endswith("." + target)):
            continue
        if safe is not None and normalized(account.get("safeName")) != normalized(safe):
            continue
        props = deepcopy(account.get("platformAccountProperties") or {})
        keys = [k for k in props if normalized(k) == "port"]
        if len(keys) > 1:
            raise ValueError("Ambiguous port property casing")
        key = keys[0] if keys else "Port"
        previous = props.get(key)
        props[key] = str(port)
        rows.append({"accountId": identity, "address": account.get("address"),
                     "safeName": account.get("safeName"), "platformId": account.get("platformId"),
                     "beforeProperties": account.get("platformAccountProperties") or {},
                     "afterProperties": props, "oldPort": previous, "newPort": str(port),
                     "action": "unchanged" if str(previous) == str(port) else "review",
                     "patch": [{"op": "add", "path": "/platformaccountproperties", "value": props}]})
    return {"mode": "plan-only", "suffix": target, "newPort": port,
            "warning": "Review platform-specific property names and re-fetch before any mutation.", "accounts": rows}

def session_summary(rows: list[dict]) -> list[dict]:
    groups = defaultdict(lambda: {"sessions": 0, "knownDurationSeconds": 0, "unknownDuration": 0})
    seen = set()
    for row in rows:
        identity = str(row["id"])
        if identity in seen:
            raise ValueError("Duplicate recording ID")
        seen.add(identity)
        # initiatingUser is the person who launched the session, not targetUser.
        g = groups[str(row.get("initiatingUser") or "Unresolved")]
        g["sessions"] += 1
        start, end = timestamp(row.get("start")), timestamp(row.get("end"))
        if start is None or end is None:
            g["unknownDuration"] += 1
        elif end < start:
            raise ValueError("Session end precedes start")
        else:
            g["knownDurationSeconds"] += int((end - start).total_seconds())
    return [{"initiatingUser": k, **v} for k, v in sorted(groups.items())]
