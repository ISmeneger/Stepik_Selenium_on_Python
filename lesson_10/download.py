import os
import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# Инициализируем опции
prefs = {
    "download.default_directory": f"{os.getcwd()}\\downloads"
}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options)

# Открываем страницу для скачивания файлов
driver.get('https://the-internet.herokuapp.com/download')

time.sleep(3)

# Найдем все элементы и кликнем на любой
driver.find_elements('xpath', '//a')[3].click()

time.sleep(3)