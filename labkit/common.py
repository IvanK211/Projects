"""Small, explicit I/O helpers; no network access or credential discovery."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import json
import math
import os
import tempfile

def load_json(path: str | Path) -> Any:
    p = Path(path)
    if p.stat().st_size > 20 * 1024 * 1024:
        raise ValueError("Input exceeds the 20 MiB safety limit; split it explicitly")
    with p.open(encoding="utf-8-sig") as stream:
        return json.load(stream)

def write_json(path: str | Path, data: Any) -> None:
    """Atomic replacement; private file permissions on POSIX."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=".pending-", dir=p.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(data, stream, indent=2, ensure_ascii=True, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, p)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)

def timestamp(value: str | None) -> datetime | None:
    if value in (None, ""):
        return None
    result = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("Timestamp needs an explicit UTC offset")
    return result.astimezone(timezone.utc)

def normalized(value: object) -> str:
    return str(value or "").strip().casefold()

def number(value: Any, name: str, minimum: float = 0) -> float:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be numeric, not boolean")
    result = float(value)
    if not math.isfinite(result) or result < minimum:
        raise ValueError(f"{name} must be finite and >= {minimum}")
    return result

def count(value: Any, name: str) -> int:
    result = number(value, name)
    if int(result) != result:
        raise ValueError(f"{name} must be an integer")
    return int(result)

def ratio(numerator: float, denominator: float) -> float | None:
    return None if denominator == 0 else round(numerator / denominator, 6)


def write_text_private(path: str | Path, content: str) -> None:
    """Atomic UTF-8 text output; private mode on POSIX from file creation."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=".pending-", dir=p.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, p)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)
