import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.wikipedia.org/')

url = driver.current_url
print('url страницы: ', url)
assert url == 'https://www.wikipedia.org/', "Ошибка в url, открыта не та страница"

current_title = driver.title
print('Текущий заголовок страницы: ', current_title)
assert current_title == 'Wikipedia', "Некорретный заголовок страницы"

print(driver.page_source)

time.sleep(3)
