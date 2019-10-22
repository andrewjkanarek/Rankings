

insert_raw_game_query = """INSERT INTO GamesRaw
		(GameId,
		HomeTeamName,
		HomeTeamScore,
		AwayTeamName,
		AwayTeamScore,
		Location,
		MonthDay,
		Year,
		DateCreated,
		Errors)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
