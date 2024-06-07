import os
import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

# Задание 1.
driver.get('https://demoqa.com/upload-download')

time.sleep(3)

upload_file_field = driver.find_element('xpath', "//input[@type='file']")

upload_file_field.send_keys(f'{os.getcwd()}\\downloads\\STE In Banner.jpg')

time.sleep(5)

# Задание 2.
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\\lesson_6\\downloads"
}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://the-internet.herokuapp.com/download')

time.sleep(3)

list_links = driver.find_elements('xpath', f'//a[contains(@href, "download")]')
for link in list_links:
    link.click()
    time.sleep(2)