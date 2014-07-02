<h1> Public Radio App <h1>


A simple Python application created for the purpose of practicing using API's and Git/Github. Uses the NPR The Story API to GET info about NPR stories in the form of Json. Uses the Alchemy Natural Language Processing API to parse location data out of the NPR story text.

Instructions: open up grab_story.py and look for the command at bottom:

MapDataGenerator('1002').parse_json_to_file('Top_Stories')

Feel free to change the number 1002 to the any topic ID that the NPR API will recognize.
Be sure to also change 'Top_Stories' to a different title if you change the ID (which is currently set to home page top stories).
Also feel free to change the date or add a start and end date to get stories within a certain date range. 

Then run grab_story.py (by typing python grab_story.py at the command line.)

Open up the map and the story data should be plotted on the map. There's a rate limit to how much you can send requests to the MapQuest API for geo-coding and the Alchemy API for language processing. The Alchemy and NPR API's both require API keys which can be obtained by making an
account on their respective web-sites.


Good resources for developing this app further:

Developer resources (adding additional criteria to API call): http://dev.npr.org/

Query Generator: http://www.npr.org/api/queryGenerator.php

Mapping index (Map's topics to ID's): http://www.npr.org/api/mappingCodes.php

Current NPR widgets: http://www.npr.org/api/widgets.php
