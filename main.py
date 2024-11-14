from save_to_csv import save_to_csv
from fetch_data import *
from product_page_url import control_pagination

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

# Products urls
url = "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
urls = control_pagination(url, "div", "image_container")

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

save_to_csv("data.csv", headers, rows)

categories = []