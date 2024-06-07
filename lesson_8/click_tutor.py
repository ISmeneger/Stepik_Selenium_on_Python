import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.freeconferencecall.com/global/pl')

login_button = driver.find_element('xpath', '//a[@id="login-desktop"]')
login_button.click()

email_field = driver.find_element('xpath', '//input[@id="login_email"]')
# Проверяем, что в поле пусто
assert email_field.get_attribute("value") == ""
# Вводим логин в поле email
email_field.send_keys('email@yandex.ru')
# Записываем значение поля в переменную
email_field_value = email_field.get_attribute("value")
# Проверяем, что в поле email содержится введенный логин
assert "email@yandex.ru" in email_field_value
# print(email_field.get_attribute('maxlength'))
time.sleep(3)

email_field.clear()
# Проверяем, что в поле пусто
assert email_field.get_attribute("value") == ""

email_field.send_keys('Aaaaaaaaaaaaa')
# Проверяем что в поле First Name содержится введенное нами значение "Alexey"
assert "Aaaaaaaaaaaaa" in email_field.get_attribute("value")
time.sleep(3)
