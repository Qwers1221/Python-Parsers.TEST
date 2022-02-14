import time, random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import *

def login(username, password):
    browser = webdriver.Chrome(executable_path=r'chromedriver.exe')

    browser.get("https://www.instagram.com/")
    time.sleep(random.randrange(3, 5))

    browser.close()
    browser.quit()

login(username, password)