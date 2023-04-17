class StatsModel:
    
    def __init__(self, defence, offense) -> None:
        self.field_goals = offense[5]
        self.free_throw_perc = offense[7]
        self.off_rebounds = offense[10]
        self.def_rebounds = defence[1]
        self.three_point_perc = offense[13]
        self.points = offense[11]
        self.blocks = defence[0]
        self.steals = defence[2]