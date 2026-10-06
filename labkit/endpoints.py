"""Explicit, offline URL-host replacements; never edits the original input."""
from __future__ import annotations
import re
from urllib.parse import urlsplit, urlunsplit

URL = re.compile(r"https?://[^\s\"'<>]+")

def propose_replacements(text: str, hosts: dict[str, str]) -> tuple[str, list[dict]]:
    for old, new in hosts.items():
        if not old or not new or any(c in old + new for c in "/@: "):
            raise ValueError("Replacement map must contain plain hostnames only")
    changes = []
    def replace(match):
        original = match.group(0)
        uri = urlsplit(original)
        if uri.username or uri.password:
            raise ValueError("Embedded credentials found; remove them before processing")
        host = (uri.hostname or "").casefold()
        if host not in hosts:
            return original
        new_host = hosts[host]
        netloc = new_host + (f":{uri.port}" if uri.port is not None else "")
        replacement = urlunsplit((uri.scheme, netloc, uri.path, uri.query, uri.fragment))
        changes.append({"oldHost": host, "newHost": new_host})
        return replacement
    return URL.sub(replace, text), changes
