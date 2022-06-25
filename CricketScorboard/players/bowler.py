from .player import Player
from metrics.bowlerMetrics import BowlerMetrics


class Bowler(Player, BowlerMetrics):
    def next_bowler(self, index: int, bowlers: list) -> int:
        if index < len(bowlers) - 1:
            return index + 1
        else:
            return (index + 1) % len(bowlers)
