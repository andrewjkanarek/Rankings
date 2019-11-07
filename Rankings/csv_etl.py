import numpy as np
import pandas as pd
import datetime as dt

# api connecting the bball database
import apis.bball_db_api as api

filepath = '/Users/AndrewKanarek/Desktop/Tech/Rankings/Data/Games/ncaamb_gamerts.csv'

games = pd.read_csv(filepath, names=['AwayTeam', 'AwayScore', 'HomeTeam', 'HomeScore', 'Location', 'Blank1', 'MonthDay', 'Year'])

# Update/clean team names
games["HomeTeam"] = games["HomeTeam"].str.replace("'", "")
games["HomeTeam"] = games["HomeTeam"].str.title().str.strip()
games["AwayTeam"] = games["AwayTeam"].str.replace("'", "")
games["AwayTeam"] = games["AwayTeam"].str.title().str.strip()

# parse date format into datetime
games["Date"] = pd.to_datetime(games["MonthDay"].str.cat(games["Year"].astype(str), sep=' '))

# update season - games in nov/dec 2018 are for the 2019 season, all other 2019 games are for 2019 season
nov_dec_games = games["Date"].dt.month >= 11
games.loc[nov_dec_games, "Season"] = games["Date"].dt.year + 1
games.loc[~nov_dec_games, "Season"] = games["Date"].dt.year

# check if games are neutral - neutral if no location specified
games["IsNeutral"] = ~games["Location"].isnull()

# map team name to teamid
teams = {}

api = api.BballApi()

# insert any missing teams into database
unique_teams = pd.concat([games["HomeTeam"], games["AwayTeam"]]).unique()
for team_name in unique_teams:
	# insert into database
	print("inserting '{}' into DB".format(team_name))
	team_id = api.insert_team(team_name)
	teams[team_name] = team_id

# insert game data into database
for index, row in games.iterrows():
	home_team_id = teams[row["HomeTeam"]]
	away_team_id = teams[row["AwayTeam"]]
	api.create_game(home_team_id, away_team_id, row)

api.db.commit()

