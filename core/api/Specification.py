'''
Created on Mar 19, 2019

@author: mrane
'''

class Specification(object):
    '''
    classdocs
    '''
    
    _content_type = None
    _encoding = None
    
    
    def __init__(self, params):
        '''
        Constructor
        '''


class Headers(object):
    
    class ContentType:
        JSON = {'Content-Type': 'application/json'}
        
    class Accept:
        XMl = {'Accept': 'application/xml'}
        JSON = {'Accept': 'application/json'}
    