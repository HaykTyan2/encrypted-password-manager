# src/auth/key_manager.py

import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from database.db import get_master_hash_and_salt


def derive_key(master_password: str) -> bytes:
    """
    Use PBKDF2 + stored salt to derive a 32-byte encryption key.
    Returned key is Fernet-compatible.
    """
    _, salt = get_master_hash_and_salt()
    password_bytes = master_password.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,   # high-security recommendation
    )
    #you feed the machine (KDF object) a password, and it outputs a raw_key.
    #raw_key is originally bytes  
    #base64 converts the bytes into a base64 encoded text key and returns for fernet to use
    raw_key = kdf.derive(password_bytes)
    return base64.urlsafe_b64encode(raw_key)
