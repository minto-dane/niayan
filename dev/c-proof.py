#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
"""Run the pinned, explicitly scoped C proof; never certify the whole C boundary."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CBMC_SHA256 = '346f5ff6ef13aa49c187977edfc9ac86754ded0d12e9fc9fd6e3e4d8ef49e498'
INPUTS = ('pkgcore/runtime/root_handoff_wire.c', 'pkgcore/runtime/root_handoff_wire.h',
          'pkgcore/tests/proof/root_handoff_wire.c', 'dev/c-proof.py', 'dev/limited-exec.py')


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def limits() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location('limited', ROOT / 'dev/limited-exec.py')
    if spec is None or spec.loader is None:
        raise ValueError('missing resource guard')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # A container's cgroup namespace exposes its enforced budget at the root;
    # it need not have a user systemd bus even if its host group is a scope.
    try:
        return module.check_limits(Path('/sys/fs/cgroup'))
    except (OSError, ValueError):
        pass
    group = next(line[3:] for line in Path('/proc/self/cgroup').read_text().splitlines() if line.startswith('0::'))
    candidates: list[Path] = []
    if Path(group).name.endswith('.scope'):
        actual = subprocess.check_output(['systemctl', '--user', 'show', Path(group).name,
            '--property=ControlGroup', '--value'], text=True, timeout=5).strip()
        if not actual.startswith('/') or '..' in Path(actual).parts:
            raise ValueError('invalid cgroup path')
        candidates = [root / actual.lstrip('/') for root in
                      (Path('/run/host/sys/fs/cgroup'), Path('/sys/fs/cgroup'))]
    for path in candidates:
        try:
            return module.check_limits(path)
        except (OSError, ValueError):
            continue
    raise ValueError('run in dev/run-limited.sh or a container with the required kernel limits')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cbmc', default='cbmc')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    budget = limits()
    executable = shutil.which(args.cbmc)
    if executable is None or digest(Path(executable)) != CBMC_SHA256:
        raise ValueError('requires the pinned Debian amd64 cbmc 6.6.0-4 executable')
    version = subprocess.check_output([executable, '--version'], text=True, timeout=5).strip()
    if version != '6.6.0 (cbmc-6.6.0)':
        raise ValueError('unexpected CBMC version')
    args.output.mkdir(parents=True, exist_ok=False)
    before = {name: digest(ROOT / name) for name in INPUTS}
    command = [executable, INPUTS[0], INPUTS[2], '--function', 'proof_handoff_wire', '--64', '--c11',
        '--unwind', '177', '--unwinding-assertions', '--bounds-check', '--pointer-check',
        '--pointer-overflow-check', '--signed-overflow-check', '--unsigned-overflow-check',
        '--conversion-check', '--div-by-zero-check', '--undefined-shift-check', '--memory-leak-check', '--json-ui']
    result: dict[str, Any] = dict(result='fail', scope='canonical handoff wire validator and its reachable helpers only',
        inputs=before, cbmc_version=version, cbmc_sha256=CBMC_SHA256, command=command,
        kernel_limits=budget, environment_assumptions=['amd64 C11 ABI', 'input pointer is NULL or an initialized readable object of 192 bytes (preparation) or 224 bytes (reinspection)'],
        input_restrictions=[], os_or_library_models=[], complete_transport_proof=False,
        coding_standard_compliance=False, production_qualified=False)
    try:
        result['gcc_version'] = subprocess.check_output(['gcc', '--version'], text=True, timeout=5).splitlines()[0]
        static_command = ['gcc', '-std=c11', '-Wall', '-Wextra', '-Wpedantic', '-Werror',
            '-Wconversion', '-Wsign-conversion', '-Wshadow', '-Wstrict-prototypes',
            '-Wmissing-prototypes', '-Wvla', '-Wcast-align=strict', '-Wformat=2', '-Wundef',
            '-Wwrite-strings', '-fanalyzer', '-c', INPUTS[0],
            '-o', str(args.output.resolve() / 'wire-analysis.o')]
        result['static_command'] = static_command
        with (args.output / 'static.log').open('w') as log:
            subprocess.run(static_command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True, timeout=30)
        if (args.output / 'static.log').read_bytes():
            raise ValueError('unexpected static-analysis output')
        with (args.output / 'cbmc.json').open('w') as out, (args.output / 'stderr.log').open('w') as err:
            with subprocess.Popen(command, cwd=ROOT, stdout=out, stderr=err, start_new_session=True) as run:
                try:
                    run.wait(timeout=120)
                except BaseException:
                    # The child is still ours and unreaped; terminate its whole
                    # proof/preprocessor group before reporting an incomplete run.
                    try:
                        os.killpg(run.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    run.wait()
                    raise
        data = json.loads((args.output / 'cbmc.json').read_text())
        properties = [item for entry in data for item in entry.get('result', [])]
        ids = [item.get('property') for item in properties]
        if (run.returncode != 0 or not properties or len(ids) != len(set(ids))
                or any(item.get('status') != 'SUCCESS' for item in properties)
                or not {'proof_handoff_wire.assertion.1', 'proof_handoff_wire.assertion.2',
                        'proof_reinspection_wire.assertion.1', 'proof_reinspection_wire.assertion.2'} <= set(ids)
                or [entry['cProverStatus'] for entry in data if 'cProverStatus' in entry] != ['success']
                or any(entry.get('messageType') in ('WARNING', 'ERROR') for entry in data)
                or (args.output / 'stderr.log').read_bytes()):
            raise ValueError('incomplete, failed or warning-bearing proof result')
        if before != {name: digest(ROOT / name) for name in INPUTS}:
            raise ValueError('proof inputs changed during verification')
        result.update(result='pass', properties=len(properties), cbmc_result_sha256=digest(args.output / 'cbmc.json'))
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        result['error'] = str(error)
    (args.output / 'report.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in ('result', 'scope', 'production_qualified')}))
    return 0 if result['result'] == 'pass' else 1


if __name__ == '__main__':
    raise SystemExit(main())
