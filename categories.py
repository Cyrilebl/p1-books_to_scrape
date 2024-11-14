import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

page_url = "https://books.toscrape.com/"
response = requests.get(page_url)
soup = BeautifulSoup(response.content, "html.parser")

def categories():
    nav_bar = soup.find("ul", class_="nav")
    categories_list = nav_bar.find("ul").find_all("a")
    
    categories = []
    
    for category in categories_list:
        href = category.get("href")
        categories_urls = urljoin(page_url, href)
        categories.append(categories_urls)
        
    print(categories)
    
categories()