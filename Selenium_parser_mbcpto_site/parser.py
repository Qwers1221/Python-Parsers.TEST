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

    # Закрытие окна, и на всякий случай браузер полностью
    browser.close()
    browser.quit()

login(username, password)