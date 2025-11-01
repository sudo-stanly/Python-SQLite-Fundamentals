import sqlite3

conn = sqlite3.connect('customer.db')


#create a cursor
c = conn.cursor()

#query the database
c.execute("SELECT * FROM customers")

items = c.fetchall()
print(" NAME " + "\t\t\tEMAIL\n----------------------- ------------------------")
for item in items:
    # print(item[0] , item[1], "", item[2])
    fullname = item[0] + " " + item[1]
    print(f"| {fullname:20} | {item[2]}")


print("\ncommand executed sucessfully...")
conn.commit()
conn.close()