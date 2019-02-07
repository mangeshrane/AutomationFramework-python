from core.readers.csv_reader import CSVReader
from core.readers.excel_reader import ExcelReader
from core.readers.json_reader import JSONReader

def data(d):
    def wrap(f):
        
        def wrapper(*margs, **kwargs):
            def parser(func, args):
                func(*args)
            
            for data in d:
                data.insert(0, margs)
                parser(f, data)
        return wrapper
    return wrap


def dataFile(filename, headers=True):
    if str(filename).endswith("csv"):
        dataset = CSVReader(filename, headers)
    elif str(filename).endswith("xls") or str(filename).endswith("xlsx"):
        dataset = ExcelReader(filename, headers)
        edata = []
        for data in dataset:
            edata.append(data.keys())
    elif str(filename).endswith("json"):
        dataset = JSONReader(filename, headers)
    else:
        raise UnsupportedFileFormat("Datafile must be csv, xls or json")
    
    def wrap(f):

        def wrapper(*margs, **kwargs):
            def parser(func, args):
                func(*args)
            
            for data in dataset:
                data.insert(0, margs)
                parser(f, data)
        return wrapper
    return wrap

class UnsupportedFileFormat(Exception):
    pass
