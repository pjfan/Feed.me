"""For now this script, just prints the headlines to the command line, in the future make a better front-end."""
import npr_story as npr
import json
import time
import datetime
import alchemy_api as alch


#Other ID's: 1007(science), 1002(home page stories), 1090(story of the day)
#Regional ID's: Africa-1126,Asia-1125,Latin America-1127,Europe-1124, 

class RegionalData(object):
	def __init__(self, region_id):
		self.id = region_id
		self.npr_story = npr.nprStoryData(id=self.id, numResults=10, date="2014-06-17")
		self.npr_json = self.npr_story.get_json()
	def parse_npr_json(self):
		json_list = []
		for story in self.npr_json['list']['story']:
			geo_data = alch.AlchemyAPIData(story['link'][0]['$text']).parse_for_location()
			json_map_format = {
				"url": story['link'][0]['$text'],
				"title": story['title']['$text'],
				"description": story['teaser']['$text'],
				"geo_data": geo_data,
				"reporter": story['byline'][0]['name']['$text'],
				"date": story['storyDate']['$text']
			}
			json_list.append(json_map_format)
		return json_list

print RegionalData('1125').parse_npr_json()
print RegionalData('1126').parse_npr_json()
print RegionalData('1127').parse_npr_json()
print RegionalData('1124').parse_npr_json()

