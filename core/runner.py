#!/usr/bin/env python
# encoding: utf-8
'''
core.runner -- shortdesc

core.runner is a pytest test case runner

@author:     mrane
'''

import sys
import os

from optparse import OptionParser
from unittest2.loader import TestLoader
import unittest2
import pytest

__all__ = []
__version__ = 0.1
__date__ = '2019-02-19'
__updated__ = '2019-02-19'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

def main(argv=None):
    '''Command line options.'''

    program_name = os.path.basename(sys.argv[0])
    program_version = "v0.1"
    program_build_date = "%s" % __updated__

    program_version_string = '%%prog %s (%s)' % (program_version, program_build_date)

    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = OptionParser(version=program_version_string)
        parser.add_option("-t", "--tags", dest="tags", help="tags to run tagged tests [default: %default]", metavar="TAGS")
        parser.add_option("-c", "--config", dest="config", help="Override default config file [default: %default]", metavar="FILE")
        parser.add_option("-p", "--pattern", dest="pattern", help="file patterns eg. *_test.py [default: test*.py]", metavar="String")
        parser.add_option("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %default]")
        
        parser.defaults['pattern'] = "test*.py"
        # process options
        (opts, args) = parser.parse_args(argv)
        if opts.verbose:
            print("verbosity level = %d" % opts.verbose)
        if opts.tags:
            print("tags = %s" % opts.tags)
        if opts.config:
            print("config = %s" % opts.config)
        
        pytest.main([os.getcwd(), "-v", "--html=results/report.html"], plugins=["core.reporter.plugin"])        

    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


if __name__ == "__main__":
    main()