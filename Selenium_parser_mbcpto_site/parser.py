import time, random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from auth_data import *

# Подключение WebDriver(Chrome) через менеджер, обычный способ из директории не сработал!
browser = webdriver.Chrome(ChromeDriverManager().install())
# Время задержки перед началом след действия
sleep = random.randrange(3, 5)
# Функция авторизации в Instagram
def login(username, password):
    # Проверка на ошибку
    try:
        # Загрузка сайта + задержка
        browser.get("https://www.instagram.com/")
        time.sleep(sleep)
        # Ищем елемент username на странице, очищаем + заполняем именем из файла auth_data + задержка
        username_input = browser.find_element_by_name("username")
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(sleep)
        # Ищем елемент password на странице, очищаем + заполняем паролем из файла auth_data + задержка
        password_input = browser.find_element_by_name("password")
        password_input.clear()
        password_input.send_keys(password)
        # Нажимаем клавишу Enter в поле пароля + задержка
        password_input.send_keys(Keys.ENTER)
        time.sleep(sleep)
    except Exception as ex:
        print(ex) # Вывод ошибки в консоль

# Функция поиска в инсте по хештегу
def hashtag_liker_disliker(username, password, hashtag):
    login(username, password) # Авторизация в инсте
    # Проверка на ошибку
    try:
        # Открытие страницы тега + задержка
        browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        time.sleep(sleep)

        # for i in 3: # Не раб прокрутка страницы
        #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(sleep)

        # Поиск ссылок на странице
        hrefs = browser.find_elements_by_tag_name("a")
        # Отсейка, оставляем только ссылки постов
        posts_hrefs = []
        for item in hrefs:
            href = item.get_attribute("href")
            
            if "/p/" in href: 
                posts_hrefs.append(href)
        # Лайкаем каждую ссылку
        for url in posts_hrefs:
            try:
                browser.get(url)
                time.sleep(sleep)
                like_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button").click()
                time.sleep(sleep)
            except Exception as ex:
                print(ex) # Вывод ошибки в консоль

        # Закрытие окна, и на всякий случай браузер полностью
        browser.close()
        browser.quit()
    except Exception as ex:
        print(ex) # Вывод ошибки в консоль
        # Закрытие окна, и на всякий случай браузер полностью
        browser.close()
        browser.quit()

hashtag_liker_disliker(username, password, "surfing")