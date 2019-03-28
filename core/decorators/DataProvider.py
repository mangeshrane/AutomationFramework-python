from core.data_providers.csv_reader import CSVReader
from core.data_providers.excel_reader import ExcelReader
from core.data_providers.json_reader import JSONReader

def dataFile(filename, data_filter="", fields_string=None, headers=True):
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
    
    if fields_string:
        data = *(fields_string, edata)
        return data
    else:
        edata = []
        edata = [tuple(data.values()) for data in dataset]
        return edata


class UnsupportedFileFormat(Exception):
    pass
