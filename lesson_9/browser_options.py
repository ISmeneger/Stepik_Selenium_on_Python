import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options_page_load_strategy = 'eager'
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--ignore-sertificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--disable-cache")
driver = webdriver.Chrome(options=chrome_options)

start_time = time.time()

driver.get('https://whatismyipaddress.com/')

end_time = time.time()
result = end_time - start_time
print(result)
