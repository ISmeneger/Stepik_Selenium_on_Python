import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://demoqa.com/selectable')

GRID_TAB = ('xpath', '//a[@id="demo-tab-grid"]')
ELEMENT_ONE = ('xpath', '//li[text()="One"]')
ELEMENT_TWO = ('xpath', '//li[text()="Two"]')
ELEMENT_THREE = ('xpath', '//li[text()="Three"]')

driver.find_element(*GRID_TAB).click()

print('Кликнуть на элементы и убедиться, что они выбраны')

for i in range(3):
    element = driver.find_element("xpath", f'//div[@id="row1"]/li[{i + 1}]')
    before = element.get_attribute("class")
    print(before)
    element.click()
    time.sleep(2)
    after = element.get_attribute("class")
    print(after)
    assert "active" in after
    print('=================')

time.sleep(3)

print('Кликнуть еще раз на элементы и убедиться, что теперь они не выбраны')

for i in range(3):
    element = driver.find_element("xpath", f'//div[@id="row1"]/li[{3 - i}]')
    before = element.get_attribute("class")
    print(before)
    element.click()
    time.sleep(2)
    after = element.get_attribute("class")
    print(after)
    assert "active" not in after
    print('=================')

# Решение без использования циклов:

# before = driver.find_element(*ELEMENT_ONE).get_attribute('class')
# print(before)
# driver.find_element(*ELEMENT_ONE).click()
# after = driver.find_element(*ELEMENT_ONE).get_attribute('class')
# print(after)
# assert 'active' in after
#
# time.sleep(2)
# print('=================')
#
# before = driver.find_element(*ELEMENT_TWO).get_attribute('class')
# print(before)
# driver.find_element(*ELEMENT_TWO).click()
# after = driver.find_element(*ELEMENT_TWO).get_attribute('class')
# print(after)
# assert 'active' in after
#
# time.sleep(2)
# print('=================')
#
# before = driver.find_element(*ELEMENT_THREE).get_attribute('class')
# print(before)
# driver.find_element(*ELEMENT_THREE).click()
# after = driver.find_element(*ELEMENT_THREE).get_attribute('class')
# print(after)
# assert 'active' in after
#
# time.sleep(2)
#
# print('Кликнуть еще раз на элементы и убедиться, что теперь они не выбраны')
#
# before = driver.find_element(*ELEMENT_THREE).get_attribute('class')
# print(before)
# driver.find_element(*ELEMENT_THREE).click()
# after = driver.find_element(*ELEMENT_THREE).get_attribute('class')
# print(after)
# assert 'active' not in after
#
# time.sleep(2)
# print('=================')
#
# before = driver.find_element(*ELEMENT_TWO).get_attribute('class')
# print(before)
# driver.find_element(*ELEMENT_TWO).click()
# after = driver.find_element(*ELEMENT_TWO).get_attribute('class')
# print(after)
# assert 'active' not in after
#
# time.sleep(2)
# print('=================')
#
# before = driver.find_element(*ELEMENT_ONE).get_attribute('class')
# print(before)
# driver.find_element(*ELEMENT_ONE).click()
# after = driver.find_element(*ELEMENT_ONE).get_attribute('class')
# print(after)
# assert 'active' not in after
#
# time.sleep(2)