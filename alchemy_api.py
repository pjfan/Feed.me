import os
import requests
import json
import operator


ALCHEMY_API_KEY = os.environ.get('ALCHEMY_API_KEY', 'INPUT_ALCHEMY_API_KEY_HERE')


class AlchemyAPIData(object):
    def __init__(self,url,apiKey=ALCHEMY_API_KEY):
        self.url = 'http://access.alchemyapi.com/calls/url/URLGetRankedNamedEntities?apikey='+apiKey+'&url='+url+'&outputMode=json' 
        self.json = None
    def get_json(self):
        """Makes a GET request to Alchemy API server and asks for JSON as reply."""
        request = requests.get(self.url)
        self.json = request.json()
        return self.json
    def json_to_text(self):
        self.get_json()
        with open ('Alchemy.json','w') as alchemy_json:
            json.dump(self.json, alchemy_json, sort_keys=True, indent=4)
    def parse_for_location(self):
        self.get_json()
        geo_data = (None, None)
        location_list = []
        for entity in self.json['entities']:
            if (entity['type'] == 'Country') or (entity['type'] == 'City'):
                location_list.append({'name': entity['text'],'relevance':entity['relevance'], 'type':entity['type']})
        location_list.sort(key=operator.itemgetter('relevance'), reverse=True)
        city_list = filter_by_key(location_list, 'type', ['City'])
        country_list = filter_by_key(location_list, 'type', ['Country'])
        if country_list != [] and city_list != []:
            for country in country_list:
                for city in city_list:
                    if get_coordinates(country=country['name'] ,city=city['name']) != None:
                        geo_data = (city['name'] + ', ' + country['name'], get_coordinates(country=country['name'] ,city=city['name']))
                        return geo_data
        if geo_data == (None, None):
            for location in location_list:
                if location['type']=='City' and (get_coordinates(city=location['name']) != None):
                    geo_data = (location['name'], get_coordinates(city=location['name']))
                    return geo_data
                if location['type']=='Country' and (get_coordinates(country=location['name'])!=None):
                    geo_data = (location['name'], get_coordinates(country=location['name']))
                    return geo_data
        return geo_data


def get_coordinates(city=None, country=None, zip=None, state=None):
    """Takes location data (city, state, zip, country) as input. Sends a GET request to the open street maps/mapquest API and 
    pulls latitude/longitude information out of the Json that's returned."""
    url = 'http://open.mapquestapi.com/nominatim/v1/search.php'
    parameters = {'city': city, 'country': country, 'postalcode': None, 'state': state, 'format': 'json' }
    request = requests.get(url, params=parameters)
    request_json = request.json()
    if request_json == []:
        return None
    else:
        return {'latitude': request_json[0]['lat'], 'longitude': request_json[0]['lon']}


def filter_by_key(location_list, key, value_list):
    return [location for location in location_list if location[key] in value_list]