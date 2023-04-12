import requests
import json
from model.team_model import TeamModel

class EspnApi:
    teams_url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/"

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
            "next_opp_id":team_model.next_opponent_id
        }

        return team_dict