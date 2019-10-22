import pymysql
from pymysql import Error

from database.bballsql.db import BballDb


class BballApi:

	def __init__(self):
		self.db = BballDb()

	# def __del__(self):
	# 	self.db.disconnect()

	def insert_raw_games(self, raw_games):

		try:
			for game in raw_games:
				placeholders = ', '.join(['%s'] * len(game))
				columns = ', '.join(game.keys())
				query = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('GamesRaw', columns, placeholders)
				self.db.insert_row(query, game.values())

			sefl.db.commit()

		except Error as e:
			print('Error:', e)


	# given the team name, return row from DB if it exists
	def get_team(self, team_name):
		try:
			query = 'SELECT * FROM bball.Teams WHERE name = "{team_name}" LIMIT 1'.format(team_name=team_name)
			team = self.db.execute(query)

			return team

		except Error as e:
			print('Error:', e)

	# insert the Team if it doesn't exist
	def insert_team(self, team_name):
		try:
			team = self.get_team(team_name)
			if team is not None:
				return team['Id']

			query = "INSERT INTO Teams ( Name ) VALUES ( '{name}' )".format(name=team_name)
			self.db.execute(query)
			teamid = self.db.cursor.lastrowid
			self.db.commit()

			return teamid

		except Error as e:
			print('Error:', e)

