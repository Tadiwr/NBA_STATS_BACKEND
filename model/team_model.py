class TeamModel:

    def __init__(self, team_json) -> None:
        self.team_id = int(team_json["id"])
        self.abbrv = team_json["abbreviation"]
        self.name = team_json["displayName"]
        self.location = team_json["location"]
        self.next_match = team_json["nextEvent"][0]["name"]

    def factory(self):

        return {
            "team_id":self.team_id,
            "abbrv":self.abbrv,
            "short_name":self.name,
            "location": self.location,
            "next_match":self.next_match,
        }