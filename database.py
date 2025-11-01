import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")
items = c.fetchall()
for item in items:
    print(item)

print("\ncommand executed sucessfully...")
conn.commit()
conn.close()