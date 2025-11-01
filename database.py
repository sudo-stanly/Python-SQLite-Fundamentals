import sqlite3

conn = sqlite3.connect('customer.db')


#create a cursor
c = conn.cursor()

#insert a record in table
c.execute("INSERT INTO customers VALUES('Mary','Poppins','mpoppins@email.com')")

print("command executed sucessfully...")
conn.commit()
conn.close()