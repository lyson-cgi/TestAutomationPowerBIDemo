import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: --browser_name"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    print("browser name:", browser_name)
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="c:\\webdriver\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="c:\\webdriver\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="c:\\webdriver\\msedgedriver.exe")
    else:
        driver = webdriver.Chrome(executable_path="c:\\webdriver\\chromedriver.exe")

    driver.get("https://app.powerbi.com/groups/4af14a54-e4b2-46c3-83ab-ea11cc636a7a/reports/37d98bec-e44a-46c5-8096-3a83d4ed1e99/ReportSection0fe5bb62de4b8ad15778")

    print("Sign In with Two Factor Authentication")

    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='mainContent']/section[1]/div[3]/div/a")))
    element.click() # Power BI SIGN IN button

    driver.find_element_by_name("loginfmt").send_keys("ly-son.le@cgi.com")
    time.sleep(1)
    driver.find_element_by_id("idSIButton9").click()  # Next button
    time.sleep(30)  # give user time to response on phone
    request.cls.driver = driver  # class driver
    print("Yield Started")
    yield
    print("Yield Ended")

    driver.close()
