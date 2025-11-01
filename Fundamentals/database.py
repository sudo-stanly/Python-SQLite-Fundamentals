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