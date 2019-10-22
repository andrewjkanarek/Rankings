import pymongo
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient("mongodb+srv://admin:Gunnison30@cluster0-v4srx.mongodb.net/bballdb?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority")
db=client.bballdb

# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
