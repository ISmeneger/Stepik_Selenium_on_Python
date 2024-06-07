import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# driver.get('https://www.freeconferencecall.com/en/us/login')

# Получение, удаление, довавление и замена куков

# print(driver.get_cookie('country_code'))

# print(driver.get_cookies())

# driver.add_cookie({
#     'name': 'Example',
#     'value': 'Kukushka'
# })
#
# print(driver.get_cookie('Example'))

# before = driver.get_cookie('split')
# print(before)
#
# driver.delete_cookie('split')
#
# driver.add_cookie({
#     'name': 'split',
#     'value': 'QWERTY'
# })
#
# after = driver.get_cookie('split')
# print(after)

# before = driver.get_cookies()
# print(before)
#
# driver.delete_all_cookies()
#
# driver.add_cookie({
#     'name': 'split',
#     'value': 'QWERTY'
# })
#
# after = driver.get_cookies()
# print(after)

# Сохранение куков в файл

# driver.get("https://www.freeconferencecall.com/en/us/login")
#
# LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")
#
# # Логинимся в аккаунт
# driver.get("https://www.freeconferencecall.com/en/us/login")
# driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("123")
# driver.find_element(*SUBMIT_BUTTON).click()
#
# # Сохраняем куки в файл
# pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies_wb.pkl", "wb"))

# Подгрузка куков из файла (авторизация через куки)
# Открываем страницу логина
driver.get("https://www.freeconferencecall.com/profile")

# Чистим все куки
driver.delete_all_cookies()

# Записываем куки из файла в переменную
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies_wb.pkl", "rb"))

# Добавляем по одной куке из списка
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)

# Делаем запрос на любую страницу залогиненного пользователя
driver.refresh()

time.sleep(5)