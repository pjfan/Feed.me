
import npr_story as npr
import json
import datetime
import alchemy_api as alch

date_stamp = datetime.date.today().strftime('%y-%m-%d')

#Other ID's: 1007(science), 1002(home page stories), 1090(story of the day)
#Regional ID's: Africa-1126,Asia-1125,Latin America-1127,Europe-1124, 

class MapDataGenerator(object):
    def __init__(self, id, date=date_stamp, startDate=None, endDate=None):
        self.id = id
        self.date = date
        self.npr_story = npr.nprStoryData(id=self.id, numResults=10, date=date, startDate=startDate, endDate=endDate)
        self.npr_json = self.npr_story.get_json()
        self.json_list = None
        #self.npr_story.json_to_text()
    def parse_npr_json(self):
        if "message" in self.npr_json.keys():
            return self.no_stories_json()
        json_list = []
        for story in self.npr_json['list']['story']:
            location_tuple = alch.AlchemyAPIData(story['link'][0]['$text']).parse_for_location()
            location = location_tuple[0]
            geo_data = location_tuple[1]
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
        self.json_list = json_list
        return json_list
    def no_stories_json(self):
        return {"message":"No stories yet for this date/topic."}
    def parse_json_to_file(self, name):
        if self.json_list == None:
            self.parse_npr_json()
        with open(self.date + '_' + str(name) + '.json', 'w') as json_txt:
            json.dump(self.json_list, json_txt, indent=4, sort_keys=True)

MapDataGenerator('1002').parse_json_to_file('Top_Stories')


