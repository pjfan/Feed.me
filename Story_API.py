from urllib2 import urlopen
from json import load

API_KEY='MDE0MzQwNzMxMDE0MDEwNjE1MzNhNjU1Yw001'

#default format for response is json

class StoryURL(object):
	def __init__(API_KEY):
		self.API_KEY = API_KEY
		self.url = 'http://api.npr.org/query?apiKey=' + API_KEY + '&format=json'
		self.has_id = False
		self.has_asset = False
		self.AUDIO = 'audio'
		self.TEXT = 'text'
		self.IMAGES = 'images'
	def add_num_results(num):
		self.url += '&numResults=' + num
	def add_id(id):
		if !self.has_id:
			self.url += '&id=' + id
			self.has_id == True
		else:
			self.url = self.url.replace('&id=', '&id='+ id + ',')
	def add_required_assets(asset):
		#Only pass in one of the enumerated class fields
		if asset != self.AUDIO or asset != self.TEXT or asset != self.IMAGES:
			return 'Incorrect Inputs, please input self.AUDIO, self.TEXT, or self.IMAGES.'
		if self.has_asset:
			self.url = self.url.replace('&requiredAssets=', '&requiredAssets='+ asset + ',')
		else:
			self.url += '&requiredAssets=' + asset 
			self.has_asset = True
	def reset_url():
		self.url = 'http://api.npr.org/query?apiKey=' + API_KEY + '&format=json'
		self.has_id = False
		self.has_asset = False

		