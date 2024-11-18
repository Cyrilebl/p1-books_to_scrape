import requests
import os

def download_image(image_name, image_url, folder_path):
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)
    
    response = requests.get(image_url, stream=True)
    
    full_path = os.path.join(folder_path, image_name)
        
    if response.status_code == 200: 
        # Download (Write Binary)
        with open(full_path, 'wb') as file:
            file.write(response.content)
    else:
        return
