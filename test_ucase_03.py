from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
import time

from pageObjects.HomePage import HomePage
import pytest

# Extend TestOne Class to inherit the BaseClass
# @pytest.mark.usefixtures("setup")
class TestUseCase03(BaseClass):
    def test_CheckContentPageTwo(self):
        log = self.getLogger()
        log.info("CheckContentPageTwo started")
        # looking for the element with the iframe that contains a specified string in a attribute src
        search_element = "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]"
        homePage = HomePage(self.driver)
        homePage.switch_to_iframe()

        #WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(
        #    (By.XPATH, "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]")))

        time.sleep(3)

        # goto Labour Market Outlook Highlights page
        #elem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
        #    (By.XPATH, '//*[@id="tabZoneId364"]/div/div/div/div/div/div')))

        homePage.labour_market_outlook_highlights_item().click()


        #time.sleep(1)

        #elem.click()
        time.sleep(3)
        log.info("CheckContentPageTwo ended")