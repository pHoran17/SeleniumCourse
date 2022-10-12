import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver must be used to invoke browser, cant be invoked directly without driver

from selenium.webdriver.common.by import By

# These 3 lines assign driver path, assign driver object and invoke browser
#Use forwardslash with path to prevent error
service_obj = Service("C:/Users/thund/Documents/ChromeDriver/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
#Time package used for waiting specified amount of time
time.sleep(2)

#Creates list of all countries from dropdown list after previously declared characters are entered in the autosuggest field
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
#Prints number of returned countries containing 'ind'
print(len(countries))

#Loop that iterates through list of countries and clicks on element if the text is the country India
for country in countries:
    if country.text == "India":
        country.click()
        break

#print(driver.find_element(By.ID, "autosuggest").text) This didnt work, below line will
#Use get_attribute to extract text from dynamic texts
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
