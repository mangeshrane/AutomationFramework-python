import csv

class CSVReader(object):
    
    def __init__(self, filename):
        self.f = open(filename)
        
    def __call__(self):
        pass