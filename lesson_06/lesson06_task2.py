from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

url = "http://uitestingplayground.com/textinput"
id_input_field = "newButtonName"
id_blue_button = "updatingButton"
browser.get(url)

input_text = browser.find_element(By.ID, id_input_field)
input_text.send_keys("SkyPro")

button = browser.find_element(By.ID, id_blue_button)
button.click()

updated_button_text = button.text

print(f'("{updated_button_text}")')

browser.quit()
