***** Basic Summary *****

This program takes in a file containing basketball games and outputs a file containing all of the teams and their RPI statistics.

Input File: 
Each row in the file is comma separated and contains a game from a season.
Format of each row: <home_team_name>,<home_team_score>,<away_team_name>,<away_team_score>,<location>
Assumptions:
	1) If the first column is blank, the rest are too.
	2) The names and scores of the teams are required.
	3) Two teams can never tie.
	4) If a location is specified, it is neutral court, otherwise the home team has the advantage.
	5) All of the rows in a single file are part of the same season.
	6) All teams specified are D1.


Output File:
Name: rpi.csv
There is one row for every team that plays a game in the season, and each row contains RPI statistics. 
The rows are comma separated.
Format of each row: <team_name>,<WP>,<OWP>,<OOWP>,<RPI>
Rows are sorted with highest RPI's at the top


***** How to Run *****

1) Change 'filepath' variable in main.py to point to file you would like to run.
2) cd into directory to where "main.py" is.
3) Run: python main.py
4) An output file is created.

***** Formulas *****

RPI = (WP * 0.25) * (OWP * 0.50) * (OOWP * 0.25)

WP (win percentage) for Team A = Sum of weighted wins for Team A / Sum of weighted games for Team A
Each game is weighted based on location
Home win - .6 points	Home loss - 1.4 points
Away win - 1.4 points	Away loss - .6 points
Neutral win - 1 point  Neutral loss - 1 point
Ex: If a team wins at home and loses at home their WP = (.6 (home win)) / (.6 (home win) + 1.4 (home loss)) = .3

OWP (opposing WP) for Team A = (sum of (games won / total number of games) for each opponent of Team A, not including the games against Team A) / (number of games played by Team A)
Note: If Team A plays Team B twice, the sum for B is counted twice.

OOWP (opposing OWP) for Team A = sum of each opponent's OWP / number of games played by Team A.
Note: If Team A plays Team B twice, the sum for B is counted twice.


