'''
Created on Feb 11, 2019

@author: mrane
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.logger import LOG


class Element(object):
    '''
    WebElement descriptor to define webelements in page objects
    This will returns Webelement when it is accessed
    '''

    def __init__(self, by, locator, wait=10):
        '''
        Constructor: 
        Parameters:
        ---------- 
        by : selenium.webdriver.common.by.By
        locator: string locator value
        wait: [optional] default=10
        
        '''
        self._by = by
        self._locator = locator
        self._wait = wait
        self._element = None

    def __get__(self, instance, owner):
        if self._wait:
            _element = WebDriverWait(instance.driver, self._wait).until(
                EC.presence_of_element_located((self._by, self._locator)))
        else:
            _element = instance.driver.find_element(self._by, self._locator)
        LOG.info("returning element {}={} ".format(self._by, self._locator))
        return _element

    def __set__(self, instance, name):
        pass

    def __delete__(self):
        pass

    
    
