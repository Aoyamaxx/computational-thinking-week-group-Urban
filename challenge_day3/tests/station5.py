import pandas as pd

def solution_station_5(name):
    df = pd.read_excel("/Users/aoyamaxx/Desktop/Repo/computational-thinking-week-group-Urban/challenge_day3/tests/NameGroup.xlsx")
    team_nr = df["Team"][df["Name"].isin([name])]
    return int(team_nr)