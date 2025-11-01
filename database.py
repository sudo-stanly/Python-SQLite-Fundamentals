import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#drop a table
c.execute("DROP TABLE customers")
conn.commit()

#query database
c.execute("SELECT rowid,* FROM customers")
items = c.fetchall()
for item in items:
    print(item)

print("\ncommand executed sucessfully...")
conn.commit()
conn.close()