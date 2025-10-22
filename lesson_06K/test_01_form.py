from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By


def test_field_color():
    edge_driver_path = r"C:\Program Files (x86)\Microsoft\msedgedriver.exe"
    browser = webdriver.Edge(service=EdgeService(edge_driver_path))

    url = 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
    browser.get(url)

    First_name = browser.find_element(By.NAME, 'first-name')
    First_name.send_keys('Иван')

    Last_name = browser.find_element(By.NAME, 'last-name')
    Last_name.send_keys('Петров')

    Address = browser.find_element(By.NAME, 'address')
    Address.send_keys('Ленина, 55-3')

    E_mail = browser.find_element(By.NAME, 'e-mail')
    E_mail.send_keys('test@skypro.com')

    Phone_number = browser.find_element(By.NAME, 'phone')
    Phone_number.send_keys('+7985899998787')

    Zip_code = browser.find_element(By.NAME, 'zip-code')
    Zip_code.send_keys('')

    City = browser.find_element(By.NAME, 'city')
    City.send_keys('Москва')

    Country = browser.find_element(By.NAME, 'country')
    Country.send_keys('Россия')

    Job_position = browser.find_element(By.NAME, 'job-position')
    Job_position.send_keys('QA')

    Company = browser.find_element(By.NAME, 'company')
    Company.send_keys('SkyPro')

    Submit_button = browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    Submit_button.click()

    red = 'rgb(245, 194, 199)'
    green = 'rgb(186, 219, 204)'

    zip_code_field = browser.find_element(By.ID, 'zip-code')

    zip_code_color = zip_code_field.value_of_css_property('border-color')

    assert zip_code_color == red

    other_fields = [
        browser.find_element(By.ID, 'first-name'),
        browser.find_element(By.ID, 'last-name'),
        browser.find_element(By.ID, 'address'),
        browser.find_element(By.ID, 'e-mail'),
        browser.find_element(By.ID, 'phone'),
        browser.find_element(By.ID, 'city'),
        browser.find_element(By.ID, 'country'),
        browser.find_element(By.ID, 'job-position'),
        browser.find_element(By.ID, 'company')
    ]

    fields_to_check = other_fields
    for field in fields_to_check:
        assert field.value_of_css_property('border-color') == green

    browser.quit
