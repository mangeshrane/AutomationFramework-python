'''
Created on Mar 7, 2019

@author: 
'''
import logging

import pytest
from contextlib import contextmanager
import os

import profile
from os.path import dirname, abspath
from core.browsers.web_drivers import WebDrivers


_logger = logging.getLogger()
    
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_protocol(item, nextitem):
#     pass
# 
# @contextmanager
# def _capture_log(item, when):
#     pass
# 
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_setup(item):
#     pass
# 
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_call(item):
#     pass
# 
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_teardown(item):
#     pass


def _capture_screenshot(name):
    name = os.path.join(dirname(dirname(abspath(__file__))), "..", "results", name)
    WebDrivers.get().get_screenshot_as_file(name)
    return name

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    
    # Go to screenshot only when UI tests
    if WebDrivers.get():
        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                file_name = file_name.replace(r"/", "_", -1)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % _capture_screenshot(file_name)
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra
                
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url(WebDrivers.get().current_url))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        else:
            extra.append(pytest_html.extras.html('<div>Additional HTML  asds</div>'))
            for log in report._json_report_extra:
                extra.append(pytest_html.extras.html('<div>' + log + '</div>'))
            
        report.extra = extra

    
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