import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#query database - ORDER BY
c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'Br%' OR rowid=3 ")
items = c.fetchall()
for item in items:
    print(item)

print("\ncommand executed sucessfully...")
conn.commit()
conn.close()