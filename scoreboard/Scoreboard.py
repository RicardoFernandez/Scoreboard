class Scoreboard:
    def __init__(self):
        self.local_score = "000"
        self.visitor_score = "000"
        self.separator = ":"

    def __str__(self):
        return "{}{}{}".format(self.local_score, self.separator, self.visitor_score)

    def get_local_score(self):
        return self.local_score

    def get_visitor_score(self):
        return self.visitor_score

    def set_local_score(self, score):
        self.local_score = score

    def set_visitor_score(self, score):
        self.visitor_score = score

    def score(self, team, points):
        self.determinate_scorer(team, points)
        return self.__str__()

    def determinate_scorer(self, team, points):
        if team == "local":
            self.score_locals(points)
            return
        self.score_visitors(points)

    def score_visitors(self, points):
        visitor_score = int(self.get_visitor_score())
        visitor_score += points
        str_visitor_score = str(visitor_score).zfill(3)
        self.set_visitor_score(str_visitor_score)
        return self.get_visitor_score()

    def score_locals(self, points):
        local_score = int(self.get_visitor_score())
        local_score += points
        str_locals_score = str(local_score).zfill(3)
        self.set_local_score(str_locals_score)
        return self.get_local_score()
