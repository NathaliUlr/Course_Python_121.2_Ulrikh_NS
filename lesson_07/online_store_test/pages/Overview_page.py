from selenium.webdriver.common.by import By


class Overview_page:

    # инициализация нового объекта класса
    def __init__(self, driver):
        self.driver = driver

    # читаем цену
    def total(self):
        total_element = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label')
        total_text = total_element.text
        total_text_c = total_text.replace("Total: ", "")
        return total_text_c

    # закрыть браузер
    def quit(self):
        self.driver.quit()
