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
    @pytest.fixture(scope="class")
    def web_driver(self, request):
        self.driver = WebDrivers().get(request.node.nodeid + "::" + request.node.name)
        request.cls.driver = self.driver
        yield
        self.driver.quit()
    
   



