'''
Created on Mar 20, 2019

@author: mrane
'''
import json

from requests.models import Response as rp 
from collections import namedtuple

class Response(object):
    '''
    classdocs
    '''
    
    def __init__(self, response):
        '''
        Constructor
        '''
        if not isinstance(response, rp):
            raise ValueError
        self.url = response.url
        self.status_code = response.status_code
        self._request = response.request
        self.body = PyJSON(response.text)
        self.reason = response.reason
        self.cookies = response.cookies
        self.headers = response.headers
    
    def assert_response_code(self, response_code):
        assert self.status_code == response_code, "Response code does not match, expected {0} but found {1}".format(response_code, self.status_code)
        return self
    
    def _json_object_hook(self, d): 
        return namedtuple('response', d.keys())(*d.values())

    def json2obj(self, data): 
        return json.loads(data, object_hook=self._json_object_hook)

    
    
class PyJSON(object):
    def __init__(self, d):
        if type(d) is str:
            d = json.loads(d)

        self.from_dict(d)

    def from_dict(self, d):
        self.__dict__ = {}
        for key, value in d.items():
            if type(value) is dict:
                value = PyJSON(value)
            self.__dict__[key] = value

    def to_dict(self):
        d = {}
        for key, value in self.__dict__.items():
            if type(value) is PyJSON:
                value = value.to_dict()
            d[key] = value
        return d

    def __repr__(self):
        return str(self.to_dict())

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]