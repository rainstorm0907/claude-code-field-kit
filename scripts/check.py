#!/usr/bin/env python3
"""Check that every skill reference in skills/ and agents/ points inside this kit."""
import re, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
skills = root / 'skills'
names = {p.name for p in skills.iterdir() if (p / 'SKILL.md').exists()}
errors = []

for d in sorted(names):
    head = (skills / d / 'SKILL.md').read_text().split('---')[1]
    m = re.search(r'^name:\s*"?([^"\n]+)"?', head, re.M)
    if not m or m.group(1).strip() != d:
        errors.append(f'{d}/SKILL.md: name does not match folder')
    if not re.search(r'^description:', head, re.M):
        errors.append(f'{d}/SKILL.md: missing description')

files = [f for f in skills.rglob('*.md')] + list((root / 'agents').glob('*.md'))
for f in files:
    text = f.read_text()
    rel = f.relative_to(root)
    for m in re.finditer(r'Skill\(([\w-]+)\)', text):
        if m.group(1) not in names:
            errors.append(f'{rel}: Skill({m.group(1)}) is not in this kit')
    for m in re.finditer(r'(?<![./])\.\./([\w-]+)/', text):
        if m.group(1) not in names and not (f.parent.parent / m.group(1)).is_dir():
            errors.append(f'{rel}: ../{m.group(1)}/ is not in this kit')
    if f.parts[-3:-1] and f.is_relative_to(skills):
        for m in re.finditer(r'\]\(([^)#\s]+)\)', text):
            target = m.group(1)
            if re.match(r'[a-z]+:', target):
                continue
            if not (f.parent / target).exists():
                errors.append(f'{rel}: broken link {target}')

print('\n'.join(errors) or f'ok: {len(names)} skills, {len(files)} files')
sys.exit(1 if errors else 0)
