from match import Match
from players.batter import Batter
from players.bowler import Bowler


first_team_batters = []
second_team_batters = []
first_team_bowlers = []
second_team_bowlers = []
first_team = ['P1', 'P2', 'P3', 'P4', 'P5']
second_team = ['P6', 'P7', 'P8', 'P9', 'P10']
for i in range(len(first_team)):
    first_team_batters.append(Batter(i))
    second_team_batters.append(Batter(i))
    first_team_bowlers.append(Bowler(i))
    second_team_bowlers.append(Bowler(i))
match = Match()
match.start_innings(players=first_team_batters,
                    overs=2,
                    bowlers=second_team_bowlers,
                    runs=[['1', '4', '1', 'W', '1', '2'],
                          ['1', '2', '3', 'Wd', 'W', 'W', '4', '1']],
                    batting_order=first_team,
                    bowling_order=second_team)
first_innings_score = match.total_score

match.start_innings(players=second_team_batters,
                    overs=2,
                    bowlers=first_team_bowlers,
                    runs=[['1', '4', '2', 'W', '1', '2'], ['W', 'W', 'W', 'W']],
                    batting_order=second_team,
                    bowling_order=first_team)
second_innings_score = match.total_score

if first_innings_score > second_innings_score:
    print("First team won by " + str(first_innings_score - second_innings_score) + " runs")
elif first_innings_score < second_innings_score:
    print("Second team won by " + str(second_innings_score - first_innings_score) + " runs")
else:
    print("It's a tie")
