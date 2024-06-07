import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXI_SERVER = "77.232.21.4:8080"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXI_SERVER}") # Добавляем прокси через опции

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://2ip.ru") # Проверяем IP-адрес

time.sleep(5)

# Добавление proxy-server

