#!/usr/bin/env python3
"""Offline structure, Python syntax, JSON, and relative Markdown link checks."""
from __future__ import annotations
import ast,json,re,sys
from pathlib import Path
from urllib.parse import unquote,urlsplit
from repository_files import candidates
ROOT=Path(__file__).resolve().parents[1]
LINK=re.compile(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+"[^"]*")?\)')
def anchor(text):
    # Plain ASCII GitLab-style headings used by this repository.
    return re.sub(r'[^\w\- ]','',text.strip().casefold()).replace(' ','-')
def main():
    errors=[];counts={'files':0,'python':0,'json':0,'markdownLinks':0}
    try: paths=list(candidates(ROOT))
    except ValueError as error: print(error);return 1
    for p in paths:
        counts['files']+=1
        try:
            text=p.read_text(encoding='utf-8')
            if p.suffix=='.py': ast.parse(text,filename=p.relative_to(ROOT).as_posix());counts['python']+=1
            if p.suffix=='.json': json.loads(text);counts['json']+=1
            if p.suffix=='.md':
                for target in LINK.findall(text):
                    parsed=urlsplit(target)
                    if parsed.scheme or target.startswith('//'):continue
                    counts['markdownLinks']+=1
                    dest=(p.parent/unquote(parsed.path)).resolve() if parsed.path else p
                    if not dest.is_relative_to(ROOT) or not dest.exists():
                        errors.append(f'{p.relative_to(ROOT)}: missing/outside link: {target}');continue
                    if parsed.fragment and dest.suffix=='.md':
                        headings={anchor(h) for h in re.findall(r'^#{1,6} (.+)$',dest.read_text(),re.M)}
                        if unquote(parsed.fragment) not in headings:
                            errors.append(f'{p.relative_to(ROOT)}: missing heading: {target}')
        except (OSError,ValueError,SyntaxError,UnicodeDecodeError) as error:
            errors.append(f'{p.relative_to(ROOT)}: {type(error).__name__}')
    try:
        catalog=json.loads((ROOT/'project-catalog.json').read_text())
        entries=catalog if isinstance(catalog,list) else catalog['projects']
        seen=set()
        for entry in entries:
            slug=entry.get('folder',entry.get('id',entry.get('slug')))
            if slug in seen: errors.append('Duplicate catalog project')
            seen.add(slug)
        if len(entries)!=len(list((ROOT/'projects').glob('*/project.json'))): errors.append('Catalog/project count mismatch')
    except (OSError,ValueError,KeyError): errors.append('Invalid project catalog')
    print(json.dumps({'checks':counts,'errors':errors},indent=2))
    return 1 if errors else 0
if __name__=='__main__':sys.exit(main())
