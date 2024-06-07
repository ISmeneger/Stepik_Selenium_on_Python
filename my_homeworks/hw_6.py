import time
import os
import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920, 1080')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# # Задание 1. (Установка и чтение куки)
#
# driver.get('https://demoqa.com/')
#
# driver.add_cookie({
#     'name': 'username',
#     'value': 'user123'
# })
#
# driver.refresh()
# time.sleep(3)
# new_cookie = driver.get_cookie('username')
# print(new_cookie)
#
# # Задание 2. (Удаление куков)
#
# driver.get('https://whatismyipaddress.com/')
#
# print(driver.get_cookie('usprivacy'))
#
# cookie_no = driver.delete_cookie('usprivacy')
#
# driver.refresh()
# print(cookie_no)

# Задание 3. (Автоматизация корзины покупок)

driver.get('https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony')
time.sleep(10)
BUTTON_ADD = ('xpath', '(//a[contains(@class, "product-card__add-basket")])[1]')
BUTTON_GO_TO_BASKET = ('xpath', '(//a[contains(@class, "navbar-pc__link")])[3]')
BUTTON_DELETE_IN_TO_BASKET = ('xpath', '//button[@class="btn__del j-basket-item-del"]')

wait.until(EC.element_to_be_clickable(BUTTON_ADD)).click()
wait.until(EC.element_to_be_clickable(BUTTON_GO_TO_BASKET)).click()

time.sleep(5)

pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies_wb/cookies.pkl", "wb"))

time.sleep(5)

wait.until(EC.element_to_be_clickable(BUTTON_DELETE_IN_TO_BASKET)).click()

driver.delete_all_cookies()
time.sleep(20)
driver.refresh()

time.sleep(5)

cookies = pickle.load(open(os.getcwd()+"/cookies_wb/cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)

driver.refresh()

time.sleep(5)


