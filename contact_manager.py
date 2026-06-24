import sqlite3
import re

DB_FILE = "contacts.db"

EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
PHONE_PATTERN = r"^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$"

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

def is_email_valid(email):
    return re.match(EMAIL_PATTERN, email) is not None

def is_phone_valid(phone):
    return re.match(PHONE_PATTERN, phone) is not None

def prompt_email():
    while True:
        email = input("Enter your email address: ").strip()

        if is_email_valid(email):
            return email

        print("Enter a valid email address.")

def prompt_phone():
    while True:
        phone = input("Enter your phone number: ").strip()

        if is_phone_valid(phone):
            return phone

        print("Enter a valid phone number.")

def add_contact():\
    print('Ad Contact')

    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    phone = prompt_phone()
    email = prompt_email()

    with get_db_conn() as conn:
        conn.execute(
            """INSERT INTO contacts (name, email, phone)
                VALUES (?, ?, ?)""",
            (name, email, phone),
        )
        conn.commit()

    print("Contact added!")














def menu():
    print("Welcome to Contact Manager")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Update contact")
    print("5. Search for contact")
    print("6. Exit")


