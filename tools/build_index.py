#!/usr/bin/env python3
"""Generate a portable index of release-candidate files; no local absolute paths."""
import sys
from pathlib import Path
from repository_files import candidates
ROOT=Path(__file__).resolve().parents[1]
def main():
    lines=['# File index','','Generated from the explicit release boundary. Local outputs, credentials, caches and Git history are excluded.','',
           '| File | Bytes |','|---|---:|']
    for p in candidates(ROOT):
        rel=p.relative_to(ROOT).as_posix()
        if rel in {'FILE_INDEX.md','MANIFEST.sha256'}:continue
        lines.append(f'| [{rel}]({rel}) | {p.stat().st_size} |')
    (ROOT/'FILE_INDEX.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('FILE_INDEX.md generated.')
    return 0
if __name__=='__main__':sys.exit(main())
