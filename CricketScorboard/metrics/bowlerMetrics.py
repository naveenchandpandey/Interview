from metrics import Metrics


class BowlerMetrics(Metrics):
    economy: float = 0.0
    overs: int = 0
    maiden: int = 0
    wickets: int = 0
    dot_balls: int = 0

    def __str__(self):
        self.economy = round(self.score * 6 / (self.balls if self.balls else 1), 1)
        return str(self.score) + " " + str(self.wickets) + " " + str(self.overs) + " " + str(self.maiden) \
               + " " + str(self.dot_balls) + " " + str(self.economy)
