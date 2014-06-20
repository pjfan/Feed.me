"""For now this script, just prints the headlines to the command line, in the future make a better front-end."""
import npr_story as npr
import json
import time
import datetime
import alchemy_api as alch


#Other ID's: 1007(science), 1002(home page stories), 1090(story of the day)
#Regional ID's: Africa-1126,Asia-1125,Latin America-1127,Europe-1124, 

class MapDataGenerator(object):
	def __init__(self, id, date="2014-06-17", startDate=None, endDate=None):
		self.id = id
		self.npr_story = npr.nprStoryData(id=self.id, numResults=10, date=date, startDate=startDate, endDate=endDate)
		self.npr_json = self.npr_story.get_json()
		#self.npr_story.json_to_text()
	def parse_npr_json(self):
		if "message" in self.npr_json.keys():
			return self.no_stories_json()
		json_list = []
		for story in self.npr_json['list']['story']:
			location = alch.AlchemyAPIData(story['link'][0]['$text']).parse_for_location()
			geo_data = None
			reporter = "unknown"
			if "byline" in story.keys():
				reporter = story['byline'][0]['name']['$text'],				
			json_map_format = {
				"url": story['link'][0]['$text'],
				"title": story['title']['$text'],
				"description": story['teaser']['$text'],
				"location": location,
				"geo_data": geo_data,
				"reporter": reporter,
				"date": story['storyDate']['$text']
			}
			json_list.append(json_map_format)
		return json_list
	def no_stories_json(self):
		return {"message":"No stories yet for this date/topic."}



print MapDataGenerator('1125').parse_npr_json()
#print MapDataGenerator('1126').parse_npr_json()
#print MapDataGenerator('1127').parse_npr_json()
#print MapDataGenerator('1124').parse_npr_json()

