import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

driver.get('https://seiyria.com/bootstrap-slider/')

# driver.execute_script("alert('Hello!')")

EX_2_LOCATOR = ('xpath', '//h3[text()="Example 2: "]')
EX_2 = driver.find_element(*EX_2_LOCATOR)

# action.scroll_to_element(EX_2).perform()

scrolls.scroll_to_element(EX_2)

time.sleep(5)

