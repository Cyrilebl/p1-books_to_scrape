import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def categories(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        return print(e)

    nav_bar = soup.find("ul", class_="nav")
    categories_list = nav_bar.find("ul").find_all("a")
    
    categories = []
    
    for category in categories_list:
        href = category.get("href")
        categories_urls = urljoin(url, href)
        categories.append(categories_urls)
        
    return categories
