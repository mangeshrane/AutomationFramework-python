'''
Created on Feb 5, 2019

@author: mrane
'''

class Page(object):
    
    def load(self):
        raise NotImplementedError("load method is not implemented")
    
    def is_loaded(self):
        raise NotImplementedError("is_loaded method is not implemented")

