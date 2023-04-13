print("🔑 Starting ...")
import database.operations as op 
import time

print("🚗 Running main app...")
while True:

    op.insert_all_teams()
    op.insert_games()
    print("😴 Sleeping for 60 seconds...")
    time.sleep(60)
    pass