#!/usr/bin/env python3
"""Create a reviewed copy from an explicit host map; never edits installed agents."""
import argparse
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from labkit.common import load_json
from labkit.endpoints import propose_replacements

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input',type=Path);p.add_argument('mapping',type=Path)
    p.add_argument('output',type=Path);p.add_argument('--write-copy',action='store_true')
    a=p.parse_args()
    if a.input.resolve()==a.output.resolve():
        p.error('Input and output must differ')
    try:
        revised,changes=propose_replacements(a.input.read_text(encoding='utf-8'),load_json(a.mapping))
        print(f'Proposed host replacements: {len(changes)}. No URL paths, queries or secrets printed.')
        if a.write_copy:
            if a.output.exists():
                p.error('Output already exists; review/remove it explicitly')
            a.output.parent.mkdir(parents=True,exist_ok=True)
            fd=os.open(a.output,os.O_WRONLY | os.O_CREAT | os.O_EXCL,0o600)
            with os.fdopen(fd,'w',encoding='utf-8') as f:
                f.write(revised)
        return 0
    except (ValueError, OSError):
        print('Input validation failed. Review the mapping and local file.',file=sys.stderr)
        return 2
if __name__=='__main__':
    raise SystemExit(main())
