import selenium
from utilities.BaseClass import BaseClass

print("Selenium Version: ", selenium.__version__)
base_class = BaseClass()
thisDict = (base_class.getTestData("Testcase20"))
print(thisDict)
print(thisDict['website_title'])
