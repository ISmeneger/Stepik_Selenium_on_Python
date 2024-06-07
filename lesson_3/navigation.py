import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://yandex.ru')
time.sleep(10)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()
time.sleep(3)