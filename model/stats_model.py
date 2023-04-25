class StatsModel:
    
    def __init__(self, defence, offense) -> None:
        self.field_goals = offense[5]["value"]
        self.free_throw_perc = offense[7]["value"]
        self.off_rebounds = offense[10]["value"]
        self.def_rebounds = defence[1]["value"]
        self.three_point_perc = offense[13]["value"]
        self.points = offense[11]["value"]
        self.blocks = defence[0]["value"]
        self.steals = defence[2]["value"]

    def factory(self) -> dict:
        return  {
            "field_goal_pct": self.field_goals,
            "free_throw_pct":self.free_throw_perc,
            "offensive_rebs":self.off_rebounds,
            "defensive_rebs":self.def_rebounds,
            "three_point_pct":self.three_point_perc,
            "points":self.points,
            "blocks":self.blocks,
            "steals":self.steals
        }