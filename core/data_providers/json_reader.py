import json

class JSONReader(object):
    
    @staticmethod
    def get_data_map(filename):
        with open(filename) as f:
            raw = f.read()
        j = json.loads(raw)
        return j
            