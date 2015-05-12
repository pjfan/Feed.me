<h1> Feed.me </h1>

A simple Python application created for the purpose of practicing using API's and Git/Github. (No seriously there are 4 different API's being used here...) Uses the NPR The Story API to GET info about NPR stories in the form of Json. Uses the Alchemy Natural Language Processing API to parse location data out of the NPR story text. Uses the OpenStreetMaps nominatim API (hosted on MapQuest's servers) to get geo data (latitude/longitude) from the Alchemy location data. Uses the SendGrid API to send users an e-mail containing the top stories from an NPR category of their choosing.
<br>
<br>
<b>Instructions:</b> 

1. Pip install requirements.txt 
2. Open 'mailsender.py' (it's a script) and change the sender, recipient, and categoryID variables to whatever you want. Some sample categoryID's are listed in the comments. A full list can be found at: http://www.npr.org/api/mappingCodes.php
3. Open up 'grab_story.py' if you want to change the parameters for the NPR Story API. The geo\_data variable is set to false because I haven't implemented a mapping function for the geo data quite yet. The defaults are:

 "def \_\_init\_\_(self, id, numResults=5, npr_story_date=None, startDate=None, endDate=None, include_geo_data=False)"

4. run mailsender.py and the recipient should receive an e-mail with the 5 (or whatever number numResults is set to) most recent stories from the categoryID. 

<b>Possible Future updates:</b><br>
-Making a nicer HTML e-mail format.<br>
-Incorporating more news sources.<br>
-Finding creative uses for the geo data. (Including a map of news stories embedded in the e-mail. Possibly using Leaflet.js or Google Maps.)

<b>Other Resources:</b>
<br>
Query Generator: http://www.npr.org/api/queryGenerator.php


