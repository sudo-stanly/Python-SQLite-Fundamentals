import os

if os.path.exists("./Fundamentals"):
    
    from Fundamentals import database
    if os.path.exists("./Fundamentals/database.py"):

        #lookup email address record
        database.email_lookup("john@codemy.com")
        
    else:
        print("File not found.")
else:
    print("Path not found.")
