import json
from collections import namedtuple
from builtins import staticmethod
from core.file_manager.file_manager import FileManager
import os
from core.logger import LOG


class JSONReader(object):

    @staticmethod
    def get_data_map(filename):
        with open(os.path.join(FileManager.get_test_datadir(), filename)) as f:
            raw = f.read()
        j = json.loads(raw)
        LOG.info("returning data from json file : " + filename)
        return j

    @staticmethod
    def json2obj(name, data):
        return json.loads(data, object_hook=lambda d: namedtuple(name, d.keys())(*d.values()))
