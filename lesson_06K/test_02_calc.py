from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_result_of_solving():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    browser.get(url)
    Delay = browser.find_element(By.ID, 'delay')
    Delay.clear()
    Delay.send_keys('45')
    Seven = browser.find_element(By.XPATH, ('//span[contains(text(), "7")]'))
    Seven.click()
    Plus = browser.find_element(By.XPATH, ('//span[contains(text(), "+")]'))
    Plus.click()
    Eight = browser.find_element(By.XPATH, ('//span[contains(text(), "8")]'))
    Eight.click()
    Still = browser.find_element(By.XPATH, ('//span[contains(text(), "=")]'))
    Still.click()
    field_solution = browser.find_element(By.CLASS_NAME, 'screen')
    wait = WebDriverWait(browser, 45)
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'screen'), '15'))
    result = field_solution.text
    assert result == '15'
    browser.quit
