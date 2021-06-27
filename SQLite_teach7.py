# SQLite Databases with Python
# Deleting records

import sqlite3
from pprint import pprint

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Delete Records
c.execute("""DELETE FROM customers WHERE rowid=2
""")

conn.commit()

# Query the Database
c.execute("SELECT rowid, * FROM customers")

pprint(f'{c.fetchall()}')


print(f'Command executed successfully')
# Commit our command
conn.commit()

# Close our connection
conn.close()
