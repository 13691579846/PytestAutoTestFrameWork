"""
------------------------------------
@Time : 2019/4/22 16:12
@Auth : linux超
@File : parseExcelFile.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from openpyxl import load_workbook
from config.conf import excelPath


class ParseExcel(object):

    def __init__(self):
        self.wk = load_workbook(excelPath)
        self.excelFile = excelPath

    def getSheetByName(self, sheetName):
        """获取sheet对象"""
        sheet = self.wk[sheetName]
        return sheet

    def getRowNum(self, sheet):
        """获取有效数据的最大行号"""
        return sheet.max_row

    def getColsNum(self, sheet):
        """获取有效数据的最大列号"""
        return sheet.max_column

    def getRowValues(self, sheet, rowNum):
        """获取某一行的数据"""
        maxColsNum = self.getColsNum(sheet)
        rowValues = []
        for colsNum in range(1, maxColsNum + 1):
            value = sheet.cell(rowNum, colsNum).value
            if value is None:
                value = ''
            rowValues.append(value)
        return tuple(rowValues)

    def getColumnValues(self, sheet, columnNum):
        """获取某一列的数据"""
        maxRowNum = self.getRowNum(sheet)
        columnValues = []
        for rowNum in range(2, maxRowNum + 1):
            value = sheet.cell(rowNum, columnNum).value
            if value is None:
                value = ''
            columnValues.append(value)
        return tuple(columnValues)

    def getValueOfCell(self, sheet, rowNum, columnNum):
        """获取某一个单元格的数据"""
        value = sheet.cell(rowNum, columnNum).value
        if value is None:
            value = ''
        return value

    def getAllValuesOfSheet(self, sheet):
        """获取某一个sheet页的所有测试数据，返回一个元祖组成的列表"""
        maxRowNum = self.getRowNum(sheet)
        columnNum = self.getColsNum(sheet)
        allValues = []
        for row in range(2, maxRowNum + 1):
            rowValues = []
            for column in range(1, columnNum + 1):
                value = sheet.cell(row, column).value
                if value is None:
                    value = ''
                rowValues.append(value)
            allValues.append(tuple(rowValues))
        return allValues


if __name__ == '__main__':
    # excel = ParseExcel()
    # sheet = excel.getSheetByName('login')
    # print('行号:', excel.getRowNum(sheet))
    # print('列号:', excel.getColsNum(sheet))
    #
    # rowvalues = excel.getRowValues(sheet, 1)
    # columnvalues = excel.getColumnValues(sheet, 2)
    # valueofcell = excel.getValueOfCell(sheet, 1, 2)
    # allvalues = excel.getAllValuesOfSheet(sheet)
    #
    # print('第{}行数据{}'.format(1, rowvalues))
    # print('第{}列数据{}'.format(2, columnvalues))
    # print('{}{}单元格的内容{}'.format(1, 2, valueofcell))
    # print('login{}'.format(allvalues))

    excel = ParseExcel()
    sheet = excel.getSheetByName('mail')
    print('行号:', excel.getRowNum(sheet))
    print('列号:', excel.getColsNum(sheet))

    allvalues = excel.getAllValuesOfSheet(sheet)

    print('sendmail{}'.format(allvalues))
