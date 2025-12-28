## encrypted-password-manager

A Python-based encrypted password manager that securely stores and retrieves login credentials using modern cryptographic techniques.
This project was built as a learning exercise to understand password hashing, key derivation, encryption, and secure local data storage.

--------------------------------------------------------------------------------------------------------

## What this project does
The program allows a user to manage passwords locally using a single master password.

It allows the user to:

- Create a master password on first run
- Authenticate using the master password on subsequent runs
- Add new password entries
- View saved entries without revealing passwords
- Decrypt a specific password entry on demand
- Copy decrypted passwords to the clipboard temporarily
- Delete saved entries

All passwords are encrypted before being stored and are only decrypted in memory when explicitly requested.

--------------------------------------------------------------------------------------------------------

## How it works (high level)

1. The application initializes a local SQLite database if one does not exist.
2. On first run, the user creates a master password.
3. The master password is hashed using bcrypt and stored securely.
4. A cryptographic key is derived from the master password using PBKDF2 and a stored salt.
5. Password entries are encrypted using Fernet symmetric encryption.
6. Encrypted passwords are stored in the database.
7. On login, the master password is verified before allowing access.
8. Decryption occurs only when the user chooses to view a specific entry.

--------------------------------------------------------------------------------------------------------

Project structure
```
encrypted-password-manager/
├── src/
│   ├── auth/
│   │   ├── master_password.py   # Master password creation and authentication
│   │   └── key_manager.py       # PBKDF2 key derivation
│   │
│   ├── crypto/
│   │   └── encryptor.py         # Password encryption and decryption
│   │
│   ├── database/
│   │   ├── init_db.py           # Database initialization
│   │   └── db.py                # Database queries and storage
│   │
│   ├── ui/
│   │   └── cli.py               # Command-line interface
│   │
│   ├── utils/
│   │   ├── clipboard.py         # Clipboard copy with auto-clear
│   │   └── validators.py        # Password strength validation
│
├── main.py                       # Application entry point
├── requirements.txt
├── .gitignore
├── README.md
```
--------------------------------------------------------------------------------------------------------

File explanations

main.py  
Acts as the main entry point of the application.  
It coordinates database setup, authentication, key derivation, and launches the CLI.

--------------------------------------------------------------------------------------------------------

auth/master_password.py  
Handles first-time setup and login:
- Prompts for master password creation
- Enforces password strength
- Hashes passwords using bcrypt
- Verifies passwords on login
  
--------------------------------------------------------------------------------------------------------

## auth/key_manager.py  
Derives a secure encryption key from the master password using PBKDF2 and a stored salt.

--------------------------------------------------------------------------------------------------------

## crypto/encryptor.py  
Handles encryption and decryption of password entries using Fernet.

--------------------------------------------------------------------------------------------------------

## database/init_db.py  
Initializes the SQLite database and creates required tables and salts.

--------------------------------------------------------------------------------------------------------

## database/db.py  
Handles all database interactions including:
- Storing encrypted entries
- Fetching entries
- Deleting entries
  
--------------------------------------------------------------------------------------------------------

## ui/cli.py  
Provides a command-line interface for interacting with the password manager.

--------------------------------------------------------------------------------------------------------

## utils/clipboard.py  
Copies decrypted passwords to the clipboard and clears them automatically after a short delay.

--------------------------------------------------------------------------------------------------------

## utils/validators.py  
Performs basic master password strength validation.

--------------------------------------------------------------------------------------------------------

## Installation / Process

## Clone the repository:
```
git clone https://github.com/YOUR_USERNAME/encrypted-password-manager.git
```
```
cd encrypted-password-manager
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Run the program:
```
python main.py
```
--------------------------------------------------------------------------------------------------------

## Notes and limitations

- This project stores all data locally.
- No cloud syncing or network features are included.
- Database files are generated at runtime and should not be committed.
- Clipboard contents are cleared automatically after a timeout.
- This project is intended for educational purposes.
  
--------------------------------------------------------------------------------------------------------

## License

This project is provided for educational use.
