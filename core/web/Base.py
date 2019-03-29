'''
Created on Feb 28, 2019

@author: mrane
'''

import pytest
from core.browsers.web_drivers import WebDrivers

@pytest.mark.usefixtures("web_driver")
class Base():
    '''
    This fixture contains the set up and tear down code for each test.
    
    '''
    @pytest.fixture(scope="class", autouse=True)
    def web_driver(self, request):
        self.driver = WebDrivers().get()
        request.cls.driver = self.driver        
        yield 
        # Close browser window:
        self.driver.quit()
