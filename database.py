import sqlite3

conn = sqlite3.connect('customer.db')


#create a cursor
c = conn.cursor()

#query the database
c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)
print(c.fetchall())


print("command executed sucessfully...")
conn.commit()
conn.close()