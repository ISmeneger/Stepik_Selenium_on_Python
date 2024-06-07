import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

CHECKBOX_1 = ('xpath', '(//input[@type="checkbox"])[1]')

# driver.get('https://the-internet.herokuapp.com/checkboxes')
# Получение статуса чек-бокса через метод get_attribute

# time.sleep(3)
# print(driver.find_element(*CHECKBOX_1).get_attribute('checked'))
# driver.find_element(*CHECKBOX_1).click()
# print(type(driver.find_element(*CHECKBOX_1).get_attribute('checked')))
# time.sleep(3)

# Получение статуса чек-бокса через метод is_selected

# time.sleep(3)
# print(driver.find_element(*CHECKBOX_1).is_selected())
# driver.find_element(*CHECKBOX_1).click()
# print(driver.find_element(*CHECKBOX_1).is_selected())
# time.sleep(3)

# Нюанс 1.

# CHECKBOX_HOME_STATUS = ('xpath', '//input[@id="tree-node-home"]')
# CHECKBOX_HOME_ACTION = ('xpath', '//span[@class="rct-checkbox"]')
#
# driver.get('https://demoqa.com/checkbox')
#
# print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())
# driver.find_element(*CHECKBOX_HOME_ACTION).click()
# print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())
#
# time.sleep(3)

# Нюанс 2.

ELEMENT_ONE = ('xpath', '//li[text()="Cras justo odio"]')

driver.get('https://demoqa.com/selectable')

before = driver.find_element(*ELEMENT_ONE).get_attribute('class')
print(before)
driver.find_element(*ELEMENT_ONE).click()
after = driver.find_element(*ELEMENT_ONE).get_attribute('class')
assert 'active' in after

time.sleep(3)

