import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)

driver.get('https://the-internet.herokuapp.com/drag_and_drop')

# COLUMN_A = ('xpath', '//div[@id="column-a"]')
# COLUMN_B = ('xpath', '//div[@id="column-b"]')
#
# A = driver.find_element(*COLUMN_A)
# B = driver.find_element(*COLUMN_B)
#
# # Первый способ реализации метода drag_and_drop
# time.sleep(2)
#
# action.drag_and_drop(A, B).perform()
#
# time.sleep(2)

# Второй способ реализации метода drag_and_drop
driver.get('https://tympanus.net/Development/DragDropInteractions/index.html')

GREED_ITEM = ('xpath', '(//div[@class="grid__item"])[3]')
SIDEBAR_ITEM = ('xpath', '//div[@class="drop-area__item"][3]')

action.click_and_hold(driver.find_element(*GREED_ITEM)) \
    .pause(2) \
    .move_to_element(driver.find_element(*SIDEBAR_ITEM)) \
    .release() \
    .perform()




