#!/usr/bin/env python3
"""Parse Bash sources; never execute infrastructure scripts."""
import shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    bash=shutil.which('bash')
    if not bash:raise SystemExit('Bash is required for shell syntax validation.')
    paths=sorted((ROOT/'projects').rglob('*.sh'))
    for path in paths:subprocess.run([bash,'-n',str(path)],check=True)
    print(f'{len(paths)} Bash files passed syntax checking; no host/service changes executed.')
if __name__=='__main__':main()
