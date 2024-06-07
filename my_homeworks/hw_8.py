import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920, 1080')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

START_FOR_FREE_BUTTON = ('xpath', '//button[text()="Start for free"]')
FOR_BUSINESS_BUTTON = ('xpath', '//a[text()="Для бизнеса"]')
ENTERED_BUTTON = ('xpath', '(//a[contains(@class, "navbar-pc__link")])[2]')

ELEMENTS_FOR_CLICK = [START_FOR_FREE_BUTTON, FOR_BUSINESS_BUTTON, ENTERED_BUTTON]

# Открываем 3 пустые вкладки
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
time.sleep(3)

tab= driver.window_handles
links = ['https://hyperskill.org/login', 'https://www.avito.ru/', 'https://www.wildberries.ru/']

# Первый способ с помощью циклов:
# Открываем 3 вкладки:
for i in range(3):
    driver.switch_to.window(tab[i])
    driver.get(links[i])
    time.sleep(3)

time.sleep(3)

# Получаем title каждой страницы
for i in range(3):
    driver.switch_to.window(tab[i])
    current_title = driver.title
    print('Текущий заголовок страницы: ', current_title)
    time.sleep(3)

time.sleep(3)

# Кликаем на элемент на каждой странице
for i in range(3):
    driver.switch_to.window(tab[i])
    wait.until(EC.element_to_be_clickable(ELEMENTS_FOR_CLICK[i])).click()
    time.sleep(3)

# Второй способ напрямую без цикла
driver.switch_to.window(tab[0])
driver.get('https://hyperskill.org/login')
time.sleep(3)

driver.switch_to.window(tab[1])
driver.get('https://www.avito.ru/')
time.sleep(3)

driver.switch_to.window(tab[2])
driver.get('https://www.wildberries.ru/')
time.sleep(3)

driver.switch_to.window(tab[0])
current_title_1 = driver.title
print('Текущий заголовок страницы 1: ', current_title_1)
time.sleep(3)

driver.switch_to.window(tab[1])
current_title_2 = driver.title
print('Текущий заголовок страницы 2: ', current_title_2)
time.sleep(3)

driver.switch_to.window(tab[2])
current_title_3 = driver.title
print('Текущий заголовок страницы 3: ', current_title_3)
time.sleep(3)

driver.switch_to.window(tab[0])
driver.find_element(*START_FOR_FREE_BUTTON).click()
time.sleep(3)

driver.switch_to.window(tab[1])
driver.find_element(*FOR_BUSINESS_BUTTON).click()
time.sleep(3)

driver.switch_to.window(tab[2])
driver.find_element(*ENTERED_BUTTON).click()
time.sleep(3)

