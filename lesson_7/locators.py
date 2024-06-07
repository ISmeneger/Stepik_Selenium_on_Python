import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://hyperskill.org/tracks')

time.sleep(3)

Hyperskill = ('xpath', '//ul[@class="navbar-nav"]')
Explore = ('xpath', '//li[@class="nav-item position-relative"]')
Pricing = ('xpath', '(//a[@class="nav-link"])[2]')
For_Business = ('xpath', '(//a[@class="nav-link"])[3]')
Sign_in = driver.find_element('xpath', '(//button[contains(@class,"btn")])[1]').click()
time.sleep(3)
Start_for_free = ('xpath', '(//button[contains(@class,"btn")])[2]')
All_tracks = ('xpath', '//a[contains(text(),"All tracks")]')
Top_tracks = ('xpath', '//a[contains(text(),"Top tracks")]')
Beginner_friendly = ('xpath', '(//a[contains(text(),"Beginner-friendly")])[1]')
Python = ('xpath', '//a[contains(text(),"Python")]')






