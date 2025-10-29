from selenium.webdriver.common.by import By


class Cart:

    # инициализация нового объекта класса
    def __init__(self, driver):
        self.driver = driver

    # нажать Checkout
    def checkout(self):
        Checkout = self.driver.find_element(By.ID, 'checkout')
        Checkout.click()
