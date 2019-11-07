BACKGROUND

Ranking teams in college basketball is a very challenging task, since there are 351 Division I basketball teams with a wide range of skills. A team with a record of 29-1 may still be worse than a team with a record of 20-10, if the second team has a harder schedule.

My solution is to use Google's PageRank algorithm to help rank the teams, then use this to make predictions for future basketball games. This algorith will then be modified with other important factors like home field advantage and margins of vistory for each game to make the best model for ranking the teams.

TO COME

 - Use data models to determine what are the most important factors in determining a team's "value" (how good they are), and apply them to the ranking model.
 - Use API to upload game data real time.


LIMITS

1) Difficult to predict games early in the season, since there is no training data, and games from the previous year are not a good measure since teams change so much between years.
2) It does not currently account for player contributions, so if a team's best player is missing from a game, it is not factored into the outcome prediction.

FILES (require DB access)

csv_etl.py - upload game data from csv file, transform data and load into database 
rankings.py - reads game data from database and rank teams
homeadv.py - determines the average win percentage for home and away games during a given season to predict how much home field is (about 62% of home games won)
apis.bball_db_api.py - manages connection and queries to MySQL database
apis.theodds_api.py - manages api calls to TheOdds API.


MYSQL Info (AWS)

https://us-west-2.console.aws.amazon.com/rds/home?region=us-west-2#database:id=bball-db;is-cluster=false
	'host': 'bball-db.cw0hxqyittzg.us-west-2.rds.amazonaws.com'
	'port': 3306
	'database': 'bball'
	'user': 'admin'
	'password': 'Gunnison30'

MongoDB (Atlas)

https://cloud.mongodb.com/v2/5da4a3bed5ec130628a1f2c9#clusters
connection string: mongodb+srv://admin:Gunnison30@cluster0-v4srx.mongodb.net/bballdb?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority
connect with mongo shell: mongo "mongodb+srv://cluster0-v4srx.mongodb.net/bballdb" --username admin

The Odds API
key: 2b6c4ce43498af94d0d6145c964a91b4


