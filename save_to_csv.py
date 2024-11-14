import csv

# Save to an csv file
def save_to_csv(file_name, headers, rows):
    with open(file_name, "w") as file_csv:
        writer = csv.writer(file_csv, delimiter=",")
        writer.writerow(headers)
        writer.writerows(rows)