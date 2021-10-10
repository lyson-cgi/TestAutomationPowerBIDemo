from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        print("Constructor Invoked")



