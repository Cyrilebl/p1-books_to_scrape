import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def control_pagination(url, selector, attribute):
    products_urls = []
    
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        elements = soup.find_all(selector, class_=attribute)
        
        page_url = "https://books.toscrape.com/"
        
        for element in elements:
            inner_selector = element.find("a")
            product_url = inner_selector.get("href")
            
            product_url = product_url.replace("../", "")
            product_url = "catalogue/" + product_url
            
            full_url = requests.compat.urljoin(page_url, product_url)
            products_urls.append(full_url)

        next_page = soup.find("li", class_="next")
        
        if next_page:
            new_page_url = next_page.find("a").get("href")
            url = urljoin(url, new_page_url)
        else:
            break
    return products_urls