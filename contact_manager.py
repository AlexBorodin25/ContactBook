import sqlite3
import re

DB_FILE = "contacts.db"

def get_db_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    with get_db_conn() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,)
        """
        )
        conn.commit()













def menu():
    print("Welcome to Contact Manager")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Update contact")
    print("5. Search for contact")
    print("6. Exit")


