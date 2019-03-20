'''
Created on Mar 19, 2019

@author: mrane
'''
import requests
from requests import Session
import urllib.parse
from core.configuration import CONFIG
from core.api.response import Response

   
class Request(object):
    '''
    Wrapper around requests library whoch makes building requests and response Validation easier
    '''
    
    def __init__(self):

        self._headers = {}
        self._body = None
        self._cookies = {}
        self._params = {}
        self._query_param = None
        self._form_parm = None
        self._path_param = None
        self._base_url = None 
        self.stream = False
        self._timeout = CONFIG.get("api.request.timeout", None)
        self._cert_file = False
        self._json_data = None
        self._session = Session()
        self._method = ""
        self._proxy = None
    
    
        
    def header(self, Accept):
        if type(Accept).__name__ == 'dict':
            self._headers.update(Accept)
            
        else:
            raise ValueError
        return self
    
    def add_header(self, key, value):
        self._headers[key] = value
    
    def cookie(self, key, value):
        self._cookies[key] = value
        return self
    
    def add_params(self, key, value):
        if key in self._params:
            if isinstance(self._params[key], list):
                self._params[key].append(value)
            else:
                self._params[key] = [self._params[key], value]
        else:
            self._params[key] = value
        return self
        
    def set_base_url(self, url):
        self._base_url = url
        return self
        
    def set_body(self, body, file=False):
        if file:
            self._body = {'file': open(body, 'rb')}
        else:
            self.set_body(body)
        return self
    
    def raw_reponse(self):
        self.stream = True
    
    def relax_ssl_validation(self):
        self._cert_file = False
        return self
    
    def set_timeout(self, timeout):
        self._timeout=timeout
    
    def set_cert_file(self, path):
        self._cert_file = path
    
    def set_json_body(self, json_data):
        self._json_data = json_data
        
    def _build_request(self, method, endpoint=""):
        if endpoint:
            self._base_url = urllib.parse.urljoin(self._base_url, endpoint)
        self._request = requests.Request(method, self._base_url, data=self._body, json=self._json_data, headers=self._headers)
        self._request = self._request.prepare()
        
    def _get_resp(self):
        return Response(self._session.send(self._request,
                                stream=self.stream,
                                verify=self._cert_file,
                                proxies=self._proxy,
                                cert=self._cert_file,
                                timeout=self._timeout
                            ))
        
    def get(self, endpoint=''):
        self._build_request('GET', endpoint)
        return self._get_resp()
        
    def post(self, endpoint=''):
        self._build_request('POST', endpoint)
        return self._get_resp()
    
    
class AuthConfig(object):
    
    def basic(self):
        pass
    
    def digest_auth(self):
        pass
    
    def o_auth1(self):
        pass
    
    
class ContentType:
    JSON = {'Content-Type': 'application/json'}
    XML = {'Content-Type': "application/xml"}
    HTML = {'Content-Type': "text/html"}
    TEXT = {'Content-Type': 'text/plain'}
    URLENC = {'Content-Type': 'application/x-www-form-urlencoded'}
    BINARY = {'Content-Type': 'application/octet-stream'}

class Accept:
    XMl = {'Accept': 'application/xml'}
    JSON = {'Accept': 'application/json'}