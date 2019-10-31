import pymysql
from pymysql import Error

from database.bballsql.db import BballDb


class BballApi:

	def __init__(self):
		self.db = BballDb()


	def insert_raw_games(self, raw_games):

		try:
			for game in raw_games:
				placeholders = ', '.join(['%s'] * len(game))
				columns = ', '.join(game.keys())
				query = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('GamesRaw', columns, placeholders)
				self.db.insert_row(query, game.values())

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

			return teamid

		except Error as e:
			print('Error:', e)

	def check_game_exists(self, home_team_id, away_team_id, date):
		pass

	def insert_team_game_stats(self, team_id, points_scored):
		pass

	def insert_game(self, season, home_stats_id, away_stats_id, point_spread, is_neutral_flag, date):
		pass

