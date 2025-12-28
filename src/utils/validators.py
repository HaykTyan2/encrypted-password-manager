# src/utils/validators.py

def is_strong_password(password: str) -> bool:
    """
    Simple strength check:
    - at least 8 chars
    - contains digit
    - contains uppercase
    - contains lowercase
    - contains special char
    """
    if len(password) < 8:
        return False

    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|\\" for c in password)

    return has_digit and has_upper and has_lower and has_special
