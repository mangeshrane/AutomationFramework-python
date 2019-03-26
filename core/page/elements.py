'''
Created on Feb 13, 2019

@author: mrane
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Elements(object):
    '''
    WebElement descriptor to define webelements in page objects
    '''

    def __init__(self, by, locator, wait=10):
        '''
        Constructor: 
        takes selenium.webdriver.common.by.By as by and locator as string locator value
        '''
        self._by = by
        self._locator = locator
        self._wait = wait

    def __get__(self, instance, owner):
        if self._wait > 0:
            return WebDriverWait(instance.driver, self._wait).until(
                EC.presence_of_element_located((self._by, self._locator)))
        else:
            return instance.driver.find_elements(self._by, self._locator)

    def __set__(self, instance, name):
        pass

    def __delete__(self):
        pass
