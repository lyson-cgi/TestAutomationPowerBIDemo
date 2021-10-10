import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

driver = None
userLoggedIn = False
import time
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: --browser_name"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    global userLoggedIn
    browser_name = request.config.getoption("browser_name")
    print("browser name:", browser_name)
    load_dotenv()
    WEBDRIVER_PATH = os.getenv('WEBDRIVER_PATH')
    POWERBI_URL = os.getenv('POWERBI_URL')

    if browser_name == "chrome":
        # driver = webdriver.Chrome(executable_path="c:\\webdriver\\chromedriver.exe")
        driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH + "\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=WEBDRIVER_PATH + "\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path=WEBDRIVER_PATH + "\\msedgedriver.exe")
    else:
        driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH + "\\chromedriver.exe")
    if not userLoggedIn:
        #driver.get("https://app.powerbi.com/groups/4af14a54-e4b2-46c3-83ab-ea11cc636a7a/reports/37d98bec-e44a-46c5-8096-3a83d4ed1e99/ReportSection0fe5bb62de4b8ad15778")
        driver.get(POWERBI_URL)


        print("Sign In with Two Factor Authentication")

        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='mainContent']/section[1]/div[3]/div/a")))
        element.click() # Power BI SIGN IN button
        time.sleep(3)  # give user time to response on phone

        driver.find_element_by_name("loginfmt").send_keys("ly-son.le@cgi.com")
        time.sleep(1)
        driver.find_element_by_id("idSIButton9").click()  # Next button

        time.sleep(25)  # give user time to response on phone


        #WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        #        (By.ID, "idSIButton9"))).click()  # Yes button
        # driver.find_element_by_id("idSIButton9").click()  # Next button
        #time.sleep(30)
        userLoggedIn = True
        driver.maximize_window()

    request.cls.driver = driver  # class driver

    print("Yield Started")
    yield
    print("Yield Ended")

    driver.close()
