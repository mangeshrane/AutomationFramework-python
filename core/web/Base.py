'''
Created on Feb 28, 2019

@author: mrane
'''

import pytest
from core.browsers.web_drivers import WebDrivers
from core.configuration import CONFIG

@pytest.mark.usefixtures("web_driver")
class Base():
    
    @pytest.fixture(scope=CONFIG.get("tests.browser.scope", "class"), autouse=True)
    def web_driver(self, request):
        '''
        This fixture contains the set up and tear down code for each test.
        
        '''
        self.driver = WebDrivers().get()
        request.cls.driver = self.driver        
        yield 
        # Close browser window:
        self.driver.quit()
