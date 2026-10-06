"""Explicit denominators for training and phishing simulation reports."""
from __future__ import annotations
from collections import defaultdict
from .common import count, normalized, ratio, timestamp

def training_audit(data: dict) -> dict:
    users = data["users"]
    required = [normalized(v) for v in data["requiredTrainingIds"]]
    if len(set(required)) != len(required) or not all(required):
        raise ValueError("Required training IDs must be nonempty and unique")
    uid = [str(u["id"]) for u in users]
    if len(set(uid)) != len(uid):
        raise ValueError("Duplicate user IDs")
    enrollments = defaultdict(list)
    for row in data["enrollments"]:
        enrollments[(str(row["userId"]), normalized(row["trainingId"]))].append(row)
    groups = {}
    details = []
    for user in users:
        if not user.get("active", True):
            continue
        division = str(user.get("division") or "Unassigned")
        g = groups.setdefault(division, {"users": 0, "expected": 0, "completed": 0,
                                         "incomplete": 0, "notAssigned": 0})
        g["users"] += 1
        for requirement in required:
            matches = enrollments.get((str(user["id"]), requirement), [])
            # A completion satisfies this explicitly bounded requirement set.
            completed = any(normalized(e.get("status")) in {"completed", "passed"} for e in matches)
            status = "completed" if completed else "incomplete" if matches else "notAssigned"
            g["expected"] += 1
            g[status] += 1
            details.append({"userId": user["id"], "division": division,
                            "trainingId": requirement, "status": status})
    for g in groups.values():
        g["missed"] = g["incomplete"] + g["notAssigned"]
        g["completionRate"] = ratio(g["completed"], g["expected"])
    return {"groups": groups, "details": details,
            "policy": "Completion in any supplied enrollment satisfies a required ID. Filter reporting period upstream."}

def phishing_summary(rows: list[dict]) -> list[dict]:
    groups = defaultdict(lambda: {"campaigns": 0, "delivered": 0, "failed": 0,
                                  "reported": 0, "rates": []})
    seen = set()
    for row in rows:
        unique = (str(row["campaignId"]), str(row["division"]))
        if unique in seen:
            raise ValueError("Duplicate campaign/division row; aggregate once before input")
        seen.add(unique)
        delivered = count(row["delivered"], "delivered")
        failed = count(row["failed"], "failed")
        reported = count(row.get("reported", 0), "reported")
        if failed > delivered or reported > delivered:
            raise ValueError("Failed/reported unique recipient counts cannot exceed delivered")
        g = groups[unique[1]]
        g["campaigns"] += 1
        g["delivered"] += delivered
        g["failed"] += failed
        g["reported"] += reported
        if delivered:
            g["rates"].append(failed / delivered)
    output = []
    for division, g in sorted(groups.items()):
        rates = g.pop("rates")
        output.append({"division": division, **g,
                       "recipientExposureWeightedFailureRate": ratio(g["failed"], g["delivered"]),
                       "campaignMeanFailureRate": ratio(sum(rates), len(rates)),
                       "reportRate": ratio(g["reported"], g["delivered"]),
                       "note": "Repeated recipients across campaigns count as repeated exposures, not unique people."})
    return output

def pim_activations(rows: list[dict], since: str) -> list[dict]:
    cutoff = timestamp(since)
    if cutoff is None:
        raise ValueError("A nonempty start timestamp is required")
    result = []
    for row in rows:
        created = timestamp(row.get("createdDateTime"))
        if normalized(row.get("action")) != "selfactivate" or created is None or created < cutoff:
            continue
        # Preserve status; a request is not proof of a completed privileged action.
        result.append({key: row.get(key) for key in (
            "id", "principalId", "roleDefinitionId", "action", "status", "createdDateTime",
            "completedDateTime", "justification", "scheduleInfo", "ticketInfo", "directoryScopeId")})
    return sorted(result, key=lambda r: (timestamp(r["createdDateTime"]), str(r["id"])))
