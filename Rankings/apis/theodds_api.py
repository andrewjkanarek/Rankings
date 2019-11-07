import json
import requests

class TheOddsApi:

	def __init__(self):
		self.key = "2b6c4ce43498af94d0d6145c964a91b4"
		self.base_url = 'https://api.the-odds-api.com/v3/sports'
		self.remaining_requests = None

	def get_sports(self):
		# First get a list of in-season sports
		sports_response = requests.get(self.base_url, params={
		    'api_key': self.key
		})

		sports_json = json.loads(sports_response.text)

		if not sports_json['success']:
		    print(
		        'There was a problem with the sports request:',
		        sports_json['msg']
		    )

		else:
		    print()
		    print(
		        'Successfully got {} sports'.format(len(sports_json['data'])),
		        'Here\'s the first sport:'
		    )
		    print(sports_json['data'][0])
		    self.remaining_requests = sports_response.headers['x-requests-remaining']

		return sports_json