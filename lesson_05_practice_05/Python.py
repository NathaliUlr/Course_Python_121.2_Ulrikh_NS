from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
time.sleep(3)

button_donat = driver.find_element(By.LINK_TEXT, "Donate")
button_donat.click()
time.sleep(3)

driver.quit()
