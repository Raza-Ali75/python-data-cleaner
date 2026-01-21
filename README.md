# CSV Data Cleaner & Validator (Python)

##  Project Overview
This project is a Python-based tool that cleans and validates raw CSV data files.
It is designed to simulate real-world data preprocessing tasks performed by Data Analysts
before analysis and reporting.

The tool reads a raw CSV file, validates data quality, logs errors, and exports a cleaned dataset.

---

##  Features
- Reads raw CSV files using Python
- Detects missing values in important columns
- Detects invalid data types (e.g. non-numeric values)
- Logs all data errors into a separate log file
- Exports only valid and cleaned records to a new CSV file

---
##  Project Structure
```
python-data-cleaner/
│
├── data/
│ └── raw_sales.csv # Input raw data file
│
├── cleaner.py # Data cleaning logic
├── validator.py # Data validation rules
├── exceptions.py # Custom exceptions
├── logger.py # Logging configuration
├── main.py # Main execution file
│
├── clean_sales.csv # Output cleaned data
└── error_log.txt # Error log file
```
---

## How to Use

### Step 1: Add your CSV file
Place your CSV file inside the `data/` folder and rename it to:
raw_sale.csv


### Step 2: Run the program
Open terminal in the project folder and run:
python main.py


### Step 3: Output
- `clean_sales.csv` → contains cleaned and valid data
- `error_log.txt` → contains all detected data errors

---

##  Concepts Used
- File Handling
- CSV Processing
- Exception Handling & Custom Exceptions
- Logging & Debugging
- Modular Python Code Structure

---

## Why this Project
Data in real-world scenarios is often messy and incomplete.
This project demonstrates how Python can be used to build reliable
data cleaning systems before performing data analysis.

---

## Author
Raza Ali  
Aspiring Data Analyst | IITM BS Data Science Student
