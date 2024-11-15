from src.save_to_csv import save_to_csv
from src.fetch_data import *
from src.product_page_url import control_pagination
from src.categories import categories
from src.download_images import download_image
import re
import os

PAGE_URL = "https://books.toscrape.com/"
DATA_FOLDER = "data/data_category"
IMAGE_FOLDER = "data/image_category"

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
categories_url = categories(PAGE_URL)

# Products urls
for category_url in categories_url:
    urls = control_pagination(PAGE_URL, category_url, "div", "image_container")

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
        
        # Generate category name
        category_name = category_url.split("/")[-2]
        category_name = re.sub(r"_\d+$", "", category_name) # Regex to remove _ and numbers
        
        
            # Download images
    
        # Create a folder for each category
        category_image_folder = os.path.join(IMAGE_FOLDER, category_name)
        os.makedirs(category_image_folder, exist_ok=True)
        
        # Generate image name
        image_name = url.split("/")[-2]
        image_name = re.sub(r"_\d+$", "", image_name) # Regex to remove _ and numbers
        image_name= f"{image_name}.jpg"
        
        # Save the image in the corresponding folder
        download_image(image_name, data["image_url"], category_image_folder)
        
    
            # Final file for each category
    file_name = f"{category_name}.csv"
    save_to_csv(file_name, headers, rows, DATA_FOLDER)
        