import pandas as pd

def solution_station_5(name):
    df = pd.read_excel("NameGroup.xlsx")
    team_nr = df["Team"][df["Name"].isin([name])]
    return team_nr