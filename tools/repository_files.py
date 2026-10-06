"""Explicit release boundaries. Never follow symlinks or publish local output."""
from pathlib import Path
SKIP_DIRS = {'.git', '.venv', 'venv', '__pycache__', '.pytest_cache', '.mypy_cache',
             'node_modules', 'local-output', 'local-data', 'private', 'dist', '.cache'}
SKIP_NAMES = {'MANIFEST.sha256'}
ALLOWED_EXACT = {'.gitignore', '.gitattributes', '.editorconfig', '.gitlab-ci.yml',
                 'Makefile', 'LICENSE', '.env.example'}
ALLOWED_SUFFIXES = {'.md','.py','.json','.yaml','.yml','.ps1','.psm1','.kql','.sh',
                    '.mjs','.html','.scad','.stl','.ino','.conf','.example','.txt','.toml'}
def candidates(root: Path, include_manifest: bool = False):
    root = root.resolve()
    for p in sorted(root.rglob('*')):
        rel = p.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if p.is_symlink():
            raise ValueError(f'Symlink is not publishable: {rel}')
        if not p.is_file():
            continue
        if p.name in SKIP_NAMES and not include_manifest:
            continue
        if p.name == 'MANIFEST.sha256' and include_manifest:
            yield p; continue
        if p.name not in ALLOWED_EXACT and p.suffix not in ALLOWED_SUFFIXES:
            raise ValueError(f'Unreviewed file type: {rel}')
        yield p
