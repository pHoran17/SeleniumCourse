from selenium import webdriver

#chrome driver must be used to invoke browser, cant be invoked directly without driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# These 3 lines assign driver path, assign driver object and invoke browser
#Use forwardslash with path to prevent error
service_obj = Service("C:/Users/thund/Documents/ChromeDriver/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")

#Use case sensitive text when using LINK_TEXT as means of finding element (hardcode)
#This will lead to new page with form for entering new password
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#XPATH used to navigate to input field contained within the form for entering email
#If done using CSS use spaces instead of / and :(index) instead of [index]
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@123")

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()




