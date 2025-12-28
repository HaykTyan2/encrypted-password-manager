# src/auth/master_password.py

import bcrypt
from getpass import getpass
from database.db import get_master_hash_and_salt, update_master_hash
from utils.validators import is_strong_password

def create_master_password():
    """
    Handles first-time setup:
    - Ask user to create a master password
    - Validate strength
    - Hash with bcrypt
    - Store hash in DB
    - Return raw master password to be used for key derivation
    """
    print("\nNo master password found. Let's create one!")

    while True:
        pw1 = getpass("Create master password: ")
        pw2 = getpass("Confirm master password: ")

        if pw1 != pw2:
            print("Passwords do not match. Try again.\n")
            continue

        if not is_strong_password(pw1):
            print("Password is too weak. Use more characters, numbers, symbols.\n")
            continue

        # Hash with bcrypt (bcrypt generates its own salt internally)
        hashed = bcrypt.hashpw(pw1.encode(), bcrypt.gensalt())

        # Store hash in database
        update_master_hash(hashed)

        print("Master password created successfully!\n")
        return pw1  # return *raw* password so key_manager can derive key

def verify_master_password(stored_hash):
    """
    Handles normal login:
    - Prompt user for password
    - Compare with stored bcrypt hash
    - Return raw password on success
    """
    print("\nPlease enter your master password.")

    while True:
        entered = getpass("Master password: ")
        #.checkpw() extracts the salt from the stored_hash, re-hashes the entered pswrd
        # using that salt, then compares that new hash to the stored hash
        if bcrypt.checkpw(entered.encode(), stored_hash):
            print("Login successful!\n")
            return entered  # raw password used for PBKDF2 → Fernet key
        else:
            print("Incorrect password. Try again.\n")

def authenticate_master_password():
    """
    Main entry point used by main.py.
    Determines whether:
    - First-time setup (hash is None)
    - Normal login (hash exists)
    Returns raw master password for key derivation.
    """

    stored_hash, stored_salt = get_master_hash_and_salt()

    # First-time setup (hash is NULL)
    if stored_hash is None:
        return create_master_password()

    # Normal login
    return verify_master_password(stored_hash)
