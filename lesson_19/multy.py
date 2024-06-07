import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')
user_1 = webdriver.Chrome(options=chrome_options)

LOGIN_FIELD = ('xpath', '//input[@type="email"]')
PASSWORD_FIELD = ('xpath', '//input[@type="password"]')
SUBMIT_BUTTON = ('xpath', '//button[@type="submit"]')

user_1.get('https://hyperskill.org/login?next=/tracks')
user_1.find_element(*LOGIN_FIELD).send_keys('alekseik@ya.ru')
user_1.find_element(*PASSWORD_FIELD).send_keys('Qwerty132!')
user_1.find_element(*SUBMIT_BUTTON).click()
time.sleep(5)
user_1.close()

user_2 = webdriver.Chrome(options=chrome_options)
user_2.get('https://hyperskill.org/login?next=/tracks')
time.sleep(3)