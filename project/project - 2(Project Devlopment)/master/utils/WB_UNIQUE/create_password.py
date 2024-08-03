import string
import random

def generate_password(length=8):
    """
    Generates a random password with a specified length.

    Args:
        length (int): The desired length of the password. Default is 8.

    Returns:
        str: A random password consisting of uppercase letters, lowercase letters, digits, and special characters (@, _, .).

    Usage:
        # Example 1: Generate a password with the default length (8 characters)
        password1 = generate_password()
        print(f"Generated password (default length 8): {password1}")

        # Example 2: Generate a password with a specified length (e.g., 12 characters)
        password2 = generate_password(12)
        print(f"Generated password (length 12): {password2}")
    """
    symbols = string.ascii_letters + string.digits + "@_."
    password = ""
    for digit in range(length):
        password += symbols[random.randint(0, len(symbols)-1)]

    return password