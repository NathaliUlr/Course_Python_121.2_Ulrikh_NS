from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
browser.get(url)

wait = WebDriverWait(browser, 10)

div = wait.until(EC.visibility_of_element_located((By.ID, 'image-container')))

img = wait.until(EC.presence_of_element_located((By.ID, 'award')))

print(img.get_attribute('src'))

browser.quit()
