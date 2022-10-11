from selenium import webdriver

#chrome driver must be used to invoke browser, cant be invoked directly without driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# These 3 lines assign driver path, assign driver object and invoke browser
#Use forwardslash with path to prevent error
service_obj = Service("C:/Users/thund/Documents/ChromeDriver/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice")

# ID, Xpath, CSSSelector, Classname, name, linktext
#Use these for identifying elements

#Use to locate element by name of element
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")

#Use to locate element by ID of element (prevents confusion of identfying multiple elements)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")

#Clicks on specified element(Checkbox in this case)
driver.find_element(By.ID, "exampleCheck1").click()
