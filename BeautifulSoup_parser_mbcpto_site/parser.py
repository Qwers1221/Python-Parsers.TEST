import requests
from bs4 import BeautifulSoup

URL = "https://mbzpto.org.ua/category/news/"

def parse(url, data = []):
    page = requests.get(url)
    soup_page = BeautifulSoup(page.text, "lxml")
    posts = soup_page.find_all("article", class_ = "post")

    for post in posts:
        try:
            image_link = post.find("img", class_ = "wp-post-image").get("src")
        except:
            image_link = "-"
        try:
            link = post.find("a", class_ = "").get("href")
        except:
            link = "-"
        try:
            name = post.find("h3", class_ = "entry-title mh-loop-title").find("a", class_ = "").text
        except:
            name = "-"
        try:
            description = post.find("div", class_ = "mh-loop-excerpt").find("div", class_ = "mh-excerpt").find("p", class_ = "").text
        except:
            description = "-"
        
        data.append([image_link, link, name, description])

    return data

data = []

print(parse(URL, data))
