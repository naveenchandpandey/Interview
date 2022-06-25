from enum import Enum

BATTER_METRICS = ['Player Name', 'Score', '4s', '6s', 'Balls', 'S/R']
BOWLER_METRICS = ['Player Name', 'Runs', 'Wickets', 'Overs', 'Maiden', 'Dot balls', 'Economy']


class CustomExceptions(Enum):
    InvalidValueException = "Invalid value provided cannot parse"
