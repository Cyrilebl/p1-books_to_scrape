import csv
import os

def save_to_csv(file_name, headers, rows, folder_path):
    
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)
    
    # Construct the full file path
    full_path = os.path.join(folder_path, file_name)
    
    # Save the data to the CSV file
    with open(full_path, "w") as file_csv:
        writer = csv.writer(file_csv, delimiter=",")
        writer.writerow(headers)
        writer.writerows(rows)