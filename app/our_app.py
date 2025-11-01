import os

if os.path.exists("./Fundamentals"):
    
    from Fundamentals import database
    if os.path.exists("./Fundamentals/database.py"):

        
        #add many records
        stuff=[
            ('Brenda','Smitherton','brenda@smitherton.com'),
            ('Joshua','Raintree','josh@raintree.com')
        ]
        database.add_many(stuff)
        
        #display result
        database.show_all()
        
    else:
        print("File not found.")
else:
    print("Path not found.")
