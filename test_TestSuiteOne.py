# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
        log.info("checking for page title 1")
        value = self.getValue(self.getTestData("Testcase03"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase04(self):
        log = self.getLogger()
        log.info("checking for page title 2")
        value = self.getValue(self.getTestData("Testcase04"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase05(self):
        log = self.getLogger()
        log.info("checking for page title 3")
        value = self.getValue(self.getTestData("Testcase05"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase06(self):
        log = self.getLogger()
        log.info("checking for page title 4")
        value = self.getValue(self.getTestData("Testcase06"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase07(self):
        log = self.getLogger()
        log.info("checking for page title 5")
        value = self.getValue(self.getTestData("Testcase05"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase08(self):
        log = self.getLogger()
        log.info("checking for page title 6")
        value = self.getValue(self.getTestData("Testcase08"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase09(self):
        log = self.getLogger()
        log.info("checking for page title 7")
        value = self.getValue(self.getTestData("Testcase09"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase10(self):
        log = self.getLogger()
        log.info("checking for page title 8")
        value = self.getValue(self.getTestData("Testcase10"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase11(self):
        log = self.getLogger()
        log.info("checking for page title 9")
        value = self.getValue(self.getTestData("Testcase11"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase12(self):
        log = self.getLogger()
        log.info("checking for page title 10")
        value = self.getValue(self.getTestData("Testcase12"), 'page_title')
        assert value in self.driver.page_source

    def test_TestCase13(self):
        log = self.getLogger()

        value = self.getValue(self.getTestData("Testcase13"), 'page_link')
        log.info("checking link to " + value)
        xpath = "//span[@title='" + value + "']"
        self.navToPage(xpath)
        #elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
        #    (By.XPATH, xpath)))
        #       (By.XPATH, '//span[@title="Application Status"]')))
        #             '//*[@id="content"]/report/exploration-container/div/exploration-fluent-navigation/mat-list/ul/li[2]/mat-list-item/div/div[3]/span')))

        #elem.click()
        #time.sleep(1)
        assert value in self.driver.page_source

    def test_TestCase14(self):
        log = self.getLogger()

        value = self.getValue(self.getTestData("Testcase14"), 'page_link')
        log.info("checking link to " + value)
        xpath = "//span[@title='" + value + "']"
        self.navToPage(xpath)
        # elem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
        #        (By.XPATH, xpath)))
        # elem.click()
        # time.sleep(1)
        assert value in self.driver.page_source

    def test_TestCase15(self):
        log = self.getLogger()

        value = self.getValue(self.getTestData("Testcase15"), 'page_link')
        log.info("checking link to " + value)
        xpath = "//span[@title='" + value + "']"
        self.navToPage(xpath)
        # elem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
        #        (By.XPATH, xpath)))
        # elem.click()
        #time.sleep(1)
        assert value in self.driver.page_source

    def test_TestCase16(self):
        log = self.getLogger()

        value = self.getValue(self.getTestData("Testcase16"), 'page_link')
        log.info("checking link to " + value)
        xpath = "//span[@title='" + value + "']"
        self.navToPage(xpath)
        # elem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
        #         (By.XPATH, xpath)))
        #elem.click()
        #time.sleep(1)
        assert value in self.driver.page_source

    def test_TestCase17(self):
        log = self.getLogger()

        value = self.getValue(self.getTestData("Testcase17"), 'page_link')
        log.info("checking link to " + value)
        xpath = "//span[@title='" + value + "']"
        self.navToPage(xpath)
        # elem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
        #        (By.XPATH, xpath)))
        # elem.click()
        # time.sleep(1)
        assert value in self.driver.page_source

    def test_TestCase18(self):
        log = self.getLogger()

        value = self.getValue(self.getTestData("Testcase18"), 'page_link')
        xpath = "//span[@title='" + value + "']"
        log.info("checking link to " + value)
        self.navToPage(xpath)
        # elem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
        #        (By.XPATH, xpath)))
        #elem.click()
        #time.sleep(1)
        assert value in self.driver.page_source

    def test_TestCase19(self):
        log = self.getLogger()

        value = self.getValue(self.getTestData("Testcase19"), 'page_link')
        assert_value = self.getValue(self.getTestData("Testcase19"), 'assert_name')
        xpath = "//span[@title='" + value + "']"
        log.info("assert value: " + assert_value)
        log.info("xpath: " + xpath)
        self.navToPage(xpath)
        assert assert_value in self.driver.page_source

    def test_TestCase20(self):
        log = self.getLogger()
        value = self.getValue(self.getTestData("Testcase20"), 'page_link')
        assert_value = self.getValue(self.getTestData("Testcase20"), 'assert_name')
        xpath = "//span[@title='" + value + "']"
        log.info("assert value: " + assert_value)
        log.info("xpath: " + xpath)
        self.navToPage(xpath)
        assert assert_value in self.driver.page_source

    def test_TestCase21(self):
        log = self.getLogger()

        value = self.getValue(self.getTestData("Testcase21"), 'page_link')
        assert_value = self.getValue(self.getTestData("Testcase21"), 'assert_name')
        xpath = "//span[@title='" + value + "']"
        log.info("assert value: " + assert_value)
        log.info("xpath: " + xpath)
        self.navToPage(xpath)

        assert assert_value in self.driver.page_source

    def test_TestCase22(self):
        log = self.getLogger()
        value = self.getValue(self.getTestData("Testcase22"), 'page_link')
        assert_value = self.getValue(self.getTestData("Testcase22"), 'assert_name')
        xpath = "//span[@title='" + value + "']"
        log.info("assert value: " + assert_value)
        log.info("xpath: " + xpath)
        self.navToPage(xpath)
        assert assert_value in self.driver.page_source

    def test_TestCase23(self):
        log = self.getLogger()
        value = self.getValue(self.getTestData("Testcase23"), 'follow_link')
        assert_value = self.getValue(self.getTestData("Testcase23"), 'assert_name')
        # $x("//div[contains(text(),'Compare Permit Application Types')]/parent::div/parent::div/parent::div/parent::div/parent::div")
        #xpath = "//div[contains(text(),'Compare Permit Application Types')]/parent::div/parent::div/parent::div/parent::div/parent::div"
        xpath = "//*[@class='tileSVG']"
        log.info("assert value: " + assert_value)
        log.info("xpath: " + xpath)
        self.navToClickable(xpath)
        time.sleep(3)
        assert assert_value in self.driver.page_source

    def test_TestCase24(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase24"), 'follow_link')
            assert_value = self.getValue(self.getTestData("Testcase24"), 'assert_name')
            xpath = "//*[@class='tileSVG']"
            log.info("assert value: " + assert_value)
            log.info("xpath: " + xpath)
            self.navToClickable(xpath)
            time.sleep(3)
            assert assert_value in self.driver.page_source

    def test_TestCase25(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase25"), 'filter')
            assert_value = self.getValue(self.getTestData("Testcase25"), 'assert_name')
            xpath = "//*[contains(text(),'" + value + "')]"

            log.info("assert value: " + assert_value)
            log.info("xpath: " + xpath)
            self.navToClickable(xpath)
            time.sleep(3)
            assert assert_value in self.driver.page_source

    def test_TestCase26(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase26"), 'filter')
            assert_value = self.getValue(self.getTestData("Testcase26"), 'assert_name')
            xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            log.info("xpath: " + xpath)
            self.navToClickable(xpath)
            time.sleep(3)
            assert assert_value in self.driver.page_source
            self.navToClickable(xpath)

    def test_TestCase27(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase27"), 'filter')
            assert_value = self.getValue(self.getTestData("Testcase27"), 'assert_name')
            xpath = "//*[contains(text(),'" + value + "')]"

            log.info("assert value: " + assert_value)
            log.info("xpath: " + xpath)
            self.navToClickable(xpath)
            time.sleep(3)
            assert assert_value in self.driver.page_source
            self.navToClickable(xpath)

    def test_TestCase28(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase28"), 'filter')
            assert_value = self.getValue(self.getTestData("Testcase28"), 'assert_name')
            xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            log.info("xpath: " + xpath)
            self.navToClickable(xpath)
            time.sleep(5)
            assert assert_value in self.driver.page_source
            self.navToClickable(xpath)

    def test_TestCase29(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase29"), 'filter')
            assert_value = self.getValue(self.getTestData("Testcase29"), 'assert_name')
            xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            # log.info("xpath: " + xpath)
            # self.navToClickable(xpath)
            # time.sleep(3)
            assert assert_value in self.driver.page_source

    def test_TestCase30(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase30"), 'filter')
            assert_value = self.getValue(self.getTestData("Testcase30"), 'assert_name')
            #xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            #log.info("xpath: " + xpath)
            #self.navToClickable(xpath)
            #time.sleep(3)
            assert assert_value in self.driver.page_source

    def test_TestCase31(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase31"), 'filter')
            assert_value = self.getValue(self.getTestData("Testcase31"), 'assert_name')
            # xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            # log.info("xpath: " + xpath)
            # self.navToClickable(xpath)
            # time.sleep(3)
            assert assert_value in self.driver.page_source

    def test_TestCase32(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase32"), 'filter')
            assert_value = self.getValue(self.getTestData("Testcase32"), 'assert_name')
            # xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            # log.info("xpath: " + xpath)
            # self.navToClickable(xpath)
            #time.sleep(3)
            assert assert_value in self.driver.page_source

    def test_TestCase33(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase33"), 'filter')
            assert_value = self.getValue(self.getTestData("Testcase33"), 'assert_name')
            # xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            # log.info("xpath: " + xpath)
            # self.navToClickable(xpath)
            # time.sleep(3)
            assert assert_value in self.driver.page_source

    def test_TestCase34(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase34"), 'visual')
            assert_value = self.getValue(self.getTestData("Testcase34"), 'assert_name')
            # xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            # log.info("xpath: " + xpath)
            # self.navToClickable(xpath)
            # time.sleep(3)
            assert assert_value in self.driver.page_source

    def test_TestCase35(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase35"), 'visual')
            assert_value = self.getValue(self.getTestData("Testcase35"), 'assert_name')
            # xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            # log.info("xpath: " + xpath)
            # self.navToClickable(xpath)
            # time.sleep(3)
            assert assert_value in self.driver.page_source

    def test_TestCase36(self):
            log = self.getLogger()
            value = self.getValue(self.getTestData("Testcase36"), 'visual')
            assert_value = self.getValue(self.getTestData("Testcase36"), 'assert_name')
            # xpath = "//*[contains(text(),'" + value + "')]"

            # log.info("assert value: " + assert_value)
            # log.info("xpath: " + xpath)
            # self.navToClickable(xpath)
            # time.sleep(3)
            assert assert_value in self.driver.page_source