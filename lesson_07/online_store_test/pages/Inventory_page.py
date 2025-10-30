from selenium.webdriver.common.by import By


class Inventory:

    # инициализация нового объекта класса
    def __init__(self, driver):
        self.driver = driver

    # добавление в корзину
    def add_to_cart(self):
        Sauce_Labs_Backpack = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack')
        Sauce_Labs_Backpack.click()
        Sauce_Labs_Bolt_T_Shirt = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        Sauce_Labs_Bolt_T_Shirt.click()
        Sauce_Labs_Onesie = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie')
        Sauce_Labs_Onesie.click()

    # перейти в корзину
    def cart(self):
        Shopping_cart = self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link')
        Shopping_cart.click()
