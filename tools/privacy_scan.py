#!/usr/bin/env python3
"""Heuristic release scan. Does not certify anonymity or scan Git history.

Diagnostics contain only relative paths, line numbers and rule labels, never
matched secret values. The original author's personal denylist is NOT bundled.
"""
from __future__ import annotations
import argparse, ipaddress, re, sys
from pathlib import Path
from repository_files import candidates

SAFE_NETWORKS = [ipaddress.ip_network(v) for v in ('127.0.0.0/8','192.0.2.0/24',
                 '198.51.100.0/24','203.0.113.0/24')]
IP = re.compile(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])')
EMAIL = re.compile(r'\b[A-Z0-9._%+-]+@([A-Z0-9.-]+\.[A-Z]{2,})\b',re.I)
RULES = {
 'private-key-block': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'),
 'cloud-access-key': re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
 'gitlab-token': re.compile(r'\bglpat-[A-Za-z0-9_-]{16,}\b'),
 'github-token': re.compile(r'\bgh[pousr]_[A-Za-z0-9]{30,}\b'),
 'slack-token': re.compile(r'\bxox[baprs]-[A-Za-z0-9-]{20,}\b'),
 'jwt-like': re.compile(r'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\b'),
 'mac-address': re.compile(r'(?<![A-Fa-f0-9])(?:[A-Fa-f0-9]{2}:){5}[A-Fa-f0-9]{2}(?![A-Fa-f0-9])'),
 'uuid-identifier': re.compile(r'\b[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\b',re.I),
 'personal-home-path': re.compile(r'(?:/home/|/Users/|[A-Za-z]:\\Users\\)[A-Za-z0-9_.-]+'),
 'url-credentials': re.compile(r'https?://[^/\s@]+:[^/\s@]+@'),
}

def inspect_text(text: str) -> list[tuple[int,str]]:
    findings=[]
    for n,line in enumerate(text.splitlines(),1):
        for name,rule in RULES.items():
            if rule.search(line): findings.append((n,name))
        for match in IP.finditer(line):
            try: address=ipaddress.ip_address(match.group())
            except ValueError: continue
            if not any(address in net for net in SAFE_NETWORKS):
                findings.append((n,'non-documentation-ipv4'))
        for match in EMAIL.finditer(line):
            domain=match.group(1).casefold()
            if domain not in {'example.invalid','example.com','example.org','example.net'} and not domain.endswith('.example.invalid'):
                findings.append((n,'non-example-email'))
    return sorted(set(findings))

def scan(root: Path):
    findings=[]; scanned=0
    for p in candidates(root):
        rel=p.relative_to(root).as_posix();scanned+=1
        if p.name=='.env' or (p.name.startswith('secrets.') and not p.name.endswith('.example')):
            findings.append((rel,0,'local-secret-file'))
        if p.stat().st_size>5*1024*1024:
            findings.append((rel,0,'oversized-file'));continue
        try: text=p.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            findings.append((rel,0,'binary-file-not-reviewed'));continue
        if '\x00' in text: findings.append((rel,0,'embedded-nul'))
        for n,rule in inspect_text(text): findings.append((rel,n,rule))
    return scanned,findings

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args(argv);root=args.root.resolve()
    try: scanned,findings=scan(root)
    except (OSError,ValueError) as error:
        print(f'Privacy scan could not complete: {error}',file=sys.stderr);return 2
    for rel,line,rule in findings: print(f'{rel}:{line}: {rule}')
    print(f'Scanned {scanned} release-candidate files; {len(findings)} heuristic findings.')
    return 1 if findings else 0
if __name__=='__main__': sys.exit(main())
