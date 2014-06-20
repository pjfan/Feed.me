import os
import requests
import json


ALCHEMY_API_KEY = os.environ.get('ALCHEMY_API_KEY', 'INPUT_ALCHEMY_API_KEY_HERE')


class AlchemyAPIData(object):
	def __init__(self,url,apiKey=ALCHEMY_API_KEY):
		self.url = 'http://access.alchemyapi.com/calls/url/URLGetRankedNamedEntities?apikey='+apiKey+'&url='+url+'&outputMode=json' 
		self.json = None
	def get_json(self):
		"""Makes a GET request to Alchemy API server and asks for JSON as reply."""
		request = requests.get(self.url)
		self.json = request.json()
		return self.json
	def json_to_text(self):
		self.get_json()
		with open ('Alchemy.json','w') as alchemy_json:
			json.dump(self.json, alchemy_json, sort_keys=True, indent=4)
	def parse_for_location(self):
		self.get_json()
		highest_relevance = 0
		geo_data = ""
		for entity in self.json['entities']:
			if (entity['type'] == 'Country' or entity['type'] == 'City') and entity['relevance'] > highest_relevance:
				highest_relevance = entity['relevance']
				geo_data = entity['text']
		return geo_data




