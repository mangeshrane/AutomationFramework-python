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
from core.configuration import CONFIG

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
    try:
        _driver  = item.cls.driver
    except Exception:
        print("Not able to capture screeshot not UI test")
    # if not exception
    if report.when == "call":
        extra.append(pytest_html.extras.url(_driver.current_url))
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail') 
        # Go to screenshot only when UI tests
        if (report.skipped and xfail) or (report.failed and not xfail):
            url = _driver.current_url
            extra.append(pytest_html.extras.url(url))
            screenshot = _driver.get_screenshot_as_base64()
            print("attaching screenshot")
            extra.append(pytest_html.extras.image(screenshot, ''))
            if CONFIG.get("reporting", "html") == "allure":
                allure.attach('screenshot', _driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    report.extra = extra

