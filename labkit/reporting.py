"""Offline HTML reports. Escapes all supplied strings; no remote fonts or scripts."""
from __future__ import annotations
from html import escape
from pathlib import Path
import json
from .common import load_json

def html_report(data: object, title: str = "Synthetic reference report") -> str:
    payload = escape(json.dumps(data, indent=2, ensure_ascii=True, allow_nan=False))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>{escape(title)}</title>
<style>body{{font:16px/1.6 system-ui,sans-serif;max-width:1100px;margin:3rem auto;padding:0 1.5rem}}
pre{{white-space:pre-wrap;overflow-wrap:anywhere;border:1px solid;padding:1.3rem}}
small{{display:block;margin:1rem 0}}h1{{line-height:1.2}}</style></head>
<body><h1>{escape(title)}</h1><small>Reference output. Validate scope, timestamps, denominators and privacy before distribution.</small>
<pre>{payload}</pre></body></html>
'''

def kpi_summary(rows: list[dict]) -> dict:
    result = []
    for row in rows:
        kind = row["kind"]
        values = row.get("values", [])
        if any(isinstance(v, bool) or not isinstance(v, (int, float)) for v in values):
            raise ValueError("Use numeric observations; missing is not zero")
        import math
        if any(not math.isfinite(v) for v in values):
            raise ValueError("Non-finite KPI value")
        if kind not in ("sum", "mean", "last"):
            raise ValueError("KPI kind must explicitly be sum, mean, or last")
        value = None if not values else sum(values) if kind == "sum" else sum(values)/len(values) if kind == "mean" else values[-1]
        result.append({"name": row["name"], "kind": kind, "value": value,
                       "sampleCount": len(values), "unit": row.get("unit", "count")})
    return {"metrics": result, "note": "Do not average rates without an appropriate denominator; use the phishing tool for exposure-weighted rates."}
