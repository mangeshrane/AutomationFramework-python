'''
Created on Feb 28, 2019

@author: mrane
'''

import pytest
from core.browsers.web_drivers import WebDrivers
import unittest

@pytest.mark.usefixtures("web_driver")
class Base(unittest.TestCase):
    '''
    This fixture contains the set up and tear down code for each test.
    
    '''
    _cache = {}
    @pytest.fixture(scope="class", autouse=True)
    def web_driver(self, request):
        name = request.module.__name__
        
        if name in Base._cache:
            request.cls.driver = Base._cache[name]
        else:    
            self.driver = WebDrivers().get()
            Base._cache[name] = self.driver
            request.cls.driver = self.driver
#         def _take_screenshot_on_failure():
#                 if getattr(request.node, 'splinter_failure', True):
#                     _take_screenshot(
#                         request=request,
#                         fixture_name=parent.__name__,
#                         session_tmpdir=session_tmpdir,
#                         browser_instance=browser,
#                         splinter_screenshot_dir=splinter_screenshot_dir,
#                         splinter_screenshot_getter_html=splinter_screenshot_getter_html,
#                         splinter_screenshot_getter_png=splinter_screenshot_getter_png,
#                         splinter_screenshot_encoding=splinter_screenshot_encoding,
#                     )
#                 request.addfinalizer(_take_screenshot_on_failure)
        yield 
        # Close browser window:
        self.driver.quit()
