'''
Created on Feb 12, 2019

@author: mrane
'''

class CreatePage(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @staticmethod
    def get(page, driver):
        pobject = page(driver)
        pobject.load()
        try:
            pobject.is_loaded()
            return pobject
        except AssertionError:
            pobject.load()
            pobject.is_loaded()
            return pobject
    