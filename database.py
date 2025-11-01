import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#update records
c.execute("""
    UPDATE customers SET first_name = 'Wes' WHERE rowid=4
""")
conn.commit()


c.execute("SELECT rowid,* FROM customers")
items = c.fetchall()
for item in items:
    print(item)

print("\ncommand executed sucessfully...")
conn.commit()
conn.close()