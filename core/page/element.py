'''
Created on Feb 11, 2019

@author: mrane
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import time


class Element(object):
    '''
    WebElement descriptor to define webelements in page objects
    '''

    def __init__(self, by, locator, wait=0):
        '''
        Constructor: 
        takes selenium.webdriver.common.by.By as by and locator as string locator value
        '''
        self._by = by
        self._locator = locator
        self._wait = wait
        self._element = None

    def __get__(self, instance, owner):
        if self._wait > 0:
            _element = WebDriverWait(instance.driver, self._wait).until(
                EC.presence_of_element_located((self._by, self._locator)))
        else:
            _element = instance.driver.find_element(self._by, self._locator)
        return _element

    def __set__(self, instance, name):
        pass

    def __delete__(self):
        pass

    def send_keys(self, keys, wait):
        try:
            if self._element:
                self._element.send_keys(keys)
            else:
                self._element = self.__get__(self, None)
        except ElementNotInteractableException:
            time.sleep(10)
            self.send_keys(keys)
