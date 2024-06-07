import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://hyperskill.org/tracks')

time.sleep(3)

driver.find_elements('class name', 'nav-link')[3].click()

time.sleep(5)