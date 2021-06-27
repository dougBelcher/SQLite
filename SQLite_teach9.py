# SQLite Databases with Python
#  And/or

import sqlite3
from pprint import pprint

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# And/or on the Database
c.execute("""SELECT rowid, * 
          FROM customers
          WHERE last_name='Brown'
          AND   first_name='Wes' 
          ORDER BY last_name DESC
          """)

items = c.fetchall()

for item in items:
    print(f'{item}')

print(f'\nCommand executed successfully')
# Commit our command
conn.commit()

# Close our connection
conn.close()