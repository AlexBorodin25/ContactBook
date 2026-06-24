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

def view_contacts():
    print("All Contacts")

    with get_db_conn() as conn:
        contacts = conn.execute(
            """SELECT id, name, email, phone FROM contacts ORDER BY name"""
        ).fetchall()

    if not contacts:
        print("No contacts available.")
        return

    for contact in contacts:
        print(
            f"{contact['id']} - {contact['name']} - {contact['phone']} - {contact['email']}"
        )

def update_contact():
    view_contacts()

    try:
        contact_id = int(input("Enter contact ID: "))
    except ValueError:
        print("Enter a valid contact ID.")
        return

    with get_db_conn() as conn:
        contact = conn.execute(
            """SELECT id, name, email, phone FROM contacts WHERE id = ?""",
        ).fetchone()

    if contact is None:
        print("Contact not found.")
        return

    print("Leave the field blank to keep current contact.")

    new_name = input(f"Name [{contact['name']}]: ").strip()
    new_phone = input(f"Phone [{contact['phone']}]: ").strip()
    new_email = input(f"Email [{contact['email']}]: ").strip()

    name = new_name if new_name else contact['name']

    if new_phone:
        if not is_phone_valid(new_phone):
            print("Invalid format.")
            return
        phone = new_phone
    else:
        phone = contact['phone']

    if new_email:
        if not is_email_valid(new_email):
            print("Invalid format.")
            return
        email = new_email
    else:
        email = contact['email']

    with get_db_conn() as conn:
        conn.execute(
            """UPDATE contacts SET name = ?, email = ?, phone = ? WHERE id = ?""",
            (name, email, phone, contact_id),
        )
        conn.commit()

        print("Contact updated.")

def delete_contact():
    view_contacts()

    try:
        contact_id = int(input("Enter contact ID: "))
    except ValueError:
        print("Enter a valid contact ID.")
        return

    with get_db_conn() as conn:
        cursor = conn.execute(
            """DELETE FROM contacts WHERE id = ?""",
            (contact_id,),
        )
        conn.commit()

        if cursor.rowcount == 0:
            print("Contact not found.")
        else:
            print("Contact deleted.")

def search_contact():
    search_value = input("Search by name or phone number: ").strip()

    if not search_value:
        print("Search cannot be empty.")
        return

    with get_db_conn() as conn:
        contacts = conn.execute(
            """SELECT id, name, email, phone
               FROM contacts
               WHERE name LIKE ? OR PHONE LIKE ?
            ORDER BY name
            """,
            (f"%{search_value}%", f"%{search_value}%"),
        ).fetchall()

    if not contacts:
        print("No contacts found.")
        return

    print("Search Results:")
    for contact in contacts:
        print(
            f"{contact['id']} - {contact['name']} - {contact['phone']} - {contact['email']}"
        )


def menu():
    print("Welcome to Contact Manager")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Update contact")
    print("5. Search for contact")
    print("6. Exit")


