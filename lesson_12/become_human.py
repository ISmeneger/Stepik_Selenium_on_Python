import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920, 1080')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# driver.get('https://dzen.ru')
#
# driver.save_screenshot('screen.png')

# driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')

driver.get('https://whatismyipaddress.com/')

driver.save_screenshot('screen.png')
wait.until(EC.title_is('What Is My IP Address - See Your Public Address - IPv4 & IPv6'))

driver.save_screenshot('screen.png')