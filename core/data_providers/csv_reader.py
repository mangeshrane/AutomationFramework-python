import csv
from core.logger import log


class CSVReader(object):
    
    def __init__(self):
        pass
        
    @staticmethod
    def get_data_map(filename, header=[]):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=header)
            return list(reader)