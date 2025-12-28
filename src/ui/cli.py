# src/ui/cli.py

from database.db import (
    add_entry, get_all_entries, get_entry_by_id, delete_entry
)
from crypto.encryptor import encrypt_password, decrypt_password
from utils.clipboard import copy_to_clipboard

def show_menu():
    print("""
==============================
   PASSWORD MANAGER
==============================
1. Add new password
2. View saved passwords
3. View / decrypt one entry
4. Delete entry
5. Exit
""")

def run_cli(key):
    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            site = input("Site: ")
            username = input("Username: ")
            pw = input("Password: ")

            encrypted = encrypt_password(pw, key)
            add_entry(site, username, encrypted)
            print("Entry saved.\n")

        elif choice == "2":
            rows = get_all_entries()
            print("\nSaved entries:")
            for row in rows:
                print(f"ID: {row[0]}  |  {row[1]}  ({row[2]})")
            print()

        elif choice == "3":
            entry_id = input("ID to decrypt: ")
            data = get_entry_by_id(entry_id)
            if not data:
                print("Not found.\n")
                continue

            site, username, blob = data
            decrypted = decrypt_password(blob, key)

            print(f"\nDecrypted password for {site} ({username}): {decrypted}")

            if input("Copy to clipboard? (y/n): ").lower() == "y":
                copy_to_clipboard(decrypted)

            print()

        elif choice == "4":
            entry_id = input("ID to delete: ")
            delete_entry(entry_id)
            print("Deleted.\n")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice\n")
