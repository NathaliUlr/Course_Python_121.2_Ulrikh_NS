from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get('http://uitestingplayground.com/classattr')
time.sleep(5)
blue_button = '.btn-primary'
search_input = driver.find_element(By.CSS_SELECTOR, blue_button)
search_input.click()
time.sleep(5)
