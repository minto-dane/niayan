#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
"""Check current project licensing and canonical sibling notices; no relicensing."""
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REPOS = ('.', 'assurance', 'pkgcore', 'statecore', 'controlcore', 'configcore',
         'resolvercore', 'capsulecore', 'distribution')
PRESERVED = {'evidence', 'history', 'history-evidence', 'fixtures'}
NOTICES = ('LICENSE', 'LICENSING.md', 'LICENSES/MIT-legacy.txt')


def inspect(root=ROOT):
    failures = []
    checked = 0
    preserved = 0
    expected = (root / 'LICENSE').read_bytes()
    legacy = (root / 'LICENSES/MIT-legacy.txt').read_bytes()
    if not legacy.startswith(b'MIT License\n'):
        failures.append('preserve the prior MIT permission notice')
    if not expected.startswith(b'BSD 3-Clause License\n'):
        failures.append('workspace LICENSE must be BSD-3-Clause')
    for repo in REPOS:
        base = root / repo
        for name in NOTICES:
            path = base / name
            if path.is_symlink() or not path.is_file():
                failures.append(f'{repo}/{name}: missing ordinary notice')
        if (base / 'LICENSES/MIT-legacy.txt').read_bytes() != legacy:
            failures.append(f'{repo}: prior permission notice differs')
        if (base / 'LICENSE').read_bytes() != expected:
            failures.append(f'{repo}: project license differs')
        paths = subprocess.check_output(['git', '-C', str(base), 'ls-files',
            '--cached', '--others', '--exclude-standard', '-z']).decode().split('\0')
        for name in sorted(set(paths) - {''}):
            parts = Path(name).parts
            if any(part in PRESERVED for part in parts):
                preserved += 1
                continue
            path = base / name
            if path.is_dir():  # Pinned component gitlinks in the workspace.
                continue
            if path.is_symlink() or not path.is_file() or path.stat().st_size > 8 * 1024 * 1024:
                failures.append(f'{repo}/{name}: review non-regular or oversized current input')
                continue
            if parts[0] == 'vendor':
                accepted = {'contracts'} if repo not in ('.', 'assurance', 'distribution') else set()
                if repo == 'pkgcore':
                    accepted.add('resolver')
                if len(parts) < 3 or parts[1] not in accepted:
                    failures.append(f'{repo}/{name}: unclassified imported material')
                    continue
            raw = path.read_bytes()
            if len(parts) == 1 and path.name.startswith('README') and re.search(rb'\bMIT[- ]licensed\b', raw, re.I):
                failures.append(f'{repo}/{name}: current introductory license differs')
            identifiers = re.findall(rb'SPDX-License-Identifier:\s*([A-Za-z0-9.+-]+)', raw)
            if any(value != b'BSD-3-Clause' for value in identifiers):
                failures.append(f'{repo}/{name}: current source identifier differs')
            checked += 1
        if repo not in ('.', 'assurance', 'distribution'):
            sources = [('contracts', 'assurance')]
            if repo == 'pkgcore':
                sources.append(('resolver', 'resolvercore'))
            for vendor, source in sources:
                for name in NOTICES:
                    path = base / 'vendor' / vendor / name
                    if not path.is_file() or path.is_symlink() or path.read_bytes() != (root / source / name).read_bytes():
                        failures.append(f'{repo}/vendor/{vendor}/{name}: regenerate canonical notices')
    copyright_path = root / 'distribution/packaging/root-preparation/debian/copyright'
    text = copyright_path.read_text()
    if '\nLicense: BSD-3-Clause\n' not in text or '\nLicense: MIT\n' in text:
        failures.append('root-preparation package license differs')
    return {'format': 1, 'result': 'fail' if failures else 'pass', 'current_files_checked': checked,
            'historical_or_fixture_files_preserved': preserved, 'failures': failures,
            'scope': 'project-authored current tree and canonical sibling notices',
            'external_package_relicensing': False, 'publication_approval': False}


if __name__ == '__main__':
    result = inspect()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(result['result'] != 'pass')
