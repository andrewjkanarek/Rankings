import numpy as np
import pandas as pd

# api connecting the bball database
import apis.bball_db_api as api

def get_teams(games):
	# dataframe to keep track of record and score for each team 
	teams = pd.DataFrame(
		index=pd.concat([games["Winner"], games["Loser"]]).unique(), 
		columns=['Name', 'NumWins', 'NumLosses', 'Score'])
	teams.index.name = "Name"
	teams["Name"] = pd.concat([games["Winner"], games["Loser"]]).unique()

	for team_name, team in teams.iterrows():
		team["NumWins"] = int(len(games[games["Winner"] == team_name]))
		team["NumLosses"] = int(len(games[games["Loser"] == team_name]))
	teams = teams.astype({"NumWins": "int32"})
	teams = teams.astype({"NumLosses": "int32"})
	teams["Score"] = teams["NumWins"] / (teams["NumWins"] + teams["NumLosses"])

	return teams

def update_scores(games, teams, x):
	# print(teams.loc["Name", "NumWins"])
	teams_updated = teams.copy()

	# update score for each team
	for team_name, team in teams_updated.iterrows():

		# get all of the games for the current team
		team_wins = games[games["Winner"] == team_name]
		team_losses = games[games["Loser"] == team_name]

		curr_sum = 0
		add = 0
		sub = 0

		# iterate through games won
		for opponent_name in team_wins["Loser"]:
			opponent = teams.loc[opponent_name]
			add += opponent["Score"] / opponent["NumLosses"]

		# iterate through games lost
		for opponent_name in team_losses["Winner"]:
			opponent = teams.loc[opponent_name]
			sub += (1 - opponent["Score"]) / opponent["NumWins"]

		curr_sum = add - sub
		curr_sum *= damp
		curr_sum += x
		teams_updated.loc[team_name, "Score"] = curr_sum

	return teams_updated.copy()



def normalize_scores(teams):

	# min score should be 0
	lowest_score = teams["Score"].min()
	if (lowest_score < 0):
		teams["Score"] += abs(lowest_score)

	# max score should be 1
	highest_score = teams["Score"].max()
	teams["Score"] /= highest_score


	return teams

def predict(games, teams, start_date, end_date):

	right = 0
	wrong = 0
	for index, game in games.iterrows():
		winner = teams.loc[game["Winner"]]
		loser = teams.loc[game["Loser"]]

		if (winner["Score"] > loser["Score"]):
			right += 1
		else:
			wrong += 1

	percentage = (right / (right + wrong)) * 100

	print("percentage: {}%, right: {}, wrong: {}".format(percentage, right, wrong))


api = api.BballApi()

damp = .85
season = 2017
start_date = '2016-03-01'
end_date = '2017-03-01'
games = api.get_games_df(season, end_date)

# initialize scores with win %

teams = get_teams(games)

print(teams.sort_values('Score', ascending=False).head(10))

predict(games, teams, None, None)

# update scores with pagerank

x = (1 - damp) / teams.shape[0]

teams = update_scores(games, teams, x)

teams = normalize_scores(teams)

print(teams.sort_values('Score', ascending=False).head(10))

predict(games, teams, None, None)

teams = update_scores(games, teams, x)

teams = normalize_scores(teams)

print(teams.sort_values('Score', ascending=False).head(10))

predict(games, teams, None, None)



