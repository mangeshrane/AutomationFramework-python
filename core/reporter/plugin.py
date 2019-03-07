'''
Created on Mar 7, 2019

@author: 
'''
import logging

import pytest
from contextlib import contextmanager
from multiprocessing.sharedctypes import template

 
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     print(item._extra[report.when]["log"])
#     if report.when == 'call':
#         # always add url to report
#         extra.append(pytest_html.extras.url(""))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
#         report.extra = extra

_logger = logging.getLogger()
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    item._json_report_extra = {}
    yield
    del item._json_report_extra

@contextmanager
def _capture_log(item, when):
    handler = LoggingHandler()
    _logger.addHandler(handler)
    try:
        yield
    finally:
        _logger.removeHandler(handler)
    item._json_report_extra[when]['log'] = handler.records

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup(item):
    item._json_report_extra['setup'] = {}
    if _must_omit('log'):
        yield
    else:
        with _capture_log(item, 'setup'):
            yield

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    item._json_report_extra['call'] = {}
    if _must_omit('log'):
        yield
    else:
        with _capture_log(item, 'call'):
            yield

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item):
    item._json_report_extra['teardown'] = {}
    if _must_omit('log'):
        yield
    else:
        with _capture_log(item, 'teardown'):
            yield

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    print("# ------------------ Getting Reporter ----------------------------")
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    
    print("=" * 50)
    print(dir(item), call, report)
    print("=" * 50)
    
    # Hook runtest_makereport to access the item *and* the report
    if not _must_omit('streams'):
        streams = {key: val for when_, key, val in item._report_sections if
                   when_ == report.when and key in ['stdout', 'stderr']}
        item._json_report_extra[call.when].update(streams)
    # Attach the JSON details to the report. If this is an xdist worker,
    # the details will be serialized and relayed with the other attributes
    # of the report.
    report._json_report_extra = item._json_report_extra
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url(""))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        else:
            extra.append(pytest_html.extras.html('<div>Additional HTML  asds</div>'))
            for log in report._json_report_extra:
                extra.append(pytest_html.extras.html('<div>' + log + '</div>'))
            
            template = """
            <div>
                <table>
                    <tr>
                        <td> Filename </td>
                        <td> 
                
                </table>
            </div>
            """
        report.extra = extra
    print(report._json_report_extra)

def _must_omit(key):
    return key in ["traceback", "error"]
    
    
class LoggingHandler(logging.Handler):

    def __init__(self):
        super(LoggingHandler, self).__init__()
        self.records = []

    def emit(self, record):
        d = dict(record.__dict__)
        d['msg'] = record.getMessage()
        d['args'] = None
        d['exc_info'] = None
        d.pop('message', None)
        self.records.append(d)