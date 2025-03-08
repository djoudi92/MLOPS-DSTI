import re

def validate_username(username: str) -> bool:
    """Username should contain only letters, numbers, and underscores."""
    return bool(re.match(r"^\w+$", username))

def validate_password(password: str) -> bool:
    """Password must be at least 8 characters, contain a number, a letter, and a special character."""
    return bool(re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password))

def validate_email(email: str) -> bool:
    """Email should be in a valid format like user@example.com."""
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email))

def get_user_input():
    """Takes user input for username, email, and password."""
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    return {"username": username, "email": email, "password": password}
