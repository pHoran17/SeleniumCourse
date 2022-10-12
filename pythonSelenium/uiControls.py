from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver must be used to invoke browser, cant be invoked directly without driver

from selenium.webdriver.common.by import By

# These 3 lines assign driver path, assign driver object and invoke browser
#Use forwardslash with path to prevent error
service_obj = Service("C:/Users/thund/Documents/ChromeDriver/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#Opens page of various UI elements such as radio buttons, checkboxes and dropdown lists
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Gets list of checkbox elements on page
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

#Gets list of radio buttons
radios = driver.find_elements(By.XPATH, "//input[@type='radio']")

print(len(checkboxes))

#Loop goes through each checkbox element, triggering only the checkbox element with option2 as its value
#Assert checks that box is checked
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

#Loop for iterating through list of radio buttons, only activiating the radio button with value of radio2
for rButton in radios:
    if rButton.get_attribute("value") == "radio2":
        rButton.click()
        assert rButton.is_selected()
        break

#Loop unecessary as radio buttons arent dynamic here
radios[2].click()
assert radios[2].is_selected()

#Checks if text element is displayed before and after it is hidden
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()