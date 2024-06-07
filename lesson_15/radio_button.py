import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

YES_RADIO_STATUS = ('xpath', '//input[@id="yesRadio"]')
YES_RADIO_ACTION = ('xpath', '//label[@for="yesRadio"]')

NO_RADIO_STATUS = ('xpath', '//input[@id="noRadio"]')
NO_RADIO_ACTION = ('xpath', '//label[@for="noRadio"]')

driver.get('https://demoqa.com/radio-button')

print(driver.find_element(*YES_RADIO_STATUS).is_selected())
driver.find_element(*YES_RADIO_ACTION).click()
print(driver.find_element(*YES_RADIO_STATUS).is_selected())

print(driver.find_element(*NO_RADIO_STATUS).is_enabled())

time.sleep(3)