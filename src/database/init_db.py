import sqlite3
import secrets
from pathlib import Path

#__file__ contains the exact file path of the script that is currently running.
#__file__ → "/home/user/project/src/database/init_db.py"

DB_PATH = Path(__file__).parent / "password_manager.db"

def initialize_database():
  if DB_PATH.exists():
    return
  
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  cursor.execute("""
    CREATE TABLE master_password (
      id INTEGER PRIMARY KEY,
      hash TEXT,
      salt BLOB
    )
  """)

  cursor.execute("""
    CREATE TABLE entries (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      site TEXT NOT NULL,
      username TEXT NOT NULL,
      encrypted_password BLOB NOT NULL
    )
  """)

  # ----- Generate PBKDF2 salt -----
  # 16–32 bytes is standard; here we use 16 bytes
  salt = secrets.token_bytes(16)

  # Insert salt with hash=NULL (first-time setup)
  cursor.execute("""
      INSERT INTO master_password (hash, salt)
      VALUES (?, ?)
  """, (None, salt))

  conn.commit()
  conn.close()