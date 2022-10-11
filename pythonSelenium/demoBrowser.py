from selenium import webdriver

#chrome driver must be used to invoke browser, cant be invoked directly without driver
from selenium.webdriver.chrome.service import Service

# These 3 lines assign driver path, assign driver object and invoke browser
#Use forwardslash with path to prevent error
service_obj = Service("C:/Users/thund/Documents/ChromeDriver/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

#Opens browser with specific url
driver.get("https://rahulshettyacademy.com")

print(driver.title)
print(driver.current_url)

#Redirects to seleniumPractise page
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.minimize_window()
#Browser controls such as refresh and forward/previous page can be controlled with driver as well
driver.back()
driver.refresh()
driver.forward()
#Closes browser automatically
driver.close()