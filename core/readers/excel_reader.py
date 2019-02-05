import xlrd
from _sqlite3 import Row


class ExcelReader(object):
    
    def __init__(self, filename, filter, headers=True, sheet_no=0):
        self.filename = filename
        self.workbook = xlrd.open_workbook(filename)
        self.filter = filter
        self.sheet = self.workbook.sheet_by_index(sheet_no)
        
    def __call__(self):
        flag = False
        for row in range(self.sheet.nrows):
            if self.sheet.cell(row, 0).value == self.filter:
                s_index = row + 1
                flag = True
            elif flag and self.sheet.cell(row, 0).value == "END":
                e_index = row
                flag = False
                
        keys = [self.sheet.cell(s_index, col_index).value for col_index in range(self.sheet.ncols)]

        dict_list = []
        for row_index in range(s_index + 1, e_index):
            d = {keys[col_index]: self.sheet.cell(row_index, col_index).value 
                 for col_index in range(self.sheet.ncols)}
            d = {key: d[key] for key in [key for key in d.keys() if key ]}
            dict_list.append(d)
        return dict_list   



