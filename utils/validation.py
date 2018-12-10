import re


def validatesignup(data):
    errors = []

    for key, value in enumerate(data):
        if value == "" or value == " ":
            errors.append({f"{key}": f"{value} Field is required."})

    if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', data["password"]):
        return errors.append({"password": "Password field must be at least 8 characters."})

    if not re.match("^[a-zA-Z]+$", data["username"]):
        return errors.append({"username": "Username Field Should only contain characters."})

    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", data["email"]):
        return errors.append({"email": "Enter a valid Email Address"})

    return errors
