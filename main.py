from database.mongo import MongoDB
import database.operations as op 
import time

print("Running all is good")
while True:
    # add time delay after every 60 seconds
    op.insert_all_teams()
    time.sleep(60)
    # insert data
    pass