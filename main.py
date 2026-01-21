import csv
from app.validator import validate_row
from app.cleaner import clean_row
from app.logger import log_error

input_file = "data/raw_sale.csv"
output_file = "clean_sales.csv"

clean_data = []

with open(input_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            validate_row(row)
            clean_data.append(clean_row(row))
        except Exception as e:
            log_error(f"{row} → {str(e)}")

with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["order_id","customer","amount","date"])
    writer.writeheader()
    writer.writerows(clean_data)

print("Cleaning completed. Check clean_sales.csv and error_log.txt")
