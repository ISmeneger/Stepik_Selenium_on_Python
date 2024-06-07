import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')

# Задание 1. Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
CHANGE_TEXT_TO_SELENIUM_WEBDRIVER_BUTTON = ('xpath', '//button[@id="populate-text"]')
TEXT_VISIBLE = ('xpath', '//h2[@id="h2"]')

driver.find_element(*CHANGE_TEXT_TO_SELENIUM_WEBDRIVER_BUTTON).click()
time.sleep(3)
wait.until(EC.text_to_be_present_in_element(TEXT_VISIBLE, 'Selenium Webdriver'))
time.sleep(3)
print('OK!!!')
print('=====================')

# Задание 2. Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
DISPLAY_BUTTON_AFTER_10_SECONDS = ('xpath', '//button[@id="display-other-button"]')
ENABLED_BUTTON = ('xpath', '//button[@id="hidden"]')

driver.find_element(*DISPLAY_BUTTON_AFTER_10_SECONDS).click()
time.sleep(3)
wait.until(EC.visibility_of_element_located(ENABLED_BUTTON))
time.sleep(3)
print('OK!!!')
print('=====================')

# Задание 3. Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
ENABLE_BUTTON_AFTER_10_SECONDS = ('xpath', '//button[@id="enable-button"]')
BUTTON = ('xpath', '//button[@id="disable"]')
driver.find_element(*ENABLE_BUTTON_AFTER_10_SECONDS).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable(BUTTON)).click()
time.sleep(3)
print('OK!!!')
print('=====================')

# Задание 4. Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта
CLICK_ME_TO_OPEN_AN_ALERT_AFTER_5_SECONDS = ('xpath', '//button[@id="alert"]')
driver.find_element(*CLICK_ME_TO_OPEN_AN_ALERT_AFTER_5_SECONDS).click()
time.sleep(3)
wait.until(EC.alert_is_present())
time.sleep(3)
print('OK!!!')
