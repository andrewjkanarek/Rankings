import mysql.connector
from mysql.connector import Error

from bball_db_config import bball_db_config

class BballDb:

	def __init__(self):
		return

	def __del__(self):
		self.disconnect()

	def connect(self):
		self.connection = mysql.connector.connect(**bball_db_config)

		self.cursor = self.connection.cursor()

		self.test_connection()

	def disconnect(self):
		if (self.connection.is_connected()):
			self.cursor.close()
			self.connection.close()
			print("MySQL connection is closed")

	def test_connection(self):
		try:

		    if self.connection.is_connected():
		        db_Info = self.connection.get_server_info()
		        print("Connected to MySQL Server version ", db_Info)
		        cursor = self.connection.cursor()
		        cursor.execute("select database();")
		        record = cursor.fetchone()
		        print("Your connected to database: ", record)

		except Error as e:
		    print("Error while connecting to MySQL", e)


	def insert(self, query, row):
		self.cursor.execute(query, row) 

	def insert_many(self, query, rows):
		self.cursor.executemany(query, rows)

	def commit(self):
		self.connection.commit()
