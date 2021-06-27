# SQLite Databases with Python
# Order by records

import sqlite3
from pprint import pprint

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Order by the Database
c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

items = c.fetchall()

for item in items:
    print(f'{item}')

print(f'\nCommand executed successfully')
# Commit our command
conn.commit()

# Close our connection
conn.close()
