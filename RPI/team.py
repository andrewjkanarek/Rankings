from opponent import *

HOME_WIN_WEIGHT = .6
NEUTRAL_WIN_WEIGHT = 1
AWAY_WIN_WEIGHT = 1.4

class Team:
	def __init__(self, name):
		self.name = name
		self.win_count = 0
		self.lose_count = 0
		self.opponents = {} # key: opponent_name value: Opponent object

		# depending on the location of the game, each game is worth a different amount
		# home game is worth .6 (more likely to win) - HOME_WIN_WEIGHT
		# away game is worth 1.4 (less likely to win) - AWAY_WIN_WEIGHT
		# neutral game is worth 1 - NEUTRAL_WIN_WEIGHT
		self.weighted_win_sum = 0 # numerator of WP
		self.weighted_game_sum = 0 # denominator of WP

		self.WP = 0 # win percentage
		self.OWP = 0 # opponent's WP
		self.OOWP = 0 # opponent's opponent's WP
		self.RPI = 0 # total RPI of team


	# update opponent dictionary used to calc OWP & OOWP
	# update weighted sums used to calc WP
	def addWin(self, opponent_name, location):
		# add number of wins to current team
		self.win_count += 1

		# add the opponent to dict of opponents if new opponent
		if not opponent_name in self.opponents:
			opponent = Opponent(opponent_name)
			self.opponents[opponent_name] = opponent
		self.opponents[opponent_name].win_count += 1

		# weight of opponent is added to numerator and denominator of WP after a win
		# won at home
		if location == 'H':
			self.weighted_win_sum += HOME_WIN_WEIGHT
			self.weighted_game_sum += HOME_WIN_WEIGHT
		# won away
		elif location == 'A':
			self.weighted_win_sum += AWAY_WIN_WEIGHT
			self.weighted_game_sum += AWAY_WIN_WEIGHT
		# won on neutral court
		else:
			self.weighted_win_sum += NEUTRAL_WIN_WEIGHT
			self.weighted_game_sum += NEUTRAL_WIN_WEIGHT

	def addLoss(self, opponent_name, location):
		# add number of losses to current team
		self.lose_count += 1

		# add the opponent to dict of opponents if new opponent
		if not opponent_name in self.opponents:
			opponent = Opponent(opponent_name)
			self.opponents[opponent_name] = opponent
		self.opponents[opponent_name].lose_count += 1

		# weight of opponent is added only to denominator of WP after a win
		# lost at home
		if location == 'H':
			self.weighted_game_sum += AWAY_WIN_WEIGHT
		# lost away
		elif location == 'A':
			self.weighted_game_sum += HOME_WIN_WEIGHT
		# lost on neutral court
		else:
			self.weighted_game_sum += NEUTRAL_WIN_WEIGHT

	# calculates the WP (winning percentage)
	def calcWP(self):
		if (self.weighted_game_sum == 0):
			self.WP = 0
		else:
			self.WP = float(self.weighted_win_sum) / self.weighted_game_sum

	# calculates the OWP (opponent's winning percentage)
	def calcOWP(self, teams):
		num = 0
		for opponent_name in self.opponents:
			# win_count = the number of wins the opponent has EXCEPT against the current team
			win_count = teams[opponent_name].win_count - self.opponents[opponent_name].lose_count
			# num_games = the number of games the opponent played EXCEPT against the current team
			num_games = (teams[opponent_name].win_count + teams[opponent_name].lose_count) - \
						(self.opponents[opponent_name].win_count + self.opponents[opponent_name].lose_count)
			# num_matchups = the total number of times the current team played the current oppoennt
			num_matchups = self.opponents[opponent_name].win_count + self.opponents[opponent_name].lose_count

			# iterate through each matchup in case the team played this opponent more than once
			for i in range(0, num_matchups):
				if (num_games > 0):
					num += float(win_count) / num_games
		den = self.win_count + self.lose_count
		self.OWP = num / den

	# calculates the OOWP (opponent's opponent's winning percentage)
	def calcOOWP(self, teams):
		owp_sum = 0
		for opponent_name in self.opponents:
			num_matchups = self.opponents[opponent_name].win_count + self.opponents[opponent_name].lose_count

			# iterate through each matchup in case the team played this opponent more than once
			for i in range(0, num_matchups):
				owp_sum += teams[opponent_name].OWP

		num_games = self.win_count + self.lose_count
		self.OOWP = owp_sum / num_games


	def calcRPI(self):
		self.RPI = (self.WP * .25) + (self.OWP * .5) + (self.OOWP * .25)


	# used for debugging only
	def printTeam(self):
		print "*********** TEAM " + self.name + "***************"
		print "record: (%s,%s)" % (str(self.win_count), str(self.lose_count)) 
		print "WP: " + str(self.WP)
		print "OWP: " + str(self.OWP)
		print "OOWP: " + str(self.OOWP)
		print "RPI: " + str(self.RPI)
