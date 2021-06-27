# SQLite Databases with Python
# Primary key

import sqlite3
from pprint import pprint

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the Database
c.execute("SELECT rowid, * FROM customers")

item = c.fetchall()
for items in item:
    print(f'{items}')

print(f'\nCommand executed successfully')
# Commit our command
conn.commit()

# Close our connection
conn.close()
