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
        book = openpyxl.load_workbook("C:\\Users\\ly-son.le\\Documents\\GitHub\\TestAutomationPowerBI\\utilities\\test_data.xlsx")
        book.active = 0 # first worksheet
        sheet = book.active
        # print("Sheet Title:", sheet.title)
        # print("Test Case ID: ", test_case_id)
        # print("Max Row:", sheet.max_row)
        # print("Max Column:", sheet.max_column)

        Dict = {}

        for i in range(2, sheet.max_row+1):  # to get rows
            if sheet.cell(row=i, column=1).value == test_case_id:
               _name = sheet.cell(row=i, column=2).value
               _value = sheet.cell(row=i, column=3).value
               Dict[_name] = _value
        return Dict

    def getValue(self, dict, name):
        return dict[name]
