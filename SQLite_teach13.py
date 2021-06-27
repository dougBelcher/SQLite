import database

# Add a record to the database
# database.add_one("Laura", "Smith", "laura@smith.com")

# Delete a record from the database
# database.delete_one('6')

# add many records to the database
stuff = [
    ('Brenda', 'Smitherson', 'brenda@smithercon.com'),
    ('Joshua', 'Raintree', 'joshua@raintree.com')
        ]
database.add_many(stuff)

# Show all the records in the database
database.show_all()
