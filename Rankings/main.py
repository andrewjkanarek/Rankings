import pandas as pd
import datetime as dt

filepath = '/Users/AndrewKanarek/Desktop/Tech/Rankings/Data/Games/ncaamb_gamerts_200.csv'

games = pd.read_csv(filepath, names=['HomeTeam', 'HomeScore', 'AwayTeam', 'AwayScore', 'Location', 'Blank1', 'MonthDay', 'Year'])

# Update team names
games["HomeTeam"] = games["HomeTeam"].str.title()
games["HomeTeam"] = games["HomeTeam"].str.replace("'", "")
games["AwayTeam"] = games["AwayTeam"].str.title()
games["AwayTeam"] = games["AwayTeam"].str.replace("'", "")

# parse date format
games["Date"] = pd.to_datetime(games["MonthDay"].str.cat(games["Year"].astype(str), sep=' '))

