import sqlite3

#  query the database and return all recods
def show_all():
    # connect to database
    conn = sqlite3.connect('./Fundamentals/customer.db')
    #create a cursor
    c = conn.cursor()

    c.execute("SELECT rowid,* FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)

    print("\ncommand executed sucessfully...")
    conn.commit()
    conn.close()
    

#add a new record to the table
def add_one(first,last,email):
    # connect to database
    conn = sqlite3.connect('./Fundamentals/customer.db')
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES(?,?,?)",(first, last, email))

    print("\ncommand executed sucessfully...")
    conn.commit()
    conn.close()
    

#delete record from table
def delete_one(id):
    # connect to database
    conn = sqlite3.connect('./Fundamentals/customer.db')
    c = conn.cursor()

    c.execute("DELETE FROM customers WHERE rowid=(?)", id)

    print("\ncommand executed sucessfully...")
    conn.commit()
    conn.close()
    
    
#add many
def add_many(list):
        # connect to database
    conn = sqlite3.connect('./Fundamentals/customer.db')
    c = conn.cursor()

    c.executemany("INSERT INTO customers VALUES(?,?,?)",(list))

    print("\ncommand executed sucessfully...")
    conn.commit()
    conn.close()
    
    
#lookup wit where
def email_lookup(email):
    # connect to database
    conn = sqlite3.connect('./Fundamentals/customer.db')
    c = conn.cursor()

    c.execute("SELECT rowid,* FROM customers WHERE email=(?)",(email,))
    items = c.fetchall()
    for item in items:
        print(item)

    print("\ncommand executed sucessfully...")
    conn.commit()
    conn.close()