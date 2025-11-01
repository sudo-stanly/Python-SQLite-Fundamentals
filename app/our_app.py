import os

if os.path.exists("./Fundamentals"):
    
    from Fundamentals import database
    if os.path.exists("./Fundamentals/database.py"):
        
        # start here
        database.show_all()
        
    else:
        print("File not found.")
else:
    print("Path not found.")
