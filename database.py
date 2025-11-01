import sqlite3

conn = sqlite3.connect('customer.db')


#create a cursor
c = conn.cursor()

#insert many record in table
many_customers = [
    ('West', 'Brown', 'wes@brown.com'),
    ('Steph','Keuwa','steph@keuwa.com'),
    ('Dan','Pas','danpas@pas.com')
]
c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)


print("command executed sucessfully...")
conn.commit()
conn.close()