#!/usr/in/env python
from __future__ import with_statement
import os
import re
import shutil
import subprocess
import sys
import tempfile


def system(*args, **kwargs):
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, err = proc.communicate()
    return out


def main():
    modified = re.compile('^[AM]+\s+(?P<name>.*\.py)', re.MULTILINE)
    files = system('git', 'status', '--porcelain')
    files = modified.findall(files)

    tempdir = tempfile.mkdtemp()
    for name in files:
        filename = os.path.join(tempdir, name)
        filepath = os.path.dirname(filename)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        with file(filename, 'w') as f:
            system('git', 'show', ':' + name, stdout=f)
    output = system('pep8', '.', cwd=tempdir)
    shutil.rmtree(tempdir)
    if output:
        print output,
        sys.exit(1)


if __name__ == '__main__':
    main()
