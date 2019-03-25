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
import pytest

from core.reporter import pytest_plugin

__all__ = []
__version__ = 0.1
__date__ = '2019-02-19'
__updated__ = '2019-03-13'

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
            parser.add_option("-d", "--testdir", dest="testdir",
                              help="specifies the directory to run tests from [default: %default]", metavar="String")
            parser.add_option("-t", "--tags", dest="tags", help="tags to run tagged tests [default: %default]",
                              metavar="TAGS")
            parser.add_option("-c", "--config", dest="config", help="Override default config file [default: %default]",
                              metavar="FILE")
            parser.add_option("-p", "--pattern", dest="pattern", help="file patterns eg. *_test.py [default: test*.py]",
                              metavar="String")
            parser.add_option("-n", "--threads", dest="threads", help="threads are used to run test as number of threads",
                              metavar="String")
            parser.add_option("-b", "--driver", dest="driver", help="override driver from config file",
                              metavar="browserName")
            parser.add_option("-r", "--report", dest="report", help="specify report generation", metavar="reportType")

            # Default option values
            parser.defaults['pattern'] = "test*.py"
            parser.defaults['testdir'] = os.getcwd()

            # Base command
            _cmd = []

            # process options
            (opts, args) = parser.parse_args(argv)
            if opts.testdir:
                _cmd.append(opts.testdir)
                print("-- Using test directoty as " + opts.testdir)
            if opts.tags:
                _cmd.append("--tags " + opts.tags)
                print("-- tags = %s" % opts.tags)
            if opts.config:
                os.environ['AUTO_CONFIG'] = opts.config
                print("-- overriding default config file = %s" % opts.config)
            if opts.threads:
                _cmd.append("-n " + opts.threads)
                _cmd.append("--dist=loadscope")
                # _cmd.append("-p core.reporter.plugin")
                print("-- Using number of threads :" + opts.threads)
            if opts.driver:
                os.environ["CORE.DRIVER"] = opts.driver
                print("-- overriding default driver configuration: " + opts.driver)
            if opts.report:
                if "html" in opts.report:
                    _cmd.append("--self-contained-html")
                    _cmd.append("--html=results/report.html")
                if "json" in opts.report:
                    _cmd.append("--json-report")
                    _cmd.append("--json-report-file=results/report.json")
                if "allure" in opts.report:
                    _cmd.append("--alluredir=results/")

            # Running tests
                pytest.main(_cmd, plugins=[pytest_plugin])

        except Exception as e:
            indent = len(program_name) * " "
            sys.stderr.write(program_name + ": " + repr(e) + "\n")
            sys.stderr.write(indent + "  for help use --help")
            return 2


if __name__ == "__main__":
    main()
