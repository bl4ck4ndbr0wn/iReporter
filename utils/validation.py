import re


def validate_login(data):
    for key in data.keys():
        if not data[key]:
            return {key: f"{key} Field can not be blank"}

    if not re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', data["password"]):
        return {"password": "Password field must be at least 8 characters."}

    if not re.match("^[a-zA-Z]+$", data["username"]):
        return {"username": "Username Field Should only contain characters."}

    return None


def validate_signup(data):
    for key in data.keys():
        if not data[key] and key != "othernames"and key != "phonenumber":
            return {key: f"{key} Field can not be blank"}

    if not re.match("^[a-zA-Z]+$", data["username"]):
        return {"username": "Username Field Should only contain characters."}

    if not re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', data["password"]):
        return {"password": "Password field must be at least 8 characters."}

    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", data["email"]):
        return {"email": "Enter a valid Email Address"}

    if not re.match("^[a-zA-Z]+$", data["firstname"]):
        return {"firstname": "First Name Field Should only contain characters."}

    if not re.match("^[a-zA-Z]+$", data["lastname"]):
        return {"lastname": "Last Name Field Should only contain characters."}

    return None


def validate_profile(data):
    for key in data.keys():
        if not data[key] and key != "othernames"and key != "phonenumber":
            return {key: f"{key} Field can not be blank"}

    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", data["email"]):
        return {"email": "Enter a valid Email Address"}

    if not re.match("^[a-zA-Z]+$", data["firstname"]):
        return {"firstname": "First Name Field Should only contain characters."}

    if not re.match("^[a-zA-Z]+$", data["lastname"]):
        return {"lastname": "Last Name Field Should only contain characters."}

    return None


def validate_create_incident(data):
    for key in data.keys():
        if not data[key].strip():
            return {key: f"{key} Field can not be blank"}


def validate_update_incident(data):
    for key in data.keys():
        if not data[key].strip():
            return {key: f"{key} Field can not be blank"}


def validate_update_incident_image(data):
    for key in data.keys():
        if not data[key]:
            return {key: f"{key} Field can not be blank"}
