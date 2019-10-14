from Extraction.completed_games_extractor import CompletedGamesExtractor
from Database.BballSql.bball_db import BballDb
from APIs.bball_db_api import *

# connect to db

bball_db = BballDb()
bball_db.connect()


# read from file

path = '/Users/AndrewKanarek/Desktop/Tech/Rankings/Data/Games/ncaamb_gamerts_200.csv'

completed_games_extractor = CompletedGamesExtractor(path);
games_raw = completed_games_extractor.extract()


# insert into raw tables

insert_raw_games(bball_db, games_raw)

# read from raw table


bball_db.disconnect()

# validate

# establish database connection

# insert into database