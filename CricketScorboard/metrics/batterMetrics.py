from metrics import Metrics


class BatterMetrics(Metrics):
    strike_rate: float = 0.0
    fours: int = 0
    sixes: int = 0

    def __str__(self):
        self.strike_rate = round(self.score / (self.balls if self.balls else 1), 1)
        return str(self.score) + " " + str(self.fours) + " " + str(self.sixes) + " " + str(self.balls) + " " + str(self.strike_rate)