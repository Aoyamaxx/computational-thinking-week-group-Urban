import pandas as pd

def solution_station_1(position):
    df = pd.read_excel("/Users/aoyamaxx/Desktop/Repo/computational-thinking-week-group-Urban/challenge_day3/tests/FibonacciSequence.xlsx")
    team_nr = df["Value"][df["Position"] == position]
    return int(team_nr)

solution_station_1(76)