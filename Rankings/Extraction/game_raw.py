from datetime import datetime

class GameRaw:

	def __init__(self, cols):

		NUM_COLS = 8

	  	if (len(cols) != NUM_COLS):
	  		return
	  
	  	self.row_data = {
	  		'GameId': None,
	  		'HomeTeamName': cols[0],
	  		'HomeTeamScore': cols[1],
	  		'AwayTeamName': cols[2],
	  		'AwayTeamScore': cols[3],
	  		'Location': cols[4],
	  		'MonthDay': cols[6],
	  		'Year': cols[7],
	  		'DateCreated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	  		'Errors': None
	  	}

	def validate(self):
		error_list = []

		if (any(error_list)):
			self['Errors'] = error_list.concat('\n')

		return


