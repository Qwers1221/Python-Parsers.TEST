import time, random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from auth_data import *

# Функция авторизации в Instagram
def login(username, password):
    # Подключение WebDriver(Chrome) через менеджер, обычный способ из директории не сработал!
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # Загрузка сайта + ждем от 3 до 5 сек для уверености
    browser.get("https://www.instagram.com/")
    time.sleep(random.randrange(3, 5))
    # Ищем елемент username на странице, очищаем + заполняем именем из файла auth_data, ждем 2 сек для уверености
    username_input = browser.find_element_by_name("username")
    username_input.clear()
    username_input.send_keys(username)
    time.sleep(2)
    # Ищем елемент password на странице, очищаем + заполняем паролем из файла auth_data, ждем 2 сек для уверености
    password_input = browser.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(2)
    # Нажимаем клавишу Enter в поле пароля + ждем 2 сек для уверености
    password_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # Закрытие окна, и на всякий случай браузер полностью
    browser.close()
    browser.quit()

login(username, password)