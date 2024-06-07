import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)

LEFT_CLICK_BUTTON_LOCATOR = ('xpath', '//button[@id="leftClick"]')
DOUBLE_CLICK_BUTTON_LOCATOR = ('xpath', '//button[@id="doubleClick"]')
RIGHT_CLICK_BUTTON_LOCATOR = ('xpath', '//button[@id="rightClick"]')
HOVER_BUTTON_LOCATOR = ('xpath', '//button[@id="colorChangeOnHover"]')

# driver.get('https://testkru.com/Elements/Buttons')

# # Клик левой кнопкой мыши
# left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
#
# # Двойной клик
# double_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
#
# # Клик правой кнопкой мыши
# right_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
#
# # Hover button
# hover_button = driver.find_element(*HOVER_BUTTON_LOCATOR)
# time.sleep(3)
#
# # Двойной клик
# action.double_click(double_button).perform()
# time.sleep(3)
#
# # Клик левой кнопкой мыши
# action.click(left_button).perform()
# time.sleep(3)
#
# # Клик правой кнопкой мыши
# action.context_click(right_button).perform()
# time.sleep(3)

# # Построение цепочки действий
# action.click(left_button).pause(2).double_click(double_button).pause(2).context_click(right_button).perform()
# time.sleep(3)
#
# # Наведение на элемент
# action.move_to_element(hover_button).perform()
# time.sleep(3)

# Выпадающее меню
# driver.get('https://demoqa.com/menu')
#
# MENU_ITEM_2_LOCATOR = ('xpath', '//a[text()="Main Item 2"]')
# SUB_LIST_LOCATOR = ('xpath', '//a[text()="SUB SUB LIST »"]')
#
# menu_item_2 = driver.find_element(*MENU_ITEM_2_LOCATOR)
# sub_list_locator = driver.find_element(*SUB_LIST_LOCATOR)
#
# action.move_to_element(menu_item_2) \
#     .pause(2) \
#     .move_to_element(sub_list_locator) \
#     .perform()
# time.sleep(2)

# Скролл к элементу

driver.get("https://clipboardjs.com/")

SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")

SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)

action.scroll_to_element(SOME_ELEMENT).perform() # Используем скролл до элемента

time.sleep(2)

