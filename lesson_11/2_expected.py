import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# driver.get('https://demoqa.com/dynamic-properties')

# VISIBLE_AFTER_BUTTON = ('xpath', '//button[@id="visibleAfter"]')

# ENABLE_IN_SECONDS = ('xpath', '//button[@id="enableAfter"]')

# wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)).click()

# wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS)).click()

driver.get('https://the-internet.herokuapp.com/dynamic_controls')

# REMOVE_BUTTON = ('xpath', '//button[text()="Remove"]')
#
# driver.find_element(*REMOVE_BUTTON).click()
#
# wait.until(EC.visibility_of_element_located(REMOVE_BUTTON))
#
# print('ВСЕ ОК!')

ENABLE_BUTTON = ('xpath', '//button[text()="Enable"]')
TEXT_FIELD = ('xpath', '//input[@type="text"]')

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click() # Ждем пока кнопка станет кликабельной
time.sleep(3)
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys('Hello!')
time.sleep(3)
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, 'Hello!'))
time.sleep(3)

print('ВСЕ ОК!')
