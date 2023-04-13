from database.mongo import MongoDB
from repo import Repo as rp
from tqdm import tqdm
import datetime as dt
import json


team_db = MongoDB(
    database="teams",
    collection="teams"
)

games_db = MongoDB(
    database="league",
    collection="games"
)

def load_status_file():
    file = open("status.json", "r")
    return json.loads(file.read())

def write_to_status_file(status: dict):
    file = open("status.json", "w")
    json_str = json.dumps(status)
    file.write(json_str)

def is_teams_data_outdated() -> bool:
    today = str(dt.date.today())
    status = load_status_file()

    return status["teams_last_updated"] != today

# Team Operations

def get_all_teams():
    return team_db.find_all()

def get_team(query_dict:dict):
    return team_db.find(query_dict)

def insert_all_teams():

    if is_teams_data_outdated():
        print("🗑️ Deleted old data")

        team_db.delete_all()

        print("⏳ Inserting new team data.......")

        for id in tqdm(range(1, 31)):
            team = rp.espn.get_team_json(id)
            team_db.insert_one(team)

        print("✅ Deleted all teams and inserted new team data")
        today = str(dt.date.today())
        status = load_status_file()
        status["teams_last_updated"] = today
        write_to_status_file(status)

        # Update status.json
    else:
        print("🥳 Teams were up to date")


# Games Operations

def insert_games():
    is_done = False
    index = 0
    n = rp.espn.get_num_games()
    print("🗑️ Deleted old game data...")
    games_db.delete_all()
    print("⏳ Inserting new data...")
    for index in tqdm(range(0, n)):
        game =rp.espn.get_game(index)
        games_db.insert_one(game)
    print("✅ Done!, games where updated")