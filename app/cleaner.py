def clean_row(row):
    row["customer"] = row["customer"].strip().title()
    return row