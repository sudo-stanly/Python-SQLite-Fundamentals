import sqlite3

conn = sqlite3.connect('customer.db')


#create a cursor
c = conn.cursor()


#create a table
c.execute("""
    CREATE TABLE customers(
        first_name text,
        last_name text,
        EMAIL text
    );
""")

conn.commit()
conn.close()