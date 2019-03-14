'''
Created on Feb 11, 2019

@author: mrane
'''
from core.page.page import Page

class Dashboard(Page):
    '''
    classdocs
    '''
    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver
    
    def load(self):
        pass
        
    def is_loaded(self):
        pass