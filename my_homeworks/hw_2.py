import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://testautomationpractice.blogspot.com/')

time.sleep(3)

driver.find_element('class name', 'wikipedia-icon')

time.sleep(3)

driver.find_element('id', 'Wikipedia1_wikipedia-search-input')

time.sleep(3)

driver.find_element('class name', 'wikipedia-search-button')

time.sleep(3)

driver.find_elements('tag name', 'button')[0].click()

time.sleep(3)

