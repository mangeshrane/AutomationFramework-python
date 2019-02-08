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


def dataFile(filename, data_filter, headers=True):
    if str(filename).endswith("csv"):
        dataset = CSVReader(filename, headers)
    elif str(filename).endswith("xls") or str(filename).endswith("xlsx"):
        dataset = ExcelReader.get_data_map(filename, data_filter, headers)
        edata = []
        edata = [ data.keys() for data in dataset ]
    elif str(filename).endswith("json"):
        dataset = JSONReader(filename, headers)
    else:
        raise UnsupportedFileFormat("Datafile must be csv, xls or json")
    
    def wrap(f):
        def wrapper(*margs, **kwargs):
            def parser(func, args):
                func(*args)
            edata.insert(0, margs)
            for data in edata:
                parser(f, data)
        return wrapper
    return wrap

class UnsupportedFileFormat(Exception):
    pass
