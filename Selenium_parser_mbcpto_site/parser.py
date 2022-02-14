import time, random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from auth_data import *

def login(username, password):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # executable_path=r'C:\\Users\\Admin\\Downloads\\chromedriver\\chromedriver.exe'
    browser.get("https://www.instagram.com/")
    time.sleep(random.randrange(3, 5))

    browser.close()
    browser.quit()

login(username, password)