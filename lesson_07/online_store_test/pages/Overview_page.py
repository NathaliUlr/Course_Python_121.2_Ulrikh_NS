from selenium.webdriver.common.by import By


class Overview_page:

    # инициализация нового объекта класса
    def __init__(self, driver):
        self.driver = driver

    # читаем цену
    def total(self):
        Total = self.driver.find_element(By.CLASS_NAME, 'summary_total_label')
        self.total_amount = '$58.29'
        total_text = Total.text
        self.price = total_text.replace("Total: ", "")

    # закрыть браузер
    def quit(self):
        self.driver.quit()

    # Проверить (assert), что итоговая сумма равна $58.29
    def check(self):
        assert self.price == self.total_amount
