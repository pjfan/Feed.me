import requests
import json
import time
import datetime



#default format for response is json

date_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%y-%m-%d')

class nprStoryData(object):
	def __init__(self,API_KEY, id=None, numResults=None, requiredAssets=None, date=date_stamp):
		self.API_KEY = API_KEY
		self.url = 'http://api.npr.org/query?apiKey=' + API_KEY + '&format=json'
		self.parameters = {'id': id,'numResults': numResults, 'requiredAssets': requiredAssets, 'date': date}
		self.has_id = False
		self.has_asset = False
		self.json = None
		self.AUDIO = 'audio'
		self.TEXT = 'text'
		self.IMAGES = 'images'
	def add_num_results(self,num):
		"""Adds numbered of results that should be returned to the URL. If there's already a value for numResults
			it will be replaced by the new value."""
		self.parameters['numResults'] = str(num)
	def add_date(self, date):
		"""Adds a date to the URL. If there's already a value for date, it will be replaced by the new value."""
		if date != str or date[4] != '-' or date[7] != '-':
			print "Please input date in the following string format YYYY-MM-DD"
		else:
			self.parameters['date'] = date
	def add_id(self,id):
		"""Adds an ID parameter to the URL. (Indicates what category/program to return stories from.), can add multiple ID's."""
		if self.has_id:
			self.parameters['id'] += ',' + str(id)
		else:
			self.parameters['id'] = str(id)
			self.has_id = True
	def add_assets(self,asset):
		"""Adds a required asset parameter to the URL, can add multiple required assets."""
		if asset != self.AUDIO and asset != self.TEXT and asset != self.IMAGES:
			print 'Incorrect Inputs, please only input "audio", "text", or "images" into this function.'
		elif self.has_asset:
			self.parameters['requiredAssets'] +=  ',' + asset
		else:
			self.parameters['requiredAssets'] = asset
			self.has_asset = True
	def reset_url(self):
		"""Changes the URL back to the base API url + API_KEY and changes has_id and has_asset to false."""
		self.url = 'http://api.npr.org/query?apiKey=' + API_KEY + '&format=json'
		self.has_id = False
		self.has_asset = False
		self.parameters = {'id': None,'numResults': None, 'requiredAssets': None }
	def get_json(self):
		"""Makes a get request to npr API server and asks for JSON as reply."""
		request = requests.get(self.url, params=self.parameters)
		self.json = request.json()
		return self.json
	def json_to_text(self):
		self.get_json()
		with open (str(self.parameters['id']) + '_' + self.parameters['date'] + '_' + 'nprStory.json','w') as npr_json:
			json.dump(self.json, npr_json, sort_keys=True, indent=4)

