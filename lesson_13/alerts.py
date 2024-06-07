import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get('https://demoqa.com/alerts')

BUTTON_1 = ('xpath', '//button[@id="alertButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

time.sleep(3)

alert.accept()

time.sleep(3)

BUTTON_3 = ('xpath', '//button[@id="confirmButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

time.sleep(3)
print(alert.text)
alert.dismiss()

time.sleep(3)

BUTTON_4 = ('xpath', '//button[@id="promtButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

time.sleep(3)

alert.send_keys('Hello world!')

alert.accept()

time.sleep(3)