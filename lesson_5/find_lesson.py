import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.freeconferencecall.com/login')
time.sleep(3)

driver.find_element('id', 'loginformsubmit').click()

time.sleep(3)