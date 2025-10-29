from selenium.webdriver.common.by import By


class Your_info_page:

    # инициализация нового объекта класса
    def __init__(self, driver):
        self.driver = driver

    # заполнить личные данные
    def fill_out_fields(self):
        First_name = self.driver.find_element(By.ID, 'first-name')
        First_name.send_keys('Наталья')
        Last_name = self.driver.find_element(By.ID, 'last-name')
        Last_name.send_keys('Ульрих')
        Postal_cod = self.driver.find_element(By.ID, 'postal-code')
        Postal_cod.send_keys('625000')
        Continue = self.driver.find_element(By.ID, 'continue')
        Continue.click()
