#!/usr/bin/env python3
"""Deterministic local ZIP; never uploads, commits or includes Git history."""
import argparse,hashlib,subprocess,sys,zipfile
from pathlib import Path
from repository_files import candidates
ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output',type=Path)
    args=parser.parse_args();dest=args.output.resolve()
    if dest.is_relative_to(ROOT):raise SystemExit('Choose an archive output outside the repository.')
    for tool in ['privacy_scan.py','check_repository.py']:
        subprocess.run([sys.executable,str(ROOT/'tools'/tool)],cwd=ROOT,check=True)
    files=list(candidates(ROOT))
    manifest=''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}\n' for p in files)
    (ROOT/'MANIFEST.sha256').write_text(manifest,encoding='utf-8')
    files.append(ROOT/'MANIFEST.sha256')
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():raise SystemExit('Output exists; choose a new archive filename.')
    with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for p in sorted(files):
            rel=p.relative_to(ROOT).as_posix()
            info=zipfile.ZipInfo('tech-projects-public/'+rel,date_time=(2000,1,1,0,0,0))
            info.create_system=3
            info.external_attr=((0o100755 if p.suffix=='.sh' else 0o100644)<<16)
            archive.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    print(f'Packaged {len(files)} files; archive SHA-256: {hashlib.sha256(dest.read_bytes()).hexdigest()}')
    return 0
if __name__=='__main__':sys.exit(main())
