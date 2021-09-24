from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
import time
import pytest

# Extend TestOne Class to inherit the BaseClass
# @pytest.mark.usefixtures("setup")
class TestHomePage(BaseClass):
    def test_OpenWebsite(self):
        log = self.getLogger()
        try:
            log.info("test_OpenWebsite started")
        except Exception as e:
            log.error("Could not find website")
        finally:
            log.info("test_OpenWebsite ended")

    def test_CheckTitle(self):
        log = self.getLogger()
        log.info("CheckTitle started")

        _title = self.driver.title
        _url = self.driver.current_url
        log.info("Current Title: " + _title)
        _dataDict = self.getTestData("Testcase01")
        print("thisDict: ", _dataDict)
        _chkStr = _dataDict['website_title']
        print("chkStr->", _chkStr)
        #_chkStr = "EMLI_POC_Sprint7_WIP_v3_sellenium test - Power BI"
        assert _chkStr in _title, "Incorrect title found"

        log.info("CheckTitle ended")

    def test_CheckUrl(self):
        log = self.getLogger()
        log.info("CheckUrl started")

        _url = self.driver.current_url
        _dataDict = self.getTestData("Testcase02")
        print("thisDict: ", _dataDict)
        _chkUrl = _dataDict["url"]
        #_chkUrl = "https://app.powerbi.com/groups/4af14a54-e4b2-46c3-83ab-ea11cc636a7a/reports/37d98bec-e44a-46c5-8096-3a83d4ed1e99/ReportSection0fe5bb62de4b8ad15778"
        log.info("Current Url: " + _url)
        assert _chkUrl in _url, "Incorrect Url found"

        log.info("CheckUrl ended")

    def test_VerifyReportTitle(self):
        log = self.getLogger()
        log.info("VerifyReportTitle started")
        _report_name = "NoW-MineType Region"
        _page_source = self.driver.page_source
        assert _report_name in _page_source

        log.info("CheckUrl ended")