# src/crypto/encryptor.py

from cryptography.fernet import Fernet


def encrypt_password(plaintext: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(plaintext.encode())


def decrypt_password(token: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(token).decode()
