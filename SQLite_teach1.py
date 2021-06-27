# SQLite Databases with Python
# Insert into the db

import sqlite3

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

c.execute("INSERT INTO customers VALUES('John', 'Elder', 'john@codemy.com')")

print(f'Command executed successfully')


# Commit our command
conn.commit()

# Close our connection
conn.close()