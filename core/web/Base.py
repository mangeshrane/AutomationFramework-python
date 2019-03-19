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
        # Close browser window:
#         self.driver.quit()
