import json
from collections import namedtuple
from builtins import staticmethod

class JSONReader(object):
    
    @staticmethod
    def get_data_map(filename):
        with open(filename) as f:
            raw = f.read()
        j = json.loads(raw)
        return j
    
    @staticmethod
    def json2obj(name, data): 
        return json.loads(data, object_hook=lambda d: namedtuple(name, d.keys())(*d.values()))