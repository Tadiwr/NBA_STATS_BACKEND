class TeamModel:

    def __init__(self, team_json) -> None:
        self.team_id = int(team_json["id"])
        self.abbrv = team_json["abbreviation"]
        self.name = team_json["displayName"]
        self.location = team_json["location"]
        self.next_match = team_json["nextEvent"][0]["name"]
        self.next_opponent_id = int(team_json["nextEvent"][0]["competitions"][0]["competitors"][0]["id"])