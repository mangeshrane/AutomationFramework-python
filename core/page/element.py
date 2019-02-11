'''
Created on Feb 11, 2019

@author: mrane
'''

class Element(object):
    '''
    WebElement descriptor to define webelements in page objects
    '''

    def __init__(self, by, locator):
        '''
        Constructor: 
        takes selenium.webdriver.common.by.By as by and locator as string locator value
        '''
        self._by = by
        self._locator = locator
    
    def __get__(self, instance, owner):
        print(instance)
        return instance.driver.find_element(self._by, self._locator)
    
    def __set__(self, instance, name):
        pass
    
    def __delete__(self):
        pass
