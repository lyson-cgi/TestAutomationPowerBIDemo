import logging
import inspect
import pytest
import openpyxl

import os
from dotenv import load_dotenv

# This BaseClass need to have the knowledge of setup which is defined in the conftest.py
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
        load_dotenv()
        TEST_DATA_FILE_PATH = os.getenv('XLS_TEST_DATA_PATH')
        print("WORKBOOK: ", TEST_DATA_FILE_PATH)
        book = openpyxl.load_workbook(TEST_DATA_FILE_PATH)
        # book = openpyxl.load_workbook("C:\\Users\\Ly-sonLe\\Documents\\Github.com\\TestAutomationPowerBI\\utilities\\test_data.xlsx")
        book.active = 0 # first worksheet
        sheet = book.active
        print("Sheet Title:", sheet.title)
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
