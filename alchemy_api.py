import os
import requests
import json
import operator


ALCHEMY_API_KEY = os.environ.get('ALCHEMY_API_KEY', 'INPUT_ALCHEMY_API_KEY_HERE')


class AlchemyAPIData(object):
    """This class passes data to and receives data from the Alchemy API. It parses the returned data for geo_data."""
    def __init__(self,url,apiKey=ALCHEMY_API_KEY):
        self.url = 'http://access.alchemyapi.com/calls/url/URLGetRankedNamedEntities?apikey='+apiKey+'&url='+url+'&outputMode=json' 
        self.json = None
    def get_json(self):
        """Makes a GET request to Alchemy API server and asks for JSON as reply."""
        request = requests.get(self.url)
        self.json = request.json()
        return self.json
    def save_json_to_file(self):
        self.get_json()
        with open ('Alchemy.json','w') as alchemy_json:
            json.dump(self.json, alchemy_json, sort_keys=True, indent=4)
    def parse_for_location(self):
        self.get_json()
        geo_data = (None, None)
        location_list = []
        #This for loop iterates through all the entities found in the text and picks out the countries and cities.
        #All Countries and Cities are added to the list as dictionaries.
        for entity in self.json['entities']:
            if (entity['type'] == 'Country') or (entity['type'] == 'City'):
                location_list.append({'name': entity['text'],'relevance':entity['relevance'], 'type':entity['type']})
        #The dictionaries in the list are then sorted by relevance in reverse order. (Most relevant first)
        location_list.sort(key=operator.itemgetter('relevance'), reverse=True)
        
        #Two separate lists are made, one for entities recorded as "cities", one for entities recorded as countries.
        city_list = filter_by_key(location_list, 'type', ['City'])
        country_list = filter_by_key(location_list, 'type', ['Country'])
        
        #The scenario for if both a city and country were found as entities in the text.
        #The return statements are necessary so that the most relevant result is returned immediately and the loop ends.
        if country_list != [] and city_list != []:
            for country in country_list:
                for city in city_list:
                    #This if statement is necessary because sometimes the most relevant city and country don't match up.
                    if get_coordinates(country=country['name'] ,city=city['name']) != None:
                        geo_data = (city['name'] + ', ' + country['name'], get_coordinates(country=country['name'] ,city=city['name']))
                        return geo_data
        #If there aren't both cities and countries found in the text then:               
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

