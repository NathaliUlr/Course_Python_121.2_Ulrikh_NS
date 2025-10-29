from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'

    # инициализация нового объекта класса
    def __init__(self, driver):
        self.driver = driver

    # открыть страницу
    def open(self):
        self.driver.get(self.url)

    # ввести значение для задержки
    def delay(self):
        Delay = self.driver.find_element(By.ID, 'delay')
        Delay.clear()
        Delay.send_keys(45)

    # нажать на кнопки калькулятора
    def button(self):
        Seven = self.driver.find_element(
            By.XPATH, ('//span[contains(text(), "7")]'))
        Seven.click()
        Plus = self.driver.find_element(
            By.XPATH, ('//span[contains(text(), "+")]'))
        Plus.click()
        Eight = self.driver.find_element(
            By.XPATH, ('//span[contains(text(), "8")]'))
        Eight.click()
        Still = self.driver.find_element(
            By.XPATH, ('//span[contains(text(), "=")]'))
        Still.click()

    # ожидание задержки
    def check(self):
        field_solution = self.driver.find_element(By.CLASS_NAME, 'screen')
        wait = WebDriverWait(self.driver, 45)
        wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'screen'), '15'))
        result = field_solution.text
        assert result == '15'
