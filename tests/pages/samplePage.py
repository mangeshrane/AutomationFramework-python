'''
Created on Feb 7, 2019

@author: mrane
'''
from core.decorators.DataProvider import data, dataFile

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @data([[1, 2], [3, 4], [5, 6]])
    def printData(self, a, b):
        print("Got " + str(a) + " " + str(b))
        
    @dataFile(r"D:\Workspace\AutomationFramework-Java\src\test\resources\testData\data.xlsx", filter="Add Customer")
    def printDatas(self, *args):
        print("Got " + str(args))