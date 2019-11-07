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

def update_scores(games, teams, x, home_adv_weight):
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
		for index, game in team_wins.iterrows():
			opponent = teams.loc[game["Loser"]]
			score = opponent["Score"]

			# update weight based on homefield advantage
			if home_adv_weight > 0 and home_adv_weight < 1:
				# if game was home, easier win, not as signficant
				if (game["Location"] == "Home"):
					score *= (1 - home_adv_weight)
				# if away win, more difficult win
				else:
					score *= home_adv_weight

			add += score / opponent["NumLosses"]


		# iterate through games lost
		for index, game in team_losses.iterrows():
			opponent = teams.loc[game["Winner"]]
			score = opponent["Score"]

			# update weight based on homefield advantage
			if home_adv_weight > 0 and home_adv_weight < 1:
				# if game was away, not as bad of a loss
				if (game["Location"] == "Home"):
					score *= home_adv_weight
				# if home loss, it is a worse loss
				else:
					score *= (1 - home_adv_weight)

			sub += (1 - score) / opponent["NumWins"]

		curr_sum = add - sub
		curr_sum *= damp
		curr_sum += x
		teams_updated.loc[team_name, "Score"] = curr_sum

	return teams_updated



def normalize_scores(teams):

	# min score should be 0
	lowest_score = teams["Score"].min()
	if (lowest_score < 0):
		teams["Score"] += abs(lowest_score)

	# max score should be 1
	highest_score = teams["Score"].max()
	teams["Score"] /= highest_score


	return teams

def predict(games, teams, start_date, end_date, home_adv_weight):

	right = 0
	wrong = 0
	for index, game in games.iterrows():
		winner_score = teams.loc[game["Winner"]]["Score"]
		loser_score = teams.loc[game["Loser"]]["Score"]

		if home_adv_weight > 0 and home_adv_weight < 1:
			if game["Location"] == "Home":
				winner_score *= home_adv_weight
				loser_score *= (1 - home_adv_weight)
			else:
				winner_score *= (1 - home_adv_weight)
				loser_score *= home_adv_weight
			

		if (winner_score > loser_score):
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

# initialize teams DF with wins/losses and initial score 
teams = get_teams(games)
print(teams.sort_values('Score', ascending=False).head(10))
predict(games, teams, None, None, 1)

# update scores with pagerank

x = (1 - damp) / teams.shape[0]

teams = update_scores(games, teams, x, 1)
teams = normalize_scores(teams)
print(teams.sort_values('Score', ascending=False).head(10))
predict(games, teams, None, None, 1)

teams = update_scores(games, teams, x, 1)
teams = normalize_scores(teams)
print(teams.sort_values('Score', ascending=False).head(10))
predict(games, teams, None, None, 1)





