import pytest

from selenium import webdriver

from .pages.Login_page import Login
from .pages.Inventory_page import Inventory
from .pages.Cart_page import Cart
from .pages.Your_info_page import Your_info_page
from .pages.Overview_page import Overview_page

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
service = Service(executable_path=GeckoDriverManager().install())


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=service)
    yield driver


# тест проверки интернет-магазина
def test_online_store(driver):

    # создать переменную равную классу Login
    login = Login(driver)

    # открыть страницу
    login.open_Login_page()

    # ввод логина
    login.Username()

    # ввод пароля
    login.Password()

    # нажатие кнопки входа Login
    login.login_button()

    # создать переменную равную классу Inventory
    inventory = Inventory(driver)

    # добавить в корзину
    inventory.add_to_cart()

    # зайти в корзину
    inventory.cart()

    # создать переменную равную классу Cart
    cart_page = Cart(driver)

    # нажать Checkout
    cart_page.checkout()

    # создать переменную равную классу Your_info_page
    your_info_page = Your_info_page(driver)

    # заполнить поля
    your_info_page.fill_out_fields()

    # создать переменную равную классу Overview_page
    overview_page = Overview_page(driver)

    # читаем цену
    overview_page.total()

    # закрыть браузер
    overview_page.quit()

    # Проверить (assert), что итоговая сумма равна $58.29
    result = overview_page.total()
    assert result == '$58.29'
