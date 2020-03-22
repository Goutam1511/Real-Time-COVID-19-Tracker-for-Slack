from database import dbconnect

db = dbconnect()
for row in db.retrieve_from_db():
    print row
