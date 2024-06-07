import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=chrome_options)

# FOR_BUSINESS_BUTTON_LOCATOR = ('xpath', '//a[text()=" For Business "]')
# START_FREE_BUTTON_LOCATOR = ('xpath', '//a[text()="Start for Free"]')
#
# driver.get('https://hyperskill.org/tracks')
#
# time.sleep(3)

# print(driver.current_window_handle)

# print(len(driver.window_handles))

# driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
# time.sleep(3)
#
# tabs = driver.window_handles
# driver.switch_to.window(tabs[1])
#
# driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
# time.sleep(3)

# # Шаг 1 - Открыть базовую страницу
# driver.get("https://whatismyipaddress.com/")
#
# # Шаг 2 - Открытие нескольких вкладок
# driver.switch_to.new_window("tab")
# driver.switch_to.new_window("tab")
# time.sleep(2)
#
# # Шаг 3 - Получение списка открытых вкладок
# windows = driver.window_handles
# print(len(windows)) # Выведем на экран кол-во открытых вкладок
#
# # Шаг 4 - Получение дескриптора текущего окна для дальнейшей проверки
# current_tab = driver.current_window_handle
# print("Дескриптор текущей вкладки: ", current_tab)
# print("Индекс: ", windows.index(current_tab)) # Получаем индекс вкладки в списке для информативности
#
# # Шаг 5 - Переключение на вкладку по ее индексу
# driver.switch_to.window(windows[1])
# time.sleep(2)
#
# # Шаг 6 - Проверка, что вкладка переключилась
# assert current_tab != driver.current_window_handle, "Вкладка не переключилась"

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Получение дескриптора текущего окна
old_window = driver.current_window_handle
print("Дескриптор первого окна: ", old_window)

# Шаг 3 - Открытие и переключение на новое окно
driver.switch_to.new_window("window")

# Шаг 4 - Получение дескриптора нового окна
new_window = driver.current_window_handle
print("Дескриптор второго окна: ", new_window)

# Шаг 5 - Проверка, что окно переключилось
assert new_window == driver.current_window_handle, "Окно не переключилось"
time.sleep(2)

# Шаг 6 - Открытие страницы в новом окне
driver.get("https://vk.com")

# Шаг 7 - Переключение на старое окно
driver.switch_to.window(old_window)

# Шаг 8 - Проверка, что переключились на старое окно
assert old_window == driver.current_window_handle, "Окно не переключилось"

# Шаг 9 - Открытие страницы в старом окне
driver.get("https://ya.ru")

# Шаг 10 - Переключение на новое окно
driver.switch_to.window(new_window)

# Шаг 11 - Закрытие нового окна
driver.close()

# driver.get('https://hyperskill.org/tracks')
#
# time.sleep(5)
#
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
#
# driver.get('https://ya.ru')
# time.sleep(3)

# driver.switch_to.new_window('window')
#
# time.sleep(3)
#
# driver.get('https://ya.ru')
#
# time.sleep(5)




