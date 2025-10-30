from selenium.webdriver.common.by import By


class Login:

    url = 'https://www.saucedemo.com/'

    # инициализация нового объекта класса
    def __init__(self, driver):
        self.driver = driver

    # открыть страницу Login_page
    def open_Login_page(self):
        self.driver.get(self.url)

    # ввод логина
    def Username(self):
        Username = self.driver.find_element(By.ID, 'user-name')
        Username.clear()
        Username.send_keys('standard_user')

    # ввод пароля
    def Password(self):
        Password = self.driver.find_element(By.ID, 'password')
        Password.clear()
        Password.send_keys('secret_sauce')

    # нажатие кнопки входа Login
    def login_button(self):
        Login = self.driver.find_element(By.ID, 'login-button')
        Login.click()
