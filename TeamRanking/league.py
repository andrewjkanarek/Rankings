from team import *
from game import *
import operator
import copy

damp = .85

def getSortedTeamsByWins(teams):
	sorted_teams = sorted(teams, key = lambda name: len(teams[name].games_won), reverse=True)
	return sorted_teams

def getSortedTeamsByScore(teams):
	sorted_teams = sorted(teams, key = lambda name: teams[name].score, reverse=True)
	return sorted_teams

def divideScoresByHighest(teams, team_with_highest_score):
	high_score = teams[team_with_highest_score].score
	# divide each team's score by the highest score so all scores are [0-1]
	for team_name in teams:
		teams[team_name].score = teams[team_name].score / high_score

def normalizeScores(self):
	lowest_score = 0
	highest_score = 0
	team_with_highest_score = None

	# for each team, find the lowest score (< 0) and the team with the highest score
	for team_name in self.teams:
		score = self.teams[team_name].score
		# set the lowest score
		if (score < 0 and score < lowest_score):
			lowest_score = score
		# get the team with the highest score
		if (score > highest_score):
			highest_score = score
			team_with_highest_score = team_name

	print "lowest_score: " + str(lowest_score)
	# add the lowest score to all scores so the lowest score is 0
	if (lowest_score < 0):
		for team_name in self.teams:
			self.teams[team_name].score += abs(lowest_score)

	divideScoresByHighest(self.teams, team_with_highest_score)

class League:

	def __init__(self):
		#dictionary {key: team_name value: Team (list of games won, list of games lost, current ranking)}
		self.teams = {} 
		self.num_games = 0;

	def addGame(self, winning_team_name, losing_team_name):
		
		if (winning_team_name in self.teams):
			winning_team = self.teams[winning_team_name]
		else:
			winning_team = Team(winning_team_name)
			self.teams[winning_team_name] = winning_team
		if (losing_team_name in self.teams):
			losing_team = self.teams[losing_team_name]
		else:
			losing_team = Team(losing_team_name)
			self.teams[losing_team_name] = losing_team
		self.num_games += 1

		self.teams[winning_team_name].addWin(losing_team_name)
		self.teams[losing_team_name].addLoss(winning_team_name)


	def getTeamWins(self, name):
		if (name in self.teams):
			return len(self.teams[name].games_won)
		return 0


	def printTeams(self):
		# t = getSortedTeamsByName(self.teams)
		print '***** TEAMS *****'
		for name in self.teams:
			print name

	def getNumGames(self):
		return self.num_games

	def getNumTeams(self):
		return len(self.teams)

	def printRecords(self):
		sorted_teams = getSortedTeamsByWins(self.teams)
		print '***** RECORDS *****'
		for team_name in sorted_teams:
			print '%s: %d,%d' % (team_name, len(self.teams[team_name].games_won), len(self.teams[team_name].games_lost))

	def initializeScores(self):
		high_score = 0
		team_with_highest_score = None
		for team_name in self.teams:
			num_won = len(self.teams[team_name].games_won)
			num_lost = len(self.teams[team_name].games_lost)
			# initialize score to games won divided by games lost 
			# more wins and less losses will result in higher score
			if num_lost == 0:
				score = len(self.teams[team_name].games_won)
			else:
				if num_won == 0:
					score = 0
				else:
					score = float(num_won) / num_lost
				

			# keep track of initial high score
			if score > high_score:
				high_score = score
				team_with_highest_score = team_name

			self.teams[team_name].score = score

		# divide all scores by highest score
		# all scored will be between 0-1 and will still be relative
		divideScoresByHighest(self.teams, team_with_highest_score)



	def printScores(self):
		sorted_teams = getSortedTeamsByScore(self.teams)
		print '***** SCORES *****'
		for team_name in sorted_teams:
			print '%s: %f' % (team_name, self.teams[team_name].score)

	def updateScores(self):
		temp_teams = copy.deepcopy(self.teams)
		for team_name in self.teams:
			print "TEAM: " + team_name
			x = (1 - damp) / len(temp_teams)
			curr_sum = 0
			add = 0
			sub = 0
			# increase the score for every team B that the current team defeated
			# the more teams that team B lost to, the less the current team's score should increase
			for defeated_team_name in temp_teams[team_name].games_won:
				num_games_lost = len(temp_teams[defeated_team_name].games_lost)
				score = temp_teams[defeated_team_name].score
		 		add += (score / num_games_lost)
		 	# decrease the score for every team C the current team lost to
		 	# the more teams that team C defeated, the less the current team's score should decrease
		 	for winning_team_name in temp_teams[team_name].games_lost:
		 		sub +=  ( (1 - temp_teams[winning_team_name].score) / len(temp_teams[winning_team_name].games_won) )

		 	curr_sum = add - sub
		 	curr_sum *= damp
		 	curr_sum += x
		 	print "new score: " + str(curr_sum)
		 	self.teams[team_name].score = curr_sum

		normalizeScores(self)












