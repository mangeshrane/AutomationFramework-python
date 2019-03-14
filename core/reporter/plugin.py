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
import allure
from allure_commons.types import AttachmentType

_logger = logging.getLogger()
    
def _capture_screenshot(node, name):
    name = os.path.join(dirname(dirname(abspath(__file__))), "..", "results", name)
    WebDrivers.get(node).get_screenshot_as_file(name)
    return name

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    
    extra = getattr(report, 'extra', [])
    _driver = None
    try:
        _driver  = item.cls.driver
        
        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail') 
            # Go to screenshot only when UI tests
            if (report.skipped and xfail) or (report.failed and not xfail):
                url = _driver.current_url
                extra.append(pytest_html.extras.url(url))
                screenshot = _driver.get_screenshot_as_base64()
                extra.append(pytest_html.extras.image(screenshot, ''))
                allure.attach('screenshot', _driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                report.extra = extra
    except Exception:
        print("Not able to capture screeshot not UI test")
                    
    if report.when == 'call':
        # always add url to report
        if _driver:
            extra.append(pytest_html.extras.url(_driver.current_url))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        else:
            extra.append(pytest_html.extras.html('<div>Additional HTML  asds</div>'))
            
        report.extra = extra

# ---------------------------------------------------------------------------------------------------------------------