from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
import time
import pytest

# Extend TestOne Class to inherit the BaseClass
# @pytest.mark.usefixtures("setup")
class TestUseCase02(BaseClass):
    def test_CheckContentTestCase01(self):
        log = self.getLogger()
        log.info("CheckContentTestCase01 started")

        # looking for the element with the iframe that contains a specified string in a attribute src
        #_search_element = "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]"

        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]")))
        _page_source = self.driver.page_source

        assert "Labour Market Outlook Highlights" in _page_source, "Missing Labour Market Outlook sHighlights"

        log.info("CheckContentPageOne ended")

    def test_CheckContentTestCase02(self):
        log = self.getLogger()
        log.info("CheckContentTestCase02 started")

        # looking for the element with the iframe that contains a specified string in a attribute src
        #_search_element = "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]"
        #WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(
        #        (By.XPATH, "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]")))

        _page_source = self.driver.page_source
        _chkStr = "Regional Highlights"
        assert _chkStr in _page_source, "Missing " + _chkStr

        log.info("CheckContentTestCase02 ended")

    def test_CheckContentTestCase03(self):
        log = self.getLogger()
        log.info("CheckContentTestCase03 started")

        _page_source = self.driver.page_source
        _chkStr = "High Opportunity Occupations"
        assert _chkStr in _page_source, "Missing " + _chkStr

        log.info("CheckContentTestCase03 ended")




    def test_CheckContentTestCase4(self):
        log = self.getLogger()
        log.info("CheckContentTestCase04 started")

        _page_source = self.driver.page_source
        _chkStr = "Industry Outlook"
        assert _chkStr in _page_source, "Missing " + _chkStr

        log.info("CheckContentTestCase04 ended")

    def test_CheckContentTestCase05(self):
        log = self.getLogger()
        log.info("CheckContentTestCase05 started")

        _page_source = self.driver.page_source
        _chkStr = "Occupational Outlook"
        assert _chkStr in _page_source, "Missing " + _chkStr

        log.info("CheckContentTestCase05 ended")

    def test_CheckContentTestCase06(self):
        log = self.getLogger()
        log.info("CheckContentTestCase06 started")

        _page_source = self.driver.page_source
        _chkStr = "Annual Highlights"
        _found = False
        _elem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="tabZoneId5"]/div/div/div/div/div/div')))
        print(_elem.text)

        assert _chkStr == _elem.text
        #    WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(
        #        (By.XPATH, "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]")))
        # // *[ @ id = "tabZoneId5"] / div / div / div / div / div / div
        log.info("CheckContentTestCase06 ended")
    # def test_CheckContentPageTwo(self):
    #    # looking for the element with the iframe that contains a specified string in a attribute src
    #    search_element = "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]"
    #
    #    WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(
    #        (By.XPATH, "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]")))
    #
    #    elem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
    #        (By.XPATH, '//*[@id="tabZoneId364"]/div/div/div/div/div/div')))
    #
    #    elem.click()
    #    time.sleep(5)
    #    log = self.getLogger()
    #    log.info("I am here testing log info")