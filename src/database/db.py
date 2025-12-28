# src/database/db.py

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "password_manager.db"


def _connect():
    return sqlite3.connect(DB_PATH)


# ---------------------- MASTER PASSWORD ----------------------

def get_master_hash_and_salt():
    """Return (hash, salt) from the master_password table."""
    conn = _connect()
    cur = conn.cursor()

    cur.execute("SELECT hash, salt FROM master_password WHERE id = 1")
    row = cur.fetchone()

    conn.close()
    return row[0], row[1]


def update_master_hash(hashed_pw):
    """Update the bcrypt hash after first-time setup."""
    conn = _connect()
    cur = conn.cursor()

    cur.execute("""
        UPDATE master_password
        SET hash = ?
        WHERE id = 1
    """, (hashed_pw,))

    conn.commit()
    conn.close()


# ---------------------- PASSWORD ENTRIES ----------------------

def add_entry(site, username, encrypted_password):
    conn = _connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO entries (site, username, encrypted_password)
        VALUES (?, ?, ?)
    """, (site, username, encrypted_password))

    conn.commit()
    conn.close()


def get_all_entries():
    conn = _connect()
    cur = conn.cursor()

    cur.execute("SELECT id, site, username FROM entries")
    rows = cur.fetchall()

    conn.close()
    return rows


def get_entry_by_id(entry_id):
    conn = _connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT site, username, encrypted_password
        FROM entries
        WHERE id = ?
    """, (entry_id,))

    row = cur.fetchone()
    conn.close()
    return row


def delete_entry(entry_id):
    conn = _connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
