from save_to_csv import save_to_csv
from fetch_data import *
from product_page_url import control_pagination
from categories import categories
import re

# File titles
headers = ["product_page_url",
            "title",
            "universal_product_code (upc)",
            "price_excluding_tax",
            "price_including_tax",
            "number_available",
            "product_description",
            "category",
            "review_rating",
            "image_url"]

# Categories urls
page_url = "https://books.toscrape.com/"
categories_url = categories(page_url)

# Products urls
for category_url in categories_url:
    urls = control_pagination(page_url, category_url, "div", "image_container")

    # Collect data for each product
    rows = []
    for url in urls:
        data = product_data(url)
        
        rows.append([
            url,
            data["title"],
            data["universal_product_code"],
            data["price_excluding_tax"],
            data["price_including_tax"],
            data["number_available"],
            data["product_description"],
            data["category"],
            data["review_rating"],
            data["image_url"]
            ])

    # Keep category name
    category_name = category_url.split("/")[-2]
    # Regex to remove _ and numbers
    category_name = re.sub(r"_\d+$", "", category_name)
    
    # Final file name for each category
    file_name = f"{category_name}.csv"
    save_to_csv(file_name, headers, rows)
