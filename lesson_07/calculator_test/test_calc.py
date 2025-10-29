import pytest
from selenium import webdriver
from .page.calculator_page import Calculator


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# тест проверки калькулятора
def test_calculator(driver):

    # создать экземпляр Page Object
    calculator = Calculator(driver)

    # открыть страницу
    calculator.open()

    # ввод значения времени - 45
    calculator.delay()

    # нажатие кнопок
    calculator.button()

    # результат
    calculator.check()
