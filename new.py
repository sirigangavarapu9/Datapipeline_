import csv

# Dummy data
data = [
    {"Name": "John Doe", "Age": 25, "City": "New York"},
    {"Name": "Jane Smith", "Age": 30, "City": "London"},
    {"Name": "Michael Johnson", "Age": 35, "City": "Paris"},
]

# CSV file path
csv_file = "dummy_data.csv"

# Write data to CSV file
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
    writer.writeheader()
    writer.writerows(data)

print(f"Dummy CSV file '{csv_file}' generated successfully.")
