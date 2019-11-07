import numpy as np
import pandas as pd

# api connecting the bball database
import apis.bball_db_api as api

api = api.BballApi()

season = 2017
start_date = '2016-03-01'
end_date = '2017-03-01'
games = api.get_games_df(season, end_date)

# get all team names (no duplicates)
teams_unique = pd.concat([games["Winner"], games["Loser"]]).unique()

# sum of all home win percentages
home_win_pct_sum = 0
# sum of all away win percentages
away_win_pct_sum = 0

# for each team, calculate their win pct at home and away games
for team_name in teams_unique:

	# get all games played by the team
	team_games = games[(games["Winner"] == team_name) | (games["Loser"] == team_name)]

	# get all home games ("Location" is based on winner's location)
	home_games_bool = ((team_games["Winner"] == team_name) & (team_games["Location"] == "Home")) | ((team_games["Loser"] == team_name) & (team_games["Location"] == "Away"))
	home_games = team_games[home_games_bool]
	home_wins_count = len(home_games[home_games["Winner"] == team_name])
	home_losses_count = len(home_games[home_games["Loser"] == team_name])

	# get all away games
	away_games_bool = ((team_games["Winner"] == team_name) & (team_games["Location"] == "Away")) | ((team_games["Loser"] == team_name) & (team_games["Location"] == "Home"))
	away_games = team_games[away_games_bool]
	away_wins_count = len(away_games[away_games["Winner"] == team_name])
	away_losses_count = len(away_games[away_games["Loser"] == team_name])

	# calculate win pct at home and away
	home_win_pct = home_wins_count / home_games.shape[0]
	away_win_pct = away_wins_count / away_games.shape[0]

	home_win_pct_sum += home_win_pct
	away_win_pct_sum += away_win_pct


# calculate average home and away win percentage
avg_home_win_pct = home_win_pct_sum / len(teams_unique)
avg_away_win_pct = away_win_pct_sum / len(teams_unique)

print("home: {}, away: {}".format(avg_home_win_pct, avg_away_win_pct))
