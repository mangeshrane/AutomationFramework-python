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

 
 
import os
 
def pytest_configure(config):
    config._foo = FooBar()
    config.pluginmanager.register(config._foo)
    if os.path.isfile('report'):
        os.remove('report')
 
 
def pytest_unconfigure(config):
    foo = getattr(config, '_foo', None)
    if foo:
        del config._foo
        config.pluginmanager.unregister(foo)
 
class FooBar(object):
 
    def pytest_runtest_makereport(self, item, call):
        with open('report', 'a+') as f:
            f.write(call.when + '\n')
 
 


# 
#  
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#      
#     with open('report', 'w') as f:
#             f.write(call.when + '\n') 
#              
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     print("inside")  
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         try:
#             _driver = item.cls.driver
#         except Exception:
#             print("Not able to capture screeshot not UI test")
#          if not exception
#         else:
#             if report.when == "call":
#                 extra.append(pytest_html.extras.url(_driver.current_url))
#             if report.when == 'call' or report.when == "setup":
#                 xfail = hasattr(report, 'wasxfail')
#                  Go to screenshot only when UI tests
#                 if (report.skipped and xfail) or (report.failed and not xfail):
#                     url = _driver.current_url
#                     extra.append(pytest_html.extras.url(url))
#                     screenshot = _driver.get_screenshot_as_base64()
#                     print("attaching screenshot")
#                     extra.append(pytest_html.extras.image(screenshot, ''))
#                     if CONFIG.get("reporting", "html") == "allure":
#                         allure.attach('screenshot', _driver.get_screenshot_as_png(), type=AttachmentType.PNG)
#     report.extra = extra
#  
#  
# def _capture_screenshot(node, name):
#     name = os.path.join(dirname(dirname(abspath(__file__))), "..", "results", name)
#     WebDrivers.get(node).get_screenshot_as_file(name)
#     return name

# def pytest_configure(config):
#     """Register pytest-splinter's deferred plugin."""
#     if config.pluginmanager.getplugin('xdist'):
#         config.pluginmanager.register("core.reporter.pytest_plugin")
#         
# def pytest_xdist_setupnodes(config, specs):
#     """ called before any remote node is set up. """
    

