import os
import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

# driver.get('https://the-internet.herokuapp.com/upload')
#
# time.sleep(3)
#
# upload_field = driver.find_element('xpath', '//input[@type="file"]')
# upload_field.send_keys(f'{os.getcwd()}\\downloads\\STE In Banner.jpg')
#
# time.sleep(3)

driver.get(' https://demoqa.com/upload-download')

time.sleep(3)

# Записываем поле ввода в переменную
upload_file_field = driver.find_element('xpath', "//input[@type='file']")
# Загружаем картинку
upload_file_field.send_keys(f'{os.getcwd()}\\downloads\\STE In Banner.jpg')

time.sleep(3)



