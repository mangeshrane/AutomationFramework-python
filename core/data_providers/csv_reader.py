import csv
import os
from core.logger import log
from core.file_manager.file_manager import FileManager


class CSVReader(object):
    
    def __init__(self):
        pass
        
    @staticmethod
    def get_data_map(filename, header=None):
        with open(os.path.join(FileManager.get_test_datadir(), filename)) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=header)
            return list(reader)