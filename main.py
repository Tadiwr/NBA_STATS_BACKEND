print("\033c", end='')
print("🔑 Starting ...")
import database.operations as op 
import time


print("🚗 Running main app...")
while True:
    # add time delay after every 60 seconds
    op.insert_all_teams()
    op.insert_games()
    print("😴 Sleeping for 60 seconds...")
    time.sleep(60)
    print("\033c", end='')
    # insert data
    pass