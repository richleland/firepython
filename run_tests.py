#!/usr/bin/env python

import os
import sys
import nose

FPY_MODS = [
    'firepython.utils',
    'firepython.middleware',
    'firepython.handlers',
    'firepython._const',
]
SYSARGS = ['nosetests']
EXT_ARGS = sys.argv[1:]

W_COVER = os.environ.get('COVER') or os.environ.get('IC')
W_ITESTS = os.environ.get('ITESTS') or os.environ.get('IC')

NOSE_ARGV = SYSARGS[:] + EXT_ARGS[:]
if W_COVER:
    NOSE_ARGV += ['--with-coverage', '--cover-erase']
    for mod in FPY_MODS:
        NOSE_ARGV += ['--cover-package', mod]

if W_ITESTS:
    NOSE_ARGV += ['-i', '^itest']


def main():
    return nose.main(argv=NOSE_ARGV)


if __name__ == '__main__':
    sys.exit(main())