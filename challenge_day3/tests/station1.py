import pandas as pd

def solution_station_1(position):
    df = pd.read_excel("FibonacciSequence.xlsx")
    team_nr = df["Value"][df["Position"] == position]
    return team_nr