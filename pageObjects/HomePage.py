from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    # sign_in = (By.XPATH, "//*[@id='mainContent']/section[1]/div[3]/div/a")
    labour_market_outlook_highlights = (By.XPATH, "//*[@id='tabZoneId364']/div/div/div/div/div/div")
    iframe = (By.XPATH, "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]")
    def __init__(self, driver):
        self.driver = driver
        print("Constructor Invoked")

    def switch_to_iframe(self):
        #elem = WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(
        #    (By.XPATH, "//iframe[contains(@src,'LMO_Tool_Sprint2_Demo')]")))
        elem = WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(
            self.iframe))
        return elem

    # to Labour Market Outlook Highlights page
    def labour_market_outlook_highlights_item(self):
        elem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            self.labour_market_outlook_highlights))

        #elem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
        #    (By.XPATH, '//*[@id="tabZoneId364"]/div/div/div/div/div/div')))
        return elem

