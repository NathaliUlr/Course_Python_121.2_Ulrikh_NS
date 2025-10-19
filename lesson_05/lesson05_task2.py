from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get('http://uitestingplayground.com/dynamicid')
time.sleep(5)
button_name = "//button[text()='Button with Dynamic ID']"
button = driver.find_element(By.XPATH, button_name)
button.click()
time.sleep(5)
