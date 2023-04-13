class GameModel:
    def __init__(self, scoreboard_json) -> None:

        self.name = scoreboard_json["name"]
        self.game_id = scoreboard_json["id"]
        self.short_name = scoreboard_json["shortName"]
        self.date = scoreboard_json["date"].split("T")[0]
        self.time = scoreboard_json["date"].split("T")[1]
        self.status = scoreboard_json["status"]["type"]["description"]
        self.home = scoreboard_json["competitions"][0]["competitors"][0]["team"]["displayName"]
        self.away = scoreboard_json["competitions"][0]["competitors"][1]["team"]["displayName"]
        self.home_score = int(scoreboard_json["competitions"][0]["competitors"][0]["score"])
        self.away_score = int(scoreboard_json["competitions"][0]["competitors"][1]["score"])
            
    

