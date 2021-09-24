import logging
import inspect
import pytest
import openpyxl
# This BaseClass need to have the knowledge of setup which is define in the conftest.py
@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        #logger = logging.getLogger(__name__)
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def getTestData(self, test_case_id):
        book = openpyxl.load_workbook("C:\\Users\\Ly-sonLe\\Documents\\Github.com\\AutomateTestPowerBI\\utilities\\test_data.xlsx")
        book.active = 0 # first worksheet
        sheet = book.active
        print("Sheet Title:", sheet.title)
        print("Test Case ID: ", test_case_id)
        print("Max Row:", sheet.max_row)
        print("Max Column:", sheet.max_column)

        Dict = {}
        curLabel = sheet.cell(row=1, column=2).value
        curVal = sheet.cell(row=2, column=2).value
        print("value ", curVal)
        print("label ", curLabel)

        for i in range(2, sheet.max_row+1):  # to get rows
            curLabel = sheet.cell(row=i-1, column=2).value
            curVal = sheet.cell(row=i, column=2).value
            curTestCase = sheet.cell(row=i, column=1).value
            if sheet.cell(row=i, column=1).value == test_case_id:

                for j in range(2, sheet.max_column+1): # get column
                    print("inside test case")
                    Dict[sheet.cell(row=i-1, column=j).value] = sheet.cell(row=i, column=j).value
        return Dict
