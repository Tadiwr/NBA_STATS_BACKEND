class StatsModel:
    
    def __init__(self, defence, offense, record, id) -> None:
        self.field_goals = offense[5]["value"]
        self.free_throw_perc = offense[7]["value"]
        self.off_rebounds = offense[10]["value"]
        self.def_rebounds = defence[1]["value"]
        self.three_point_perc = offense[13]["value"]
        self.blocks = defence[0]["value"]
        self.steals = defence[2]["value"]
        self.team_id = id
        self.wins = record[-1]["value"]
        self.streak = record[16]["value"]
        self.points_for = record[15]["value"]
        self.points_against = record[14]["value"]
        self.loses = record[10]["value"]
        self.win_percentage = record[9]["value"]
        self.points_per_game = record[3]["value"]
        

    def factory(self) -> dict:
        return  {
            "team_id": self.team_id,
            "wins":self.wins,
            "streak":self.streak,
            "loses":self.loses,
            "field_goal_pct": self.field_goals,
            "free_throw_pct":self.free_throw_perc,
            "offensive_rebs":self.off_rebounds,
            "defensive_rebs":self.def_rebounds,
            "three_point_pct":self.three_point_perc,
            "points scored":self.points_for,
            "points conceded":self.points_against,
            "win_percentage":self.win_percentage,
            "points_per_game":self.points_per_game,   
            "blocks":self.blocks,
            "steals":self.steals
        }