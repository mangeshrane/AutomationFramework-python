'''
Created on Feb 12, 2019

@author: mrane
'''
from core.page.page import Page
from core.logger import LOG


class CreatePage(object):

    @staticmethod
    def get(page, driver):
        try:
            issubclass(page, Page)
        except AssertionError:
            LOG.error("Not a Page")
            raise AssertionError("Not a Page")
        pobject = page(driver)
        pobject.load()
        try:
            pobject.is_loaded()
            LOG.info("{} page is loaded".format(page.__name__))
            return pobject
        except AssertionError:
            pobject.load()
            pobject.is_loaded()
            return pobject
