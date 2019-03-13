'''
Created on Mar 7, 2019

@author: 
'''
import logging

import pytest
import os

from os.path import dirname, abspath
from core.browsers.web_drivers import WebDrivers
from core.logger import log

_logger = logging.getLogger()
    
def _capture_screenshot(node, name):
    name = os.path.join(dirname(dirname(abspath(__file__))), "..", "results", name)
    WebDrivers.get(node).get_screenshot_as_file(name)
    return name

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    _driver  = item.cls.driver
    
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        # Go to screenshot only when UI tests
        if (report.skipped and xfail) or (report.failed and not xfail):
            url = _driver.current_url
            extra.append(pytest_html.extras.url(url))
            screenshot = _driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))
            report.extra = extra
                
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url(_driver.current_url))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        else:
            extra.append(pytest_html.extras.html('<div>Additional HTML  asds</div>'))
            
        report.extra = extra
