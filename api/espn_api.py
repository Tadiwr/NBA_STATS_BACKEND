import requests
import json
from model.team_model import TeamModel
from model.games_model import GameModel

class EspnApi:
    teams_url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/"
    scoreboard_url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

    def get_team_json(self, id:int) -> dict:

        team_json = requests.get(self.teams_url + str(id)).text
        team_json = json.loads(team_json)["team"]
        team_model = TeamModel(team_json)

        team_dict = {
            "team_id":team_model.team_id,
            "abbrv":team_model.abbrv,
            "name":team_model.name,
            "location": team_model.location,
            "next_match":team_model.next_match,
        }

        return team_dict
    
    def get_num_games(self):
        scoreboard_json = requests.get(self.scoreboard_url).text
        num_games = json.loads(scoreboard_json)["events"].__len__()
        return num_games

    def get_game(self, index:int):
        scoreboard_json = requests.get(self.scoreboard_url).text
        game_json = json.loads(scoreboard_json)["events"][index]
        model = GameModel(game_json)

        game_dict = {
            "game_id" : model.game_id, 
            "name": model.name, 
            "short_name" : model.short_name, 
            "date" : model.date, 
            "time" : model.time, 
            "status" : model.status,
            "home_team":model.home, 
            "away_team":model.away,
            "home_score":model.home_score, 
            "away_score":model.away_score, 
        }

        return game_dict
