import time
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://vk.com/')
current_title = driver.title
print('Текущий заголовок страницы: ', current_title)

driver.get('https://yandex.ru')
current_title = driver.title
print('Текущий заголовок страницы: ', current_title)

time.sleep(5)

driver.back()
time.sleep(3)
url = driver.current_url
assert url == 'https://vk.com/', "Ошибка в url, открыта не та страница"

driver.refresh()
time.sleep(3)
print('url страницы: ', url)

driver.forward()
time.sleep(3)

url = driver.current_url
assert url == 'https://dzen.ru/?yredirect=true', "Ошибка в url, открыта не та страница"