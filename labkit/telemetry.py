"""Offline observations, explicit staleness and robust event-rate arithmetic."""
from __future__ import annotations
from collections import Counter, defaultdict
from datetime import timedelta
import ipaddress
import math
import statistics
from .common import number, timestamp

def counter_rate(previous: dict | None, current: dict) -> float | None:
    current_count = number(current["count"], "count")
    current_time = timestamp(current["time"])
    if current_time is None:
        raise ValueError("Current time is required")
    if previous is None:
        return None
    previous_time = timestamp(previous["time"])
    previous_count = number(previous["count"], "count")
    if previous_time is None:
        raise ValueError("Previous time is required")
    elapsed = (current_time - previous_time).total_seconds()
    # A counter reset or changed index is unknown, never a negative EPS.
    if elapsed <= 0 or current_count < previous_count or previous.get("source") != current.get("source"):
        return None
    return round((current_count - previous_count) / elapsed, 6)

def sensor_summary(rows: list[dict]) -> dict:
    grouped = defaultdict(list)
    for row in rows:
        at = timestamp(row["time"])
        if at is None:
            raise ValueError("Measurement time is required")
        value = float(row["value"])
        if not math.isfinite(value):
            raise ValueError("Non-finite measurement")
        grouped[(str(row["sensor"]), str(row["unit"]))].append((at, value))
    result = []
    for (sensor, unit), samples in sorted(grouped.items()):
        samples.sort()
        values = [v for _, v in samples]
        hours = (samples[-1][0] - samples[0][0]).total_seconds() / 3600
        result.append({"sensor": sensor, "unit": unit, "samples": len(values),
                       "minimum": min(values), "maximum": max(values), "median": statistics.median(values),
                       "endpointDriftPerHour": None if hours == 0 else round((values[-1]-values[0])/hours, 6),
                       "note": "Descriptive drift is not proof of calibration error or a chemical mechanism."})
    return {"series": result}

def log_summary(rows: list[dict]) -> dict:
    # Deliberately exclude raw messages, hostnames, user IDs and source addresses.
    levels = Counter(str(r.get("level", "unknown")).casefold() for r in rows)
    events = Counter(str(r.get("eventType", "unknown")) for r in rows)
    return {"total": len(rows), "levels": dict(sorted(levels.items())),
            "eventTypes": dict(sorted(events.items())),
            "privacy": "Aggregated fields still require review for custom/private labels."}

def correlate_ip(rows: list[dict], address: str, as_of: str, max_age_hours: float) -> dict:
    target = ipaddress.ip_address(address)
    now = timestamp(as_of)
    if now is None:
        raise ValueError("as_of is required")
    max_age = timedelta(hours=number(max_age_hours, "maxAgeHours"))
    matches = []
    for row in rows:
        if ipaddress.ip_address(row["ip"]) != target:
            continue
        seen = timestamp(row["time"])
        if seen is None:
            raise ValueError("Observation time is required")
        age = now - seen
        matches.append({**row, "futureDated": age.total_seconds() < 0,
                        "stale": age > max_age, "ageSeconds": int(age.total_seconds())})
    return {"address": str(target), "observations": matches,
            "warning": "An IP can identify multiple devices over time; NAT and DHCP prevent identity certainty."}
