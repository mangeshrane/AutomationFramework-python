'''
Created on Feb 28, 2019

@author: mrane
'''
from core.browsers.web_drivers import WebDrivers

class Base:
    '''
    This fixture contains the set up and tear down code for each test.
    
    '''
    @classmethod
    def setup_class(cls):
        cls.driver = WebDrivers().get()

    @classmethod
    def teardown_class(cls):
        cls.driver.close()
