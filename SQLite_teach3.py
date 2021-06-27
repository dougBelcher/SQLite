# SQLite Databases with Python
# Insert many records into the db

import sqlite3

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

many_customers = [('Mary', 'Brown', 'mary@codemy.com'),
                  ('Wes', 'Brown', 'wes@codemy.com'),
                  ('Steph', 'Juewa', 'steph@kuea.com'),
                  ('Dan', 'Pas', 'dan@pas.com')]

c.executemany("INSERT INTO customers VALUES(?, ?, ?)", many_customers)

print(f'\nCommand executed successfully')
# Commit our command
conn.commit()

# Close our connection
conn.close()
