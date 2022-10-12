from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver must be used to invoke browser, cant be invoked directly without driver

from selenium.webdriver.common.by import By

# These 3 lines assign driver path, assign driver object and invoke browser
#Use forwardslash with path to prevent error
name = "Stu"
service_obj = Service("C:/Users/thund/Documents/ChromeDriver/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#Opens page of various UI elements such as radio buttons, checkboxes and dropdown lists
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Inputs previously declared name variable
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)

#
driver.find_element(By.ID, "alertbtn").click()

#Must be used when handling alert popups on web browser as alerts are not HTML/CSS elements
alert = driver.switch_to.alert

#Alert text must be assigned to variable to be printed, doing this directly will cause a crash
alertText = alert.text

print(alertText)
assert name in alertText
#Autoclicks Ok on alert
alert.accept()

#Autoclicks on cancel prompt for alert where relevant
#alert.dismiss()
