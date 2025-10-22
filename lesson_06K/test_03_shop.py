from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


def test_final_cost():

    service = Service(executable_path=GeckoDriverManager().install())
    browser = webdriver.Firefox(service=service)

    url = 'https://www.saucedemo.com/'
    browser.get(url)

    Username = browser.find_element(By.ID, 'user-name')
    Username.clear()
    Username.send_keys('standard_user')

    Password = browser.find_element(By.ID, 'password')
    Password.clear()
    Password.send_keys('secret_sauce')

    Login = browser.find_element(By.ID, 'login-button')
    Login.click()

    Sauce_Labs_Backpack = browser.find_element(
        By.ID, 'add-to-cart-sauce-labs-backpack')
    Sauce_Labs_Backpack.click()

    Sauce_Labs_Bolt_T_Shirt = browser.find_element(
        By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    Sauce_Labs_Bolt_T_Shirt.click()

    Sauce_Labs_Onesie = browser.find_element(
        By.ID, 'add-to-cart-sauce-labs-onesie')
    Sauce_Labs_Onesie.click()

    Shopping_cart = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
    Shopping_cart.click()

    Checkout = browser.find_element(By.ID, 'checkout')
    Checkout.click()

    First_name = browser.find_element(By.ID, 'first-name')
    First_name.send_keys('Наталья')

    Last_name = browser.find_element(By.ID, 'last-name')
    Last_name.send_keys('Ульрих')

    Postal_cod = browser.find_element(By.ID, 'postal-code')
    Postal_cod.send_keys('625000')

    Continue = browser.find_element(By.ID, 'continue')
    Continue.click()

    Total = browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total_amount = '$58.29'

    total_text = Total.text
    price = total_text.replace("Total: ", "")

    browser.quit()

    assert price == total_amount
