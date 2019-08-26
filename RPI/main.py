import csv
import os
import operator
from team import *


# dict of teams (key: team_name, value: Team object)
teams = {}


# read csv file and initialize data
# each row in csv represents a game
# format of csv row:
#	home_team_name, home_team_score, away_team_name, away_team_score, location (if neutral)
def initializeTeams(filepath):
	with open(filepath, 'rb') as csvfile:
		content = csvfile.readlines()
		for row in content:
			cols = row.split(',')
			has_homefield_adv = True
			# assume if the home team name is blank, the rest of the columns are
			if cols[0].strip():

					# get the columns from the current row
					home_team_name = cols[0]
					home_team_score = cols[1]
					away_team_name = cols[2]
					away_team_score = cols[3]
					location = cols[4]

					# if no location is specified, the home team had homefield advantage
					if location.strip():
						has_homefield_adv = False;

					# add teams to team dict if they do not exist
					if home_team_name not in teams:
						home_team = Team(home_team_name)
						teams[home_team_name] = home_team
					if away_team_name not in teams:
						away_team = Team(away_team_name)
						teams[away_team_name] = away_team
					
					# add the win to home team and loss to away team if home team won
					if home_team_score > away_team_score:
						if has_homefield_adv:
							teams[home_team_name].addWin(away_team_name,  'H')
							teams[away_team_name].addLoss(home_team_name, 'A')
						elif home_team_score > away_team_score:
							teams[home_team_name].addWin(away_team_name,  'N')
							teams[away_team_name].addLoss(home_team_name, 'N')
						else:
							print "Error, invalid input: Teams %s and %s tied which is not allowed" % \
								(home_team_name, away_team_name)

					# add the loss to away team and loss to home team if away team won
					else:
						if has_homefield_adv:
							teams[away_team_name].addWin(home_team_name, 'A')
							teams[home_team_name].addLoss(away_team_name,  'H')
						else:
							teams[away_team_name].addWin(home_team_name, 'N')
							teams[home_team_name].addLoss(away_team_name, 'N')


# iterates through each team and calculates the WP (winning percentage) for each
def calcWP():
	for team_name in teams:
		teams[team_name].calcWP()

# iterates through each team and calculates the OWP (opponent's winning percentage) for each
def calcOWP():
	for team_name in teams:
		teams[team_name].calcOWP(teams)

# iterates through each team and calculates the OOWP (opponent's opponent's winning percentage) for each
def calcOOWP():
	for team_name in teams:
		teams[team_name].calcOOWP(teams)	

# iterates through each team and calculates the RPI for each
def calcRPI():
	calcWP()
	calcOWP()
	calcOOWP()
	for team_name in teams:
		teams[team_name].calcRPI()	

# iterates through teams and writes the team and their RPI to file
# sorted alphabetically by team name
# each row contains "tean_name, RPI"
def writeRPIFile():
	# sorted_teams = sorted(teams.items(), key=operator.itemgetter(1))
	with open('rpi.csv', 'w') as f:
		for team in sorted(teams.values(), key=operator.attrgetter('RPI'), reverse=True):
			s = '%s,%f,%f,%f,%f\n' % (team.name, team.WP, team.OWP, team.OOWP, team.RPI)
			f.write(s)


# used for debugging only
def printTeam(team_name):
	if team_name in teams:
		teams[team_name].printTeam()
	else:
		print "Cannot print " + team_name + " because it does not exist"

# used for debugging only
def printTeams():
	for team_name in teams:
		print printTeam(team_name)


if __name__ == "__main__":

	filepath = 'data/ncaamb_gamerts.csv'
	initializeTeams(filepath)
	calcRPI()
	writeRPIFile()




