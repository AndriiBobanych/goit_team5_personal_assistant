from datetime import datetime
import re


def phone_validity(number: str):
    phone_number = (
        number.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    if phone_number.isdigit() and phone_number.startswith("380") and len(phone_number) == 12:
        return True
    else:
        return False


def email_validity(email: str):
    input_email = email.strip()
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    if re.match(pattern, input_email) is not None:
        return True
    else:
        return False


def birthday_validity(birthday: str):
    try:
        if datetime.strptime(str(birthday), "%d-%m-%Y").date():
            return True
    except ValueError:
        return False

