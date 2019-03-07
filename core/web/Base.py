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
    @pytest.fixture(scope="class")
    def web_driver(self, request):
        driver = WebDrivers().get()
        request.cls.driver = driver
        yield
        driver.quit()
   



