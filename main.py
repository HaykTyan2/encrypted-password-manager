# src/main.py

from src.database.init_db import initialize_database
from src.auth.master_password import authenticate_master_password
from src.auth.key_manager import derive_key
from src.ui.cli import run_cli

def main():
    # 1. Build database if missing
    initialize_database()

    # 2. Login or first-time creation
    master_pw = authenticate_master_password()

    # 3. Derive encryption key via PBKDF2
    key = derive_key(master_pw)

    # 4. Launch UI
    run_cli(key)


if __name__ == "__main__":
    main()
