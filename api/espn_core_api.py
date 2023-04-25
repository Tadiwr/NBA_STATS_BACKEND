import datetime
import requests
import json
from model.stats_model import StatsModel
import pandas as pd

class EspnCoreApi:
    # url
    year = datetime.datetime.now().year
    stats_base_url = f"http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/{year}/types/2/teams"

    def get_summary_team_stats(self, team_id:int):
        url = self.stats_base_url + f"/{team_id}/statistics"
        json_string = json.loads(requests.get(url).text)
        offensive = json_string["splits"]["categories"][2]["stats"]
        defensive = json_string["splits"]["categories"][0]["stats"]

        return StatsModel(defensive, offensive, team_id).factory()

    def get_all_off_team_stats(self, team_id:int):
        url = self.stats_base_url + f"/{team_id}/statistics"
        json_string = json.loads(requests.get(url=url).text)
        json_string = json_string["splits"]["categories"][2]["stats"]
        return json_string

    def get_all_def_team_stats(self, team_id:int):
        url = self.stats_base_url + f"/{team_id}/statistics"
        json_string = json.loads(requests.get(url).text)
        return json.dumps(json_string["splits"]["categories"][0]["stats"])
        
        

