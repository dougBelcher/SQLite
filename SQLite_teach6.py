# SQLite Databases with Python
# Updating records

import sqlite3
from pprint import pprint

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Update Records
# c.execute("""UPDATE customers SET first_name = 'John'
#              WHERE last_name = 'Elder'
# """)

# Update Records
# c.execute("""UPDATE customers SET first_name = 'John'
#              WHERE rowid=1
# """)

# Update Records
# c.execute("""UPDATE customers SET first_name = 'Marty'
#              WHERE last_name = 'Brown'
# """)

# Update Records
c.execute("""UPDATE customers SET first_name = 'Wes'
             WHERE rowid = 3
""")
conn.commit()

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
