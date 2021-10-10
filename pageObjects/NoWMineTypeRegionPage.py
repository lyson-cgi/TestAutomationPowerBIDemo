from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class NoWMineTypeRegionPage:
    def __init__(self, driver):
        self.driver = driver
        print("Constructor Invoked")

    def test_Testcase21(self):
        #log = self.getLogger()
        #log.info("checking for website title")

        title = self.driver.title
        value = self.getValue(self.getTestData("Testcase01"), 'website_title')

        assert value in title, "Incorrect page title found"

