#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
"""Read back the transient scope's kernel limits before starting validation."""
import json
import os
from pathlib import Path
import subprocess
import sys


def check_limits(directory: Path) -> dict[str, str]:
    values = {name: (directory / name).read_text().strip()
              for name in ('memory.max', 'memory.swap.max', 'cpu.max', 'pids.max')}
    memory = int(values['memory.max'])
    swap = int(values['memory.swap.max'])
    quota, period = map(int, values['cpu.max'].split())
    tasks = int(values['pids.max'])
    if not (0 < memory <= 3 * 1024**3 and swap == 0 and 0 < quota <= period
            and 0 < tasks <= 128):
        raise ValueError('kernel limits are weaker than the development budget')
    return values


def main() -> int:
    if len(sys.argv) < 2:
        raise ValueError('missing validation command')
    path = next(line[3:] for line in Path('/proc/self/cgroup').read_text().splitlines()
                if line.startswith('0::'))
    unit = Path(path).name
    if not unit.endswith('.scope'):
        raise ValueError('validation must start in a transient systemd scope')
    group = subprocess.check_output(['systemctl', '--user', 'show', unit,
                                    '--property=ControlGroup', '--value'], text=True, timeout=5).strip()
    if not group.startswith('/') or '..' in Path(group).parts:
        raise ValueError('invalid scope control group')
    # Distrobox exposes the host hierarchy separately; ordinary hosts use /sys.
    directory = next((root / group.lstrip('/') for root in
                      (Path('/run/host/sys/fs/cgroup'), Path('/sys/fs/cgroup'))
                      if (root / group.lstrip('/') / 'memory.max').is_file()), None)
    if directory is None:
        raise ValueError('cannot read the scope kernel controls')
    values = check_limits(directory)
    print('limited-exec: ' + json.dumps(dict(scope=unit, kernel_limits=values)), flush=True)
    os.execvp(sys.argv[1], sys.argv[1:])
    return 127


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, StopIteration, subprocess.SubprocessError) as exc:
        raise SystemExit('limited-exec: refused to start: ' + str(exc))
