import os

if os.path.exists("./Fundamentals"):
    
    from Fundamentals import database
    if os.path.exists("./Fundamentals/database.py"):

        #add a record to the db
        database.add_one("Laura","Smith","laura@smith.com")
        
        #show all the records
        database.show_all()
        
    else:
        print("File not found.")
else:
    print("Path not found.")
