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
    def delay(self, time):
        Delay = self.driver.find_element(By.ID, 'delay')
        Delay.clear()
        Delay.send_keys(time)

    # нажать на кнопки калькулятора
    def button(self, text):
        buttons = self.driver.find_elements(
            By.XPATH, f"//button[text()='{text}'] | //span[text()='{text}']")
        for button in buttons:
            if button.text == text:
                button.click()
                return
            raise ValueError(f'Кнопка {text} не найдена')

    # ожидание задержки
    def result(self, timeout):
        field_solution = self.driver.find_element(By.CLASS_NAME, 'screen')
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'screen'), '15'))
        return field_solution.text
