# SQLite Databases with Python
# Query the db

import sqlite3
from pprint import pprint

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the Database
c.execute("SELECT * FROM customers")

# pprint(f'{c.fetchall()}')
item = c.fetchall()
for items in item:
    print(f'{items}')

print(f'\nCommand executed successfully')
# Commit our command
conn.commit()

# Close our connection
conn.close()
