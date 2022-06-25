from players.batter import Batter
from players.bowler import Bowler
from exceptions import DataMismatchException, InvalidValueException
from static import BOWLER_METRICS, BATTER_METRICS


class Match:
    total_score: int
    striker: Batter
    non_striker: Batter
    bowler: Bowler
    dismissed: int
    batting_order: list
    bowling_order: list

    def modify_score(self, run: int) -> None:
        self.striker.score += run
        self.striker.balls += 1
        self.bowler.score += run
        self.bowler.balls += 1
        self.total_score += run

    def start_innings(self, players: list, overs: int, bowlers, runs: list, batting_order: list,
                      bowling_order: list) -> None:
        if len(players) < 2 or overs <= 0 or len(runs) == 0:
            raise InvalidValueException(players)
        self.striker = players[0]
        self.non_striker = players[1]
        self.dismissed = 0
        self.total_score = 0
        self.batting_order = batting_order
        self.bowling_order = bowling_order
        self.bowler = bowlers[0]

        if len(runs) != overs:
            raise DataMismatchException

        self.iterate_overs(players, overs, bowlers, runs)

    def iterate_overs(self, players: list, overs: int, bowlers: list, runs: list) -> None:
        bowler_index = 0
        innings_over = False
        for over in range(overs):
            maiden = True
            for run in runs[over]:
                if run in ('Wd', 'Nb'):
                    self.total_score += 1
                    maiden = False
                elif run == 'W':
                    self.dismissed += 1
                    self.bowler.wickets += 1
                    self.striker.balls += 1
                    self.bowler.balls += 1
                    self.bowler.dot_balls += 1
                    if self.dismissed == len(players) - 1:
                        self.bowler.overs += (self.bowler.balls % 6) / 10
                        innings_over = True
                        break
                    striker_index = self.striker.next_striker(self.striker, self.non_striker)
                    self.striker = players[striker_index]
                elif run.isdigit():
                    run = int(run)
                    if run > 0:
                        maiden = False
                    if run == 0:
                        self.bowler.dot_balls += 1
                    if run % 2 != 0:
                        self.modify_score(run)
                        self.striker, self.non_striker = self.striker.switch_striker(self.striker, self.non_striker)
                    else:
                        if run % 4 == 0:
                            self.striker.fours += 1
                        elif run % 6 == 0:
                            self.striker.sixes += 1
                        self.modify_score(run)
                else:
                    raise InvalidValueException(run)
            if not innings_over:
                self.striker, self.non_striker = self.striker.switch_striker(self.striker, self.non_striker)
                self.bowler.overs += 1
                if maiden:
                    self.bowler.maiden += 1

            print("Over", over + 1, "statistics:")
            print(", ".join(BATTER_METRICS))
            for order, player in zip(self.batting_order, players):
                if (player.order == self.striker.order and not innings_over) or player.order == self.non_striker.order:
                    order += '*'
                print(order, player)
            print("----------------------------------------------------------------")
            print(", ".join(BOWLER_METRICS))
            for order, player in zip(self.bowling_order, bowlers):
                if self.bowler.order == player.order:
                    order += '*'
                print(order, player)
            print("================================================================")
            print("Total Score: ", self.total_score, "/", self.dismissed)

            if innings_over:
                break

            bowler_index = self.bowler.next_bowler(bowler_index, bowlers)
            self.bowler = bowlers[bowler_index]

