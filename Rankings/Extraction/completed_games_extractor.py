from csv import reader

import models.game_raw

class CompletedGamesExtractor:

	def __init__(self, filepath):
		self.filepath = filepath

	def extract(self):

		games_raw = []

		# Read the csv file containing game data
		with open(self.filepath) as csvfile:
			read_file = reader(csvfile)
			games = list(read_file)

			for row in games:

				# initialize game with each row
				game_raw = GameRaw(row) 

				# validate 
				game_raw.validate()

				# add game to row to list of games
				games_raw.append(game_raw.row_data)


			return games_raw