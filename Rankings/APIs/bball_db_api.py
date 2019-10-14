from mysql.connector import Error

from Database.BballSql.bball_db_queries import *



def insert_raw_games(db, raw_games):

	try:

		for game in raw_games:
			placeholders = ', '.join(['%s'] * len(game))
			columns = ', '.join(game.keys())
			sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('GamesRaw', columns, placeholders)
			db.insert(sql, game.values())

		db.commit()

	except Error as e:
		print('Error:', e)


def get_new_raw_games(db):
	return
