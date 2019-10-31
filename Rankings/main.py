import numpy as np
import pandas as pd
import datetime as dt

# api connecting the bball database
import apis.bball_db_api as api

filepath = '/Users/AndrewKanarek/Desktop/Tech/Rankings/Data/Games/ncaamb_gamerts_200.csv'

games = pd.read_csv(filepath, names=['HomeTeam', 'HomeScore', 'AwayTeam', 'AwayScore', 'Location', 'Blank1', 'MonthDay', 'Year'])

# Update team names
games["HomeTeam"] = games["HomeTeam"].str.replace("'", "")
games["HomeTeam"] = games["HomeTeam"].str.title().str.strip()
games["AwayTeam"] = games["AwayTeam"].str.replace("'", "")
games["AwayTeam"] = games["AwayTeam"].str.title().str.strip()

# parse date format
games["Date"] = pd.to_datetime(games["MonthDay"].str.cat(games["Year"].astype(str), sep=' '))

# games in nov/dec 2018 are for the 2019 season, all other 2019 games are for 2019 season
nov_dec_games = games["Date"].dt.month >= 11
games.loc[nov_dec_games, "Season"] = games["Date"].dt.year + 1
games.loc[~nov_dec_games, "Season"] = games["Date"].dt.year

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
	# check if the game exists in the database already
	if (api.check_game_exists(teams[row["HomeTeam"]], teams[row["AwayTeam"]], row["Date"])):
		continue

	home_game_stats_id = api.insert_team_game_stats(teams[row["HomeTeam"]], row["HomeScore"])
	away_game_stats_id = api.insert_team_game_stats(teams[row["AwayTeam"]], row["AwayScore"])

	print("Inserting game between {home_team} and {away_team} on {date}".format(home_team=row["HomeTeam"], away_team=row["AwayTeam"], date=str(row["Date"])))
	is_neutral_game = row["Location"] is not None
	api.insert_game(row["Season"], home_game_stats_id, away_game_stats_id, None, is_neutral_game, row["Date"])

api.db.commit()

