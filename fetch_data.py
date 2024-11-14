from product_page_url import *
from bs4 import BeautifulSoup
import requests

soup = None

def product_data(url):
    global soup
    
    response = requests.get(url)
    page = response.content
    # Parse le HTML en objet BeautifulSoup
    soup = BeautifulSoup(page, "html.parser")
    
    # Data for all the products
    product_data = {
    "title" : fetch_title("h1"),
    "universal_product_code" : fetch_text_from_table("tr", 0, "td"),
    "price_excluding_tax" : fetch_text_from_table("tr", 2, "td"),
    "price_including_tax" : fetch_text_from_table("tr", 3, "td"),
    "number_available" : fetch_text_from_table("tr", 5, "td"),
    "product_description" : fetch_description("div", "product_description"),
    "category" : fetch_category("ul", "breadcrumb"),
    "review_rating" : fetch_rating("p", "star-rating"),
    "image_url" : fetch_image_url("div", "carousel")
    }
    
    return product_data

def fetch_title(selector):
    element = soup.find(selector)  
    element = element.get_text(strip=True)
    return element if element else ""

def fetch_description(selector, attribute):
    element = soup.find(selector, id=attribute)
    inner_selector = element.find_next_sibling("p")
    return inner_selector.get_text(strip=True) if element else ""

def fetch_text_from_table(selector, n, inner_selector):
    table = soup.find("table", class_="table")
    
    elements = table.find_all(selector)
    if n < len(elements):
        element = elements[n]
        inner_element = element.find(inner_selector)
        
        if inner_element:
            text_content = inner_element.get_text(strip=True)

            if n == 5:
                words_to_remove = ["In","stock","available","(", ")"]
                for word in words_to_remove:
                    text_content = text_content.replace(word, "")
            
            return text_content
                                
    return text_content if element else ""

def fetch_category(selector, attribute):
    element = soup.find(selector, class_=attribute)
    li_element = element.find_all("li")
    li_text = [li.get_text(strip=True) for li in li_element]
    return li_text[2] if element else ""

def fetch_rating(selector, attribute):
    element = soup.find(selector, class_=attribute)

    classes = element.get("class", [])
    rating = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }
    key = classes[1].lower()
        
    return f"{rating[key]}/5" if element else ""

def fetch_image_url(selector, attribute):
    element = soup.find(selector, class_=attribute)
    inner_selector = element.find("img")
    
    image_url = inner_selector.get("src")
    page_url = "https://books.toscrape.com/"
    
    full_url = requests.compat.urljoin(page_url, image_url)
    return full_url
    