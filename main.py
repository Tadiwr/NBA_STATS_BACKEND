print("🔑 Starting ...")
import database.operations as op 
import time
from colorama import Fore, Back, Style


print("🚗 Running main app...")
while True:
    op.insert_all_teams()
    op.insert_games()
    op.insert_all_summary_stats()
    op.color_print("😴 Sleeping for 60 seconds...", Fore.CYAN)
    time.sleep(60)
    pass