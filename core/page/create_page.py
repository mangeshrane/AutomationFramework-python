'''
Created on Feb 12, 2019

@author: mrane
'''
from core.page.page import Page


class CreatePage(object):

    def __init__(self):
        '''
        Constructor
        '''
        pass

    @staticmethod
    def get(page, driver):
        try:
            issubclass(page, Page)
        except AssertionError:
            raise AssertionError("Not a Page")
        pobject = page(driver)
        pobject.load()
        try:
            pobject.is_loaded()
            return pobject
        except AssertionError:
            pobject.load()
            pobject.is_loaded()
            return pobject
