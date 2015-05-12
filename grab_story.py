
import npr_story_api as npr
import json
import datetime
import alchemy_api as alch

#Some categoryID's: 1007(science), 1002(home page stories), 1090(story of the day), 103537970(shots: Health News) 
#Other Regional ID's: 1126(Africa), 1125(Asia), 1127(Latin America), 1124(Europe) 


class AssembleStory(object):
    def __init__(self, id, numResults=5, npr_story_date=None, startDate=None, endDate=None, include_geo_data=False):
        self.current_date = datetime.date.today().strftime('%y-%m-%d')
        self.include_geo_data = include_geo_data
        self.npr_story= npr.NPRStoryAPIData(id=id, numResults=numResults, date=npr_story_date, startDate=startDate, endDate=endDate)
        self.npr_json = self.npr_story.get_json()
        self.json_list = None
    def parse_npr_json(self):
        #'Message' indicates there's an error message.
        if "message" in self.npr_json.keys():
            return self.no_stories_json()
        json_list = []

        for story in self.npr_json['list']['story']:
            location = None
            geo_data = None
            reporter = "unknown"
            if self.include_geo_data == True:
                location_tuple = alch.AlchemyAPIData(story['link'][0]['$text']).parse_for_location()
                location = location_tuple[0]
                geo_data = location_tuple[1]
            if "byline" in story.keys():
                reporter = story['byline'][0]['name']['$text'],             
            json_story_format = {
                "url": story['link'][0]['$text'],
                "title": story['title']['$text'],
                "description": story['teaser']['$text'],
                "location": location,
                "geo_data": geo_data,
                "reporter": reporter,
                "date": story['storyDate']['$text']
            }
            json_list.append(json_story_format)
        self.json_list = json_list
        return json_list
    def no_stories_json(self):
        return {"message":"No stories yet for this date/topic."}
    def parse_json_to_file(self, name):
        if self.json_list == None:
            self.parse_npr_json()
        with open(self.current_date + '_' + str(name) + '.json', 'w') as json_txt:
            json.dump(self.json_list, json_txt, indent=4, sort_keys=True)



