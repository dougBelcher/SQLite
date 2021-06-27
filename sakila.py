# SQLite3
import sqlite3


def tables_in_sqlite_db(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [
        v[0] for v in cursor.fetchall()
        if v[0] != "sqlite_sequence"
    ]
    cursor.close()
    return tables


# Open database
conn = sqlite3.connect('skila.db')
# List tables
tables = tables_in_sqlite_db(conn)

# Your code goes here!
# Example:
print(f'Table: {tables}')           # prints ['commands', 'packages']
