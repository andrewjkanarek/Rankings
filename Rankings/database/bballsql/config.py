import pymysql

bball_db_config = {
	'host': 'bball-db.cw0hxqyittzg.us-west-2.rds.amazonaws.com',
	'user': 'admin',
	'password': 'Gunnison30',
	'port': 3306,
	'db': 'bball',
	'charset': 'utf8mb4',
 	'cursorclass': pymysql.cursors.DictCursor
}
