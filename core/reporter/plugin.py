'''
Created on Mar 7, 2019

@author: 
'''
import logging

import pytest
import os

from os.path import dirname, abspath
from core.browsers.web_drivers import WebDrivers

_logger = logging.getLogger()

def _capture_screenshot(node, name):
    name = os.path.join(dirname(dirname(abspath(__file__))), "..", "results", name)
    WebDrivers.get(node).get_screenshot_as_file(name)
    return name

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        # Go to screenshot only when UI tests
        print("Going to screenshot")
        if (report.skipped and xfail) or (report.failed and not xfail) and WebDrivers.get(report.nodeid):
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = file_name.replace(r"/", "_", -1)
            print("getting screenshot driver ", WebDrivers.get(report.nodeid))
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % _capture_screenshot(report.nodeid, file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
                
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url(WebDrivers.get(report.nodeid).current_url))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        else:
            extra.append(pytest_html.extras.html('<div>Additional HTML  asds</div>'))
            
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
        