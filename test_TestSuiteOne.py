from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
import time
import pytest
from pageObjects.NoWMineTypeRegionPage import NoWMineTypeRegionPage

# Extend TestOne Class to inherit the BaseClass
# @pytest.mark.usefixtures("setup")
class TestSuiteOne(BaseClass):
    #def test_OpenWebsite(self):
    #    log = self.getLogger()
    #    try:
    #        log.info("test_OpenWebsite started")
    #    except Exception as e:
    #        log.error("Could not find website")
    #    finally:
    #        log.info("test_OpenWebsite ended")


    def test_TestCase01(self):
        log = self.getLogger()
        log.info("checking for website title")

        title = self.driver.title
        value = self.getValue(self.getTestData("Testcase01"), 'website_title')

        assert value in title, "Incorrect page title found"


    def test_TestCase02(self):
        log = self.getLogger()
        log.info("checking for url")

        url = self.driver.current_url
        value = self.getValue(self.getTestData("Testcase02"), 'url')
        assert value in url, "Incorrect URL found"

    def test_TestCase03(self):
        log = self.getLogger()
        log.info("checking for report title 1")
        value = self.getValue(self.getTestData("Testcase03"), 'report_title')
        assert value in self.driver.page_source

    def test_TestCase04(self):
        log = self.getLogger()
        log.info("checking for report title 2")
        value = self.getValue(self.getTestData("Testcase04"), 'report_title')
        assert value in self.driver.page_source

    def test_TestCase05(self):
        log = self.getLogger()
        log.info("checking for report title 3")
        value = self.getValue(self.getTestData("Testcase05"), 'report_title')
        assert value in self.driver.page_source

    def test_TestCase06(self):
        log = self.getLogger()
        log.info("checking for report title 4")
        value = self.getValue(self.getTestData("Testcase06"), 'report_title')
        assert value in self.driver.page_source

    def test_TestCase07(self):
        log = self.getLogger()
        log.info("checking for report title 5")
        value = self.getValue(self.getTestData("Testcase05"), 'report_title')
        assert value in self.driver.page_source

    def test_TestCase08(self):
        log = self.getLogger()
        log.info("checking for report title 6")
        value = self.getValue(self.getTestData("Testcase08"), 'report_title')
        assert value in self.driver.page_source

    def test_TestCase09(self):
        log = self.getLogger()
        log.info("checking for report title 7")
        value = self.getValue(self.getTestData("Testcase09"), 'report_title')
        assert value in self.driver.page_source

    def test_TestCase10(self):
        log = self.getLogger()
        log.info("checking for report title 8")
        value = self.getValue(self.getTestData("Testcase10"), 'report_title')
        assert value in self.driver.page_source

    def test_TestCase11(self):
        log = self.getLogger()
        log.info("checking for report title 9")
        value = self.getValue(self.getTestData("Testcase11"), 'report_title')
        assert value in self.driver.page_source

    def test_TestCase12(self):
        log = self.getLogger()
        log.info("checking for report title 10")
        value = self.getValue(self.getTestData("Testcase12"), 'report_title')
        assert value in self.driver.page_source


    def test_TestCase21(self):
        page2Object = NoWMineTypeRegionPage(self.driver)
        page2Object.test_Testcase21()
