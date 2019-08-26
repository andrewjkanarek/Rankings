
class Team:
	def __init__(self, name):
		self.name = name
		self.score = .25
		self.games_won = []
		self.games_lost = []

	def addWin(self, opponent):
		self.games_won.append(opponent)

	def addLoss(self, opponent):
		self.games_lost.append(opponent)








