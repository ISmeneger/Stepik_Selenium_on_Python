import time
from selenium import webdriver

driver = webdriver.Chrome()

# Задание 1:
driver.get('https://demoqa.com/text-box')

full_name_field = driver.find_element('xpath', '//input[@id="userName"]')
assert full_name_field.get_attribute('value') == ''
full_name_field.send_keys('Ivan Ivanov')
time.sleep(3)
full_name_field_value = full_name_field.get_attribute('value')
assert 'Ivan' in full_name_field_value

email_field = driver.find_element('xpath', '//input[@id="userEmail"]')
assert email_field.get_attribute('value') == ''
email_field.send_keys('email@ya.ru')
time.sleep(3)
email_field_value = email_field.get_attribute('value')
assert 'email@ya.ru' in email_field_value

current_address_field = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
assert current_address_field.get_attribute('value') == ''
current_address_field.send_keys('Russia, SPb')
time.sleep(3)
current_address_field_value = current_address_field.get_attribute("value")
assert 'Russia, SPb' in current_address_field_value

permanent_address_field = driver.find_element('xpath', '//textarea[@id="permanentAddress"]')
assert permanent_address_field.get_attribute('value') == ''
permanent_address_field.send_keys('Russia, SPb')
time.sleep(3)
permanent_address_field_value = current_address_field.get_attribute("value")
assert 'Russia, SPb' in permanent_address_field_value

# Задание 2:
driver.get('http://the-internet.herokuapp.com/status_codes')

link_list = driver.find_elements('xpath', '//a[contains(@href, "status_codes")]')
time.sleep(5)
for codes in ['200', '301', '404', '500']:
    driver.find_element('xpath', f'//a[@href = "status_codes/{codes}"]').click()
    time.sleep(3)
    driver.back()

