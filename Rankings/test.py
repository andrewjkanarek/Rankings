import pymongo
import datetime as dt
from csv import reader

from extraction.completed_games_extractor import CompletedGamesExtractor
from database.bballsql.db import BballDb
import apis.bball_db_api as api
import models.data_transformer



# connect to db

# bball_db = BballDb()
# bball_db.connect()


# read from file

# path = '/Users/AndrewKanarek/Desktop/Tech/Rankings/Data/Games/ncaamb_gamerts_200.csv'

# completed_games_extractor = CompletedGamesExtractor(path);
# games_raw = completed_games_extractor.extract()

# insert into raw SQL tables

# api.insert_raw_games(bball_db, games_raw)

# clean and convert data

# bball_db.disconnect()


path = '/Users/AndrewKanarek/Desktop/Tech/Rankings/Data/Games/ncaamb_gamerts_200.csv'


api = api.BballApi()

# Read the csv file containing game data
with open(path) as csvfile:
	read_file = reader(csvfile)
	games_input = list(read_file)

	for row in games_input:
		home_team_name = row[0]
		home_team_score = row[1]
		away_team_name = row[2]
		away_team_score = row[3]
		monthday = row[6]
		year = row[7]

		# validate, trim, transform to data type
		home_team_name = home_team_name.strip().title().replace("'", "\'")
		away_team_name = away_team_name.strip().title().replace("'", "\'")

		home_team_score = int(home_team_score)
		away_team_score = int(away_team_score)

		date = monthday + " " + year
		date = dt.datetime.strptime(date, "%b %d %Y")

		# insert into database
		hometeamid = api.insert_team(home_team_name.strip().title())
		awayteamid = api.insert_team(away_team_name.strip().title())






