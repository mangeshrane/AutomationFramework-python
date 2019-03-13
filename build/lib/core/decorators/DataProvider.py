from core.data_providers.csv_reader import CSVReader
from core.data_providers.excel_reader import ExcelReader
from core.data_providers.json_reader import JSONReader


def data(data):
    
    if not all(isinstance(i, tuple) for i in data):
        raise Exception("Need a sequence of tuples as data...")
    
    def wrap(func):
        def wrapper(self, *args, **kwargs):
            for d in data:
                try:
                    func(self, *(d + args))
                except AssertionError as e:
                    raise AssertionError(e.message + " (data set used: %s)" % repr(d))
        return wrapper
    return wrap


def dataFile(filename, data_filter="", headers=True):
    
    if str(filename).endswith("csv"):
        dataset = CSVReader.get_data_map(filename)
        if headers:
            dataset = dataset[1:]
    elif str(filename).endswith("xls") or str(filename).endswith("xlsx"):
        dataset = ExcelReader.get_data_map(filename, data_filter, headers)
    elif str(filename).endswith("json"):
        dataset = JSONReader.get_data_map(filename)
    else:
        raise UnsupportedFileFormat("Datafile must be csv, xls or json")
    
    edata = []
    edata = [ tuple(data.values()) for data in dataset ]
    
    def wrap(func):
        def wrapper(self, *args, **kwargs):
            for d in edata:
                try:
                    func(self, *(d + args))
                except AssertionError as e:
                    raise AssertionError(e.message + " (data set used: %s)" % repr(d))
        return wrapper
    return wrap

class UnsupportedFileFormat(Exception):
    pass
