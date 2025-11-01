import os

if os.path.exists("./Fundamentals"):
    
    from Fundamentals import database
    if os.path.exists("./Fundamentals/database.py"):

        #delete record use id as string
        database.delete_one(str(6))
        
        #display result
        database.show_all()
        
    else:
        print("File not found.")
else:
    print("Path not found.")
