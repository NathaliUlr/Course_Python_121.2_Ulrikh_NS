from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

url = "http://uitestingplayground.com/ajax"
expected_text = "Data loaded with AJAX get request."

browser.get(url)

wait = WebDriverWait(browser, 15)

button = browser.find_element(By.ID, "ajaxButton")
button.click()

wait.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, ".bg-success"), expected_text))

ajax_text = browser.find_element(By.CSS_SELECTOR, ".bg-success").text

print(ajax_text)

browser.quit()
