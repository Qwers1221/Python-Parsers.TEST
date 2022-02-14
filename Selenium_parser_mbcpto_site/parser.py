import time, random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from auth_data import *

# Функция авторизации в Instagram
def login(username, password):
    # Подключение WebDriver(Chrome) через менеджер, обычный способ из директории не сработал!
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get("https://www.instagram.com/")
    time.sleep(random.randrange(3, 5))

    username_input = browser.find_elements_by_name("username")
    username_input.clear()
    username_input.send_keys(username)

    time.sleep(2)

    password_input = browser.find_elements_by_name("password")
    password_input.clear()
    password_input.send_keys(password)

    time.sleep(2)

    password_input.send_keys(Keys.ENTER)

    # Закрытие окна, и на всякий случай браузер полностью
    browser.close()
    browser.quit()

login(username, password)