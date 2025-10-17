from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
time.sleep(3)

search_box = driver.find_element(By.XPATH, "//textarea[@title='Поиск']")
time.sleep(3)

search_box.send_keys("Selenium")
time.sleep(3)

search_box.send_keys(Keys.RETURN)
time.sleep(3)

driver.quit()
