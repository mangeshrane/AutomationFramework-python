import csv

class CSVReader(object):
    
    def __init__(self, filename):
        self.f = open(filename)
        
    def getData(self):
        pass