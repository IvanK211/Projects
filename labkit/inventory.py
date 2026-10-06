"""Exact hostname matching, deterministic duplicates, and snapshot comparison."""
from __future__ import annotations
from collections import defaultdict
from datetime import datetime, timezone
from .common import normalized, timestamp

def reconcile(requested: list[str], devices: list[dict]) -> list[dict]:
    buckets: dict[str, list[dict]] = defaultdict(list)
    ids: set[str] = set()
    for record in devices:
        identity = str(record.get("id", "")).strip()
        name = normalized(record.get("deviceName"))
        if not identity or not name:
            raise ValueError("Every inventory record needs id and deviceName")
        if identity in ids:
            raise ValueError("Repeated device ID: normalize paginated data first")
        ids.add(identity)
        timestamp(record.get("lastSyncDateTime"))  # Validate even unmatched records.
        buckets[name].append(record)
    epoch = datetime.min.replace(tzinfo=timezone.utc)
    result = []
    # Preserve requested display spelling, collapse only exact normalized duplicates.
    unique = {normalized(name): str(name).strip() for name in requested if normalized(name)}
    for key, display in unique.items():
        matches = sorted(buckets.get(key, []), key=lambda row: (
            timestamp(row.get("lastSyncDateTime")) or epoch, str(row["id"])))
        newest = matches[-1] if matches else None
        result.append({
            "requestedName": display,
            "status": "NotFound" if not matches else "Duplicate" if len(matches) > 1 else "Found",
            "matchCount": len(matches),
            "newest": newest,
            "oldest": matches[0] if matches else None,
            "selectionRule": "lastSyncDateTime then id; null timestamps sort first",
        })
    return result

def compare(before: list[dict], after: list[dict], key: str = "id") -> dict:
    def index(rows):
        output = {}
        for row in rows:
            value = normalized(row.get(key))
            if not value or value in output:
                raise ValueError(f"Missing or duplicate comparison key: {key}")
            output[value] = row
        return output
    old, new = index(before), index(after)
    return {
        "key": key,
        "added": [new[k] for k in sorted(new.keys() - old.keys())],
        "removed": [old[k] for k in sorted(old.keys() - new.keys())],
        "changed": [{"key": k, "before": old[k], "after": new[k]}
                    for k in sorted(old.keys() & new.keys()) if old[k] != new[k]],
        "unchangedCount": sum(old[k] == new[k] for k in old.keys() & new.keys()),
        "interpretation": "Snapshot differences are not proof of employee departures or device disposal.",
    }
