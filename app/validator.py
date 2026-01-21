from app.exception import MissingValueError, InvalidDataTypeError

def validate_row(row):
    if row["customer"] == "" or row["date"] == "":
        raise MissingValueError("Missing value found")

    if not row["amount"].isdigit():
        raise InvalidDataTypeError("Amount must be a number")


