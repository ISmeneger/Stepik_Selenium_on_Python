import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

# SELECT_LOCATOR = ('xpath', '//select[@id="dropdown"]')
#
# driver.get('https://the-internet.herokuapp.com/dropdown')

# # Выбор по тексту
# DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
# time.sleep(3)
# DROPDOWN.select_by_visible_text('Option 1')
# time.sleep(3)
#
# # Выбор по value
# DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
# time.sleep(3)
# DROPDOWN.select_by_value('2')
# time.sleep(3)
#
# # Выбор по index
# DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
# time.sleep(3)
# DROPDOWN.select_by_index(1)
# time.sleep(3)

# Перебор элементов в dropdown
# 1. Перебор по тексту
# DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
# all_options = DROPDOWN.options

# for option in all_options:
#     time.sleep(3)
#     if 'Option 2' in option.text:
#         print('Опция присутствует')
    # DROPDOWN.select_by_visible_text(option.text)

# 2. Перебор по index

# for option in all_options:
#     time.sleep(3)
#     DROPDOWN.select_by_index(all_options.index(option))

# 3. Перебор по value

# for option in all_options:
#     time.sleep(3)
#     DROPDOWN.select_by_value(option.get_attribute('value'))

# Работа с клавиатурой

# KEYBOARD_INPUT = ('xpath', '//input[@id="target"]')
#
# driver.get('https://the-internet.herokuapp.com/key_presses?')
# time.sleep(2)
# driver.find_element(*KEYBOARD_INPUT).send_keys('Dfhdkjfhjdkshfjsdkhfsdjk')
# time.sleep(2)
# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.CONTROL + 'A')
# time.sleep(2)
# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE)
# time.sleep(2)

# Работа с современным dropdown
# 1-ый способ

# SELECT_LOCATOR = ('xpath', '//input[@id="react-select-3-input"]')
#
# driver.get('https://demoqa.com/select-menu')
#
# time.sleep(2)
#
# driver.find_element(*SELECT_LOCATOR).send_keys('Mr.')
# driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)
#
# time.sleep(5)

# 2-ой способ

SELECT_ONE = ('xpath', '//div[@id="selectOne"]')
PROF_OPTION = ('xpath', '//div[text()="Prof."]')

driver.get('https://demoqa.com/select-menu')

time.sleep(2)

driver.find_element(*SELECT_ONE).click()
time.sleep(3)
driver.find_element(*PROF_OPTION).click()

time.sleep(3)

# Работа с современным мультиселектом

MULTISELECT_LOCATOR = ('xpath', '//input[@id="react-select-4-input"]')

driver.find_element(*MULTISELECT_LOCATOR).send_keys('Green')
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
driver.find_element(*MULTISELECT_LOCATOR).send_keys('Black')
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)

time.sleep(3)