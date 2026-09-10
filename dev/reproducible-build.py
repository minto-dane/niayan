#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
"""Compare all shipped CLI binaries from two fresh, differently named build trees."""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'assurance/ci'))
import engineering as eng


def workspace_inputs():
    paths = [ROOT/'Makefile', ROOT/'.github/workflows/ci.yml']
    paths += sorted((ROOT/'dev').glob('*'))
    return {str(p.relative_to(ROOT)): hashlib.sha256(eng.read_regular(p)).hexdigest()
            for p in paths if p.is_file()}


def tool_versions():
    return {command[0]: subprocess.check_output(command, text=True).strip()
            for command in [['gcc','--version'], ['gprbuild','--version'],
                            ['dpkg-query','-W','gnat-14','gprbuild','libc6','binutils']]}


def main():
    if os.geteuid()==0:raise SystemExit('Run as an unprivileged builder')
    eng.validate(ROOT)
    output=Path(tempfile.mkdtemp(prefix='reproducibility-',dir=ROOT/'assurance/evidence'))
    report={'format':1,'started_utc':datetime.now(timezone.utc).isoformat(),
            'source_subject':eng.source_subject(ROOT), 'source_scope':'seven components and distribution',
            'workspace_inputs':workspace_inputs(), 'tool_versions':tool_versions(),
            'production_qualified':False,'builds':[]}
    try:
        with tempfile.TemporaryDirectory(prefix='nia-repro-') as temporary:
            temporary=Path(temporary)
            results=[]
            for build_number, directory in enumerate(('first','second-with-a-different-path-length')):
                destination=temporary/directory
                shutil.copytree(ROOT,destination,ignore=shutil.ignore_patterns('.git','build','evidence','__pycache__'))
                source_mtime = 1788739200 + build_number * 86400
                for source_file in destination.rglob('*'):
                    if source_file.is_file():
                        os.utime(source_file, (source_mtime, source_mtime))
                home=temporary/(directory+'-home');home.mkdir(mode=0o700)
                env={'PATH':os.environ['PATH'],'HOME':str(home),'TMPDIR':str(home),
                     'LANG':'C.UTF-8','LC_ALL':'C.UTF-8','SOURCE_DATE_EPOCH':'1788739200',
                     'JOBS':str(build_number + 1), 'TZ':('UTC0' if build_number == 0 else 'HST10')}
                with (output/(directory+'.log')).open('w') as log:
                    run=subprocess.run(['make','build'],cwd=destination,env=env,
                        stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,timeout=1800)
                record={'tree':directory,'returncode':run.returncode,'binaries':{},
                        'source_mtime_epoch':source_mtime, 'jobs':env['JOBS'], 'timezone':env['TZ']}
                report['builds'].append(record)
                if run.returncode:raise RuntimeError('build failed: '+directory)
                for repo in eng.REPOS:
                    artifact=eng.load_json(destination/repo/'packaging/nia/artifact.json')
                    for executable in artifact['executables']:
                        name=repo+'/'+executable['source'];p=destination/name
                        record['binaries'][name]=hashlib.sha256(p.read_bytes()).hexdigest()
                results.append(record['binaries'])
            if not results[0] or results[0]!=results[1]:raise RuntimeError('binary hashes differ')
            if eng.source_subject(ROOT)!=report['source_subject'] or workspace_inputs()!=report['workspace_inputs']:
                raise RuntimeError('source changed during builds')
            report['result']='identical-binaries';report['binary_count']=len(results[0])
    except (OSError,RuntimeError,subprocess.SubprocessError) as exc:
        report['result']='failed';report['error']=str(exc)
    finally:
        report['ended_utc']=datetime.now(timezone.utc).isoformat()
        (output/'report.json').write_text(json.dumps(report,indent=2)+'\n')
        print(output/'report.json')
    return 0 if report['result']=='identical-binaries' else 1


if __name__=='__main__':raise SystemExit(main())
