import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=chrome_options)

# FORM_NAME_FIELD_LOCATOR = ('xpath', '//input[@id="RESULT_TextField-1"]')
# COPY_TEXT_LOCATOR = ('xpath', '//button[text()="Copy Text"]')
# IFRAME_LOCATOR = ('xpath', '//frame')
#
# driver.get('https://testautomationpractice.blogspot.com/')
#
# iframe = driver.find_element(*IFRAME_LOCATOR)
# driver.switch_to.frame(iframe)
# time.sleep(3)
# driver.find_element(*FORM_NAME_FIELD_LOCATOR).send_keys('Ilya')
# time.sleep(3)
#
# driver.switch_to.default_content()
# driver.find_element(*COPY_TEXT_LOCATOR).click()

# Вложенные iframes

driver.get('https://demoqa.com/nestedframes')

driver.switch_to.frame('frame1')
print(driver.find_element('xpath', '//body').text)

driver.switch_to.frame(0)
print(driver.find_element('xpath', '//body').text)

driver.switch_to.parent_frame()
print(driver.find_element('xpath', '//body').text)

driver.switch_to.default_content()