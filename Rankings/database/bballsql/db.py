import pymysql
from pymysql import Error

from .config import bball_db_config

class BballDb:

	def __init__(self):
		self.connect()

	def connect(self):
		self.connection = pymysql.connect(**bball_db_config)

		self.cursor = self.connection.cursor()

		self.test_connection()

	def disconnect(self):
		if self.connection.open:
			self.cursor.close()
			self.connection.close()
			print("MySQL connection is closed")

	def test_connection(self):
		try:

		    if self.connection.open:
		        db_Info = self.connection.get_server_info()
		        print("Connected to MySQL Server version ", db_Info)
		        cursor = self.connection.cursor()
		        cursor.execute("select database();")
		        record = cursor.fetchone()
		        print("You're connected to database: ", record)

		except Error as e:
			print("Error while connecting to MySQL: ", e)


	def execute(self, query):
		self.cursor.execute(query)

	def insert_row(self, query, row):
		self.cursor.execute(query, row) 

	def insert_many(self, query, rows):
		self.cursor.executemany(query, rows)

	def commit(self):
		self.connection.commit()
