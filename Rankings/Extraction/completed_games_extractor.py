from game_raw import GameRaw

class CompletedGamesExtractor:

	def __init__(self, filepath):
		self.filepath = filepath

	def extract(self):

		games_raw = []

		# open file
		with open(self.filepath, 'rb') as csvfile:

			for count, line in enumerate(csvfile):
				cols = line.split(',')

				# initialize game with each row
				game_raw = GameRaw(cols) 

				# validate 
				game_raw.validate()

				# add game to row to list of games
				games_raw.append(game_raw.row_data)

		return games_raw