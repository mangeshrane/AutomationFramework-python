'''
Created on Mar 7, 2019

@author: 
'''
import pytest

import allure
from allure_commons.types import AttachmentType
from core.configuration import CONFIG

  
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        try:
            _driver = item.cls.driver
        except Exception:
            pass
        # if not exception
        else:
            if report.when == "call":
                extra.append(pytest_html.extras.url(_driver.current_url))
            if report.when == 'call' or report.when == "setup":
                xfail = hasattr(report, 'wasxfail')
                # Go to screenshot only when UI tests
                if (report.skipped and xfail) or (report.failed and not xfail):
                    url = _driver.current_url
                    extra.append(pytest_html.extras.url(url))
                    screenshot = _driver.get_screenshot_as_base64()
                    extra.append(pytest_html.extras.image(screenshot, ''))
                    if CONFIG.get("reporting", "html") == "allure":
                        allure.attach('screenshot', _driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    report.extra = extra

def pytest_runtest_call(item):
    """ called to execute the test ``item``. """
    print(dir(item))

