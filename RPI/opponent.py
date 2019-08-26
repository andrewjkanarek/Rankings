
# Each Team object t will have a dictionary of all opponents they faced in a season
class Opponent:
	def __init__(self, name):
		self.name = name
		# number of times t defeated Opponent
		self.win_count = 0 
		# number of times Opponent defeated t
		self.lose_count = 0