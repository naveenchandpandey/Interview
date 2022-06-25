from players.player import Player
from metrics.batterMetrics import BatterMetrics


class Batter(Player, BatterMetrics):
    def switch_striker(self, striker, non_striker):
        temp = striker
        striker = non_striker
        non_striker = temp
        return striker, non_striker

    def next_striker(self, striker, non_striker):
        if striker.order > non_striker.order:
            striker_index = striker.order + 1
        else:
            striker_index = non_striker.order + 1
        return striker_index
