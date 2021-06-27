# Simple database function

import sqlite3


# Query the DB and Return All Records
def show_all():
    # Connect to database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    # Query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Add a New Record to the Table
def add_one(first, last, email):
    # Connect to database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Delete a record from the Table
def delete_one(id):
    # Connect to database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Add many records from the database
def add_many(list):
    # Connect to database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", list)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

