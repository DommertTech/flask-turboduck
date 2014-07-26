#!/usr/bin/env python
import os
import sys
import unittest

from flask_turboduck import tests

def runtests(*test_args):
    suite = unittest.TestLoader().loadTestsFromModule(tests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.failures:
        sys.exit(1)
    elif result.errors:
        sys.exit(2)
    sys.exit(0)

if __name__ == '__main__':
    runtests(*sys.argv[1:])
