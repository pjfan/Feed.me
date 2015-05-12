A simple Python application created for the purpose of practicing using API's and Git/Github. (No seriously there are 4 different API's being used here...) Uses the NPR The Story API to GET info about NPR stories in the form of Json. Uses the Alchemy Natural Language Processing API to parse location data out of the NPR story text. Uses the Open Street Maps API to get geo data from the Alchemy location data. Uses the SendGrid API to send users an e-mail containing the top stories from an NPR category of their choosing.

Instructions: 

1. Pip install requirements.txt 
2. Open 'mailsender.py' (it's a script) and change the sender, recipient, and categoryID variables to whatever you want. Some sample categoryID's are listed in the comments. A full list can be found at: http://www.npr.org/api/mappingCodes.php
3. Open up 'grab_story.py' if you want to change the parameters for the NPR Story API. The defaults are:

 "def __init__(self, id, numResults=5, npr_story_date=None, startDate=None, endDate=None, include_geo_data=False)"

geo_data is set to false because I haven't implemented a mapping function for the geo data quite yet. 

4. run mailsender.py and the recipient should receive an e-mail with the 5 (or whatever number numResults is set to) most recent stories from the categoryID. 

Possible Future updates:
-Making a nicer HTML e-mail format.
-Incorporating more news sources.
-Finding creative uses for the geo data. (Including a map of news stories embedded in the e-mail.)

Other Resources:
Query Generator: http://www.npr.org/api/queryGenerator.php


