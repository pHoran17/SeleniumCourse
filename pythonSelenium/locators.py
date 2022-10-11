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

#Custom XPATH, used for identifying elements with specified attributes
# //tagname[@attribute='value'] -> //input[@type='submit']

#Finds element by Css element (input field with name in this case), inputs Paddy into Name input field
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Paddy")

#This will submit the form by clicking on the element with a type of submit
driver.find_element(By.XPATH, "//input[@type='submit']").click()


#Text returned by alert from submitting form is stored in string variable here
message = driver.find_element(By.CLASS_NAME, "alert-success").text

#Message variable printed here
print(message)

#Checks if characters Success are present in the variable message
assert "Success" in message
#Line below triggers error as condition is not met
#assert "Suc1cess" in message