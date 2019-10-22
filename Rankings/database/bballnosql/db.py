import pymongo

CONN_STR = "mongodb+srv://admin:Gunnison30@cluster0-v4srx.mongodb.net/bballdb?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority"

class BballDbNoSql:

	def __init__(self):
		# connect to MongoDB
		client = pymongo.MongoClient(CONN_STR)
		self.db = client.bballdb