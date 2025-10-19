from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


driver.get('http://the-internet.herokuapp.com/login')

Username_field = driver.find_element(By.ID, "username")
Username_field.send_keys("tomsmith")
time.sleep(5)

Password_field = driver.find_element(By.ID, "password")
Password_field.send_keys("SuperSecretPassword!")
time.sleep(5)

Login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
Login_button.click()
time.sleep(5)

message = driver.find_element(By.ID, "flash")
success_message_text = message.text
print("Текст с зеленой плашки:", success_message_text)

driver.quit()
