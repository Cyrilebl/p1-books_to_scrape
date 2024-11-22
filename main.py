from src.save_to_csv import save_to_csv
from src.fetch_data import *
from src.product_page_url import control_pagination
from src.categories import categories
from src.download_images import download_image
import re
import os
from concurrent.futures import ThreadPoolExecutor

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

def process_category(category_url):
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
        image_name = data["universal_product_code"]
        image_name= f"{image_name}.jpg"
        
        # Save the image in the corresponding folder
        download_image(image_name, data["image_url"], category_image_folder)
        
    
    # Final file for each category
    save_to_csv(f"{category_name}.csv", headers, rows, DATA_FOLDER)
        
def main():
    # Categories urls
    categories_url = categories(PAGE_URL)
    
    # Process the categories in parallel
    with ThreadPoolExecutor() as executor:
        executor.map(process_category, categories_url)
        
if __name__ == "__main__":
    main()