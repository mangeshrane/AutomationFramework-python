from functools import wraps
from core.readers.csv_reader import CSVReader
from core.readers.excel_reader import ExcelReader
from core.readers.json_reader import JSONReader

def data(dataset):
    def wrap(f):
        def parser(func, args):
            func(*args)
        def wrapper(*args, **kwargs):
            for data in dataset:
                parser(f, data)
        return wrapper
    return wrap


def dataFile(filename, headers=True):
    if str(filename).endswith("csv"):
        dataset = CSVReader(filename, headers)
    elif str(filename).endswith("xls") or str(filename).endswith("xlsx"):
        dataset = ExcelReader(filename, headers)
    elif str(filename).endswith("json"):
        dataset = JSONReader(filename, headers)
    else:
        raise UnsupportedFileFormat("Datafile must be csv, xls or json")
    
    def wrap(f):
        def parser(func, args):
            func(*args)
        def wrapper(*args, **kwargs):
            for data in dataset:
                parser(f, data)
        return wrapper
    return wrap

@data([[1, 2],[3, 2],[3, 3]])
def test(k, l):
    print("Got parameter ", k, l)


class UnsupportedFileFormat(Exception):
    pass
