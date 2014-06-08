"""For now this script, just prints the headlines from the past 5 years to the command line, in the future make a better front-end."""

import npr_story_ext as npr
import time
import datetime

month_day = datetime.datetime.fromtimestamp(time.time()).strftime('-%m-%d')

API_KEY='MDE0MzQwNzMxMDE0MDEwNjE1MzNhNjU1Yw001'

#id's to practice with 1007 for science, 1002 for home page stories, 1090 for story of the day

for year in xrange(2010,2015):
	date = str(year) + month_day
	story =	npr.nprStoryData(API_KEY, id=1090, numResults=1, date=date)
	json = story.get_json()
	print json['list']['story'][0]['title']['$text']
