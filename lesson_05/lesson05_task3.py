from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


driver.get('http://the-internet.herokuapp.com/inputs')
time.sleep(3)

field_Number = 'input[type="number"]'
input_field = driver.find_element(By.CSS_SELECTOR, field_Number)
input_field.send_keys("Sky")
time.sleep(3)

input_field.clear()
time.sleep(3)

input_field.send_keys("Pro")
time.sleep(3)

driver.quit()
