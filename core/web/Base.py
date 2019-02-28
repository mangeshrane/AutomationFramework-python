'''
Created on Feb 28, 2019

@author: mrane
'''
from selenium import webdriver
import pytest
import unittest

@pytest.fixture(scope="class")
def web_driver(request):
    driver = webdriver.Chrome("C:/chromedriver.exe")
    request.cls.driver = driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("web_driver")
class Base(unittest.TestCase):
    '''
    This fixture contains the set up and tear down code for each test.
    
    '''
    @pytest.fixture(scope="class")
    def web_driver(self, request):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        request.cls.driver = driver
        yield
        driver.close()
   



