from hose_util import lookup
import re
import logging
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)
from hw1.CarmenProperties import *
from hw1.carmen_utils import Utils
from Location import Location
from hw1.GeocodeLocationResolver import GeocodeLocationResolver
import os

root = os.path.dirname(__file__)
import json
from datetime import datetime
import pattern.en as pen


def task1():
    print "Task 1"
    print "Hello Word"

def task2():
    print "Task 2"
    list=[1,2,3,4,5]
    print list

def task3():
    print "Task 3"
    file= open("task3.data","r")
    items1=[map(int, x) for x in file.read(9).split(" ")]

    items2 = file.read(10).split(" ")
    #items2 = [int(i) for i in items2]
    print items1
    print items2

def task4(data):
    print "Task 4"
    for key,value in data.items():
        print key,value

def task5(data):
  print "Task 5"
  with open('task5.json','w') as fileopen:
      json.dump(data,fileopen)

def task6(data):
    print 'Task 6'
    items=[1,2,3,4,5]

    with open('task6.data','w') as fileopen:
        for item in items:
            json.dump(item,fileopen)
        json.dump(data,fileopen)

    file = open('task6.data','r')
    itemsread=file.read(5)
    print itemsread

    datadict=dict()
    datadict = file.read()
    print datadict

def task7():
    print 'Task 7'

    with open('CrimeReport.txt') as f:
        for line in f:
            tweet = json.loads(line)
            print tweet['id']

def task8():
    print 'Task 8'
    tweets=[]
    sorted_tweets=[]
    with open('CrimeReport.txt') as f:
        for line in f:
            tweet = json.loads(line)
            tweets.append(tweet)
            tweetDate = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')

        sorted_tweets=sorted(tweets,key=lambda item:tweetDate)

    with open('task8.data','w') as file:
        for i in list(sorted_tweets)[0:9]:
            json.dump(i,file)
            print i['created_at']


def task9():
    print 'Task 9'
    tweets=[]
    distint_hour=[]
    with open('CrimeReport.txt') as f:
        for line in f:
            tweet = json.loads(line)
            tweets.append(tweet)
            tweetDate = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
            distint_hour.append(tweetDate.hour)
    distint_hour=set(distint_hour)

    for hour in distint_hour:
        filename="%s%s" %(hour,'.data')
        print filename
        with open('task9-output/'+filename,'w') as fileout:
            for tweet in tweets:
                tweetDate = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                if tweetDate.hour==hour:
                    print hour
                    json.dump(tweet,fileout)

def task10():
    print 'Task 10'
    tweets=[]
    positive_feeds=[]
    negative_feeds=[]
    with open('CrimeReport.txt') as f:
        for line in f:
            tweet = json.loads(line)
            tweets.append(tweet)
            if pen.positive(tweet['text'],threshold=0.0):
                positive_feeds.append(tweet)
            else:
                negative_feeds.append(tweet)
    with open('positive-entiment-tweets.txt','w') as file:
        json.dump(positive_feeds,file)
    with open('negative-sentiment-tweets.txt','w') as file:
        json.dump(negative_feeds,file)

def task11():
    print 'Task 11'
    resolver = LocationResolver.getLocationResolver()
    tweet = {"user": {"follow_request_sent": None, "profile_use_background_image": True, "default_profile_image": False, "id": 450118613, "verified": False, "profile_image_url_https": "https://si0.twimg.com/profile_images/3057746486/e59e5762dae908d6c6827556b5230886_normal.jpeg", "profile_sidebar_fill_color": "FFF7CC", "profile_text_color": "0C3E53", "followers_count": 163, "profile_sidebar_border_color": "F2E195", "id_str": "450118613", "profile_background_color": "BADFCD", "listed_count": 0, "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme12/bg.gif", "utc_offset": -18000, "statuses_count": 2146, "description": "Jesus is my Savior!! I love to live, laugh, learn, and love. Friends are my rock!! Track yo(; 'Hakuna Matata' that's my motta! \ue32c", "friends_count": 386, "location": "Bethel Acers, Oklahoma", "profile_link_color": "FF0000", "profile_image_url": "http://a0.twimg.com/profile_images/3057746486/e59e5762dae908d6c6827556b5230886_normal.jpeg", "following": None, "geo_enabled": True, "profile_banner_url": "https://si0.twimg.com/profile_banners/450118613/1359593437", "profile_background_image_url": "http://a0.twimg.com/images/themes/theme12/bg.gif", "name": "Jazmine Rena\u00e9 ", "lang": "en", "profile_background_tile": False, "favourites_count": 118, "screen_name": "renaejazzz", "notifications": None, "url": None, "created_at": "Thu Dec 29 22:08:38 +0000 2011", "contributors_enabled": False, "time_zone": "Eastern Time (US & Canada)", "protected": False, "default_profile": False, "is_translator": False}, "favorited": False, "entities": {"user_mentions": [{"id": 563928121, "indices": [1, 12], "id_str": "563928121", "screen_name": "PeytonEpp9", "name": "Peyton Too Cold\u2744\u2744"}, {"id": 450118613, "indices": [14, 25], "id_str": "450118613", "screen_name": "renaejazzz", "name": "Jazmine Rena\u00e9 "}], "hashtags": [], "urls": []}, "contributors": None, "truncated": False, "text": "\"@PeytonEpp9: @renaejazzz in track tho&gt;&gt;&gt;&gt;\" I try!! \ud83d\ude0f", "created_at": "Fri Feb 01 00:00:10 +0000 2013", "retweeted": False, "in_reply_to_status_id_str": None, "coordinates": None, "in_reply_to_user_id_str": None, "lang": "nl", "source": "<a href=\"http://twitter.com/devices\" rel=\"nofollow\">txt</a>", "in_reply_to_status_id": None, "in_reply_to_screen_name": None, "id_str": "297132196270067713", "place": None, "retweet_count": 0, "geo": None, "id": 297132196270067713, "in_reply_to_user_id": None}
    print tweet['text']
    tweet['text'] = ' new york '
    location = resolver.resolveLocationFromTweet(tweet)
    print location.getDisplayString()
    pass

class LocationResolver(object):
    resolver = None
    def __init__(self):
        self.stateFullNames = []
        self.countryFullNames = []
        self.stateAbbreviationToFullName = dict()
        self.countryAbbreviationToFullName = dict()
        self.geocodeLocationResolver = None
        self.useUnknownPlaces = True
        self.newLocationIndex = Constants.NEW_LOCATION_STARTING_INDEX
        self.statePattern = ".+,\\s*(\\w+)"
        self.placeNameToNormalizedPlaceName = dict()
        self.idToLocation = dict()
        self.locationNameToLocation = dict()
        self.locationToParent = dict()
        self.locationToChildren = dict()
        self.locationToId = dict()
        self.usePlace = CarmenProperties["use_place"]
        self.useGeocodes = CarmenProperties["use_geocodes"]
        self.useUserString = CarmenProperties["use_user_string"]
        self.useUnknownPlaces = CarmenProperties["use_unknown_places"]
        logger.info("Geocoding using these resources:")
        if self.usePlace:
            logger.info('place')
        if self.useGeocodes:
            logger.info('geocodes')
        if self.useUserString:
            logger.info("user profile")
        logger.info("Loading location resources.")
        self.loadLocationFile(os.path.join(root,CarmenProperties["locations"]))
        knownLocations = []
        for location in self.idToLocation.values():
            knownLocations.append(location)
        self.idToLocation[-1] = Location.getNoneLocation()
        for location in knownLocations:
            parent = self.createParentOfLocation(location)
            if parent and not parent.isNone():
                self.locationToParent[location] = parent
            if not self.locationToChildren.has_key(parent):
                self.locationToChildren[parent] = []
            self.locationToChildren[parent].append(location)
            currentLocation = parent
            parent = self.createParentOfLocation(currentLocation)
            while parent and not parent.isNone():
                if not self.locationToParent.has_key(currentLocation):
                    self.locationToParent[currentLocation] = parent
                if not self.locationToChildren.has_key(parent):
                    self.locationToChildren[parent] = []
                self.locationToChildren[parent].append(currentLocation)
                currentLocation = parent
                parent = self.createParentOfLocation(currentLocation)
        if self.usePlace:
            self.loadNameAndAbbreviation(os.path.join(root,CarmenProperties["place_name_mapping"]), None, self.placeNameToNormalizedPlaceName, False)
        self.loadNameAndAbbreviation(os.path.join(root,CarmenProperties["state_names_file"]), self.stateFullNames, self.stateAbbreviationToFullName, True);
        self.loadNameAndAbbreviation(os.path.join(root,CarmenProperties["country_names_file"]), self.countryFullNames, self.countryAbbreviationToFullName, True);
        if self.useGeocodes:
            self.geocodeLocationResolver = GeocodeLocationResolver()
            for location in self.idToLocation.values():
                if location.latitude and location.longitude:
                    self.geocodeLocationResolver.addLocation(location)

#        print self.placeNameToNormalizedPlaceName
#        for location in self.locationNameToLocation.keys():
#            print location

    @staticmethod
    def getLocationResolver():
        if not LocationResolver.resolver:
            LocationResolver.resolver = LocationResolver()
        return LocationResolver.resolver

    def createParentOfLocation(self, location):
        parentLocation = None
        if location.getCity():
            parentLocation = Location(location.getCountry(), location.getState(), location.getCounty(), None, None, None, -1, False)
        elif location.getCountry():
            parentLocation = Location(location.getCountry(), location.getState(), None, None, None, None, -1, False)
        elif location.getState():
            parentLocation = Location(location.getCountry(), None, None, None, None, None, -1, False)
        elif location.getCountry() and location.getCountry().lower() != Constants.DS_LOCATION_NONE.lower():
            parentLocation = Location.getNoneLocation()
        if not parentLocation:
            return None
        if self.locationToId.has_key(parentLocation):
            return self.idToLocation[self.locationToId[parentLocation]]
        self.registerNewLocation(parentLocation)
        return parentLocation

    def getPlaceFromTweet(self, tweet):
        if tweet.has_key('place'):
            return tweet['place']
        else:
            return None

    def getUserFromTweet(tweet):
        if tweet.has_key('user'):
            return tweet['user']
        else:
            return None

    def getLocationFromTweet(tweet):
        user = getUserFromTweet(tweet)
        if user:
            location = lookup(user,'location')
            if location:
                return location
        return None

    def getLatLngFromTweet(tweet):
        return Utils.geo_check_tweet(tweet)

    def loadNameAndAbbreviation(self, filename, fullName, abbreviations, secondColumnKey):
        for line in open(filename).readlines():
            splitString = line.lower().split('\t')
            splitString[0] = splitString[0].strip()
            splitString[1] = splitString[1].strip()
            if fullName != None:
                fullName.append(splitString[0])
            if (abbreviations != None):
                if not secondColumnKey:
                    abbreviations[splitString[0]] = splitString[1]
                else:
                    abbreviations[splitString[1]] = splitString[0]

    def setUseUnknownPlaces(self, useUnknownPlaces):
        self.useUnknownPlaces = useUnknownPlaces

    def resolveLocationFromTweet(self, tweet):
        location = None
        if self.usePlace:
            location = self.resolveLocationUsingPlace(tweet)
            if location:
                location.setResolutionMethod(ResolutionMethod.PLACE)
                if not self.useUnknownPlaces and not location.isKnownLocation():
                    location = None
                elif self.useUnknownPlaces and not location.isKnownLocation():
                    self.registerNewLocation(location)
        if not location and self.useGeocodes:
            location = self.resolveLocationUsingGeocodes(tweet)
            if location:
                location.setResolutionMethod(ResolutionMethod.COORDINATES)
        if not location and self.useUserString:
            location = self.resolveLocationUsingUserLocation(tweet)
            if location:
                location.setResolutionMethod(ResolutionMethod.USER_LOCATION)
        return location

    def isUseUnknownPlaces(self):
        return self.useUnknownPlaces

    def resolveLocationUsingPlace(self, tweet):
        place = self.getPlaceFromTweet(tweet)
        if place == None:
            return None

        url = lookup(place, 'url')
        id = lookup(place, 'id')
        country = lookup(place, 'country')
        if country == None:
            logger.warn("Found place with no country: {}".format(place))
            return None
        if self.placeNameToNormalizedPlaceName.has_key(country.lower):
            country = placeNameToNormalizedPlaceName[country.lower]

        placeType = lookup(place, 'place_type')
        if placeType.lower() == 'city':
            city = lookup(place, 'name')
            if country.lower() == 'united states':
                fullName = lookup(place, 'full_name')
                state = None
                if not fullName:
                    logger.warn("Found place with no full_name: {}".format(place))
                    return None
                match = re.search(self.statePattern, fullName)
                if match:
                    matchedString = match.group().lower().split()[1].strip()
                    if self.stateAbbreviationToFullName.has_key(matchedString):
                        state = self.stateAbbreviationToFullName[matchedString]
                    else:
                        st_matches = [st for st in self.stateAbbreviationToFullName.values() if st == matchedString]
                        if len(st_matches) > 0:
                            state = st_matches[0]
                return self.getLocationForPlace(country, state, None, city, url, id)
            else:
                return self.getLocationForPlace(country, None, None, city, url, id)
        elif placeType.lower() == 'admin':
            state = lookup(place, 'name')
            return self.getLocationForPlace(country, state, None, None, url, id)
        elif placeType.lower() == 'country':
            return self.getLocationForPlace(country, None, None, None, url, id)
        elif placeType.lower() == 'neighborhood' or placeType.lower() == 'poi':
            fullName = lookup(place, 'full_name')
            if not fullName:
                logger.warn("Found place with no full_name: {}".format(place))
                return None
            splitFullName = fullName.split(',')
            city = None
            if len(splitFullName) > 1:
                city = splitFullName[1]
            return self.getLocationForPlace(country, None, None, city, url, id)
        else:
            logger.warn("Unknown place type: {}".format(placeType))

    def resolveLocationUsingGeocodes(self, tweet):
        return self.geocodeLocationResolver.resolveLocation(tweet)

    def extract_state(self, matchedString):
        state = None
        if self.stateAbbreviationToFullName.has_key(matchedString):
            state = self.stateAbbreviationToFullName[matchedString]
        else:
            st_matches = [st for st in self.stateAbbreviationToFullName.values() if st == matchedString]
            if len(st_matches) > 0:
                state = st_matches[0]
        return state

    def extract_country(self, matchedString):
        co = None
        if self.countryAbbreviationToFullName.has_key(matchedString):
            co = self.countryAbbreviationToFullName[matchedString]
        else:
            co_matches = [co for co in self.countryAbbreviationToFullName.values() if co == matchedString]
            if len(co_matches) > 0:
                co = co_matches[0]
        return co

    def resolveLocationUsingUserLocation(self, tweet):
        tweetLocation = Utils.getLocationFromTweet(tweet)
        if tweetLocation:
            var = re.sub("\\p{Punct}", " ", tweetLocation)
            location = re.sub("\\s+", " ", var).lower().strip()
            if self.locationNameToLocation.has_key(location):
                return self.locationNameToLocation[location]
            var = re.sub("[!\\\"#$%&'\\(\\)\\*\\+-\\./:;<=>\\?@\\[\\\\]^_`\\{\\|\\}~]", " ", tweetLocation)
            locationWithComma = re.sub("\\s+", " ", var).lower().strip()
            match = re.search(".+,\\s*(\\w+)", locationWithComma)
            if match:
                matchedString = match.group().lower()
                if self.locationNameToLocation.has_key(matchedString):
                    return self.locationNameToLocation[matchedString]
                else:
                    items = matchedString.split(',')
                    if len(items) == 2:
                        state = self.extract_state(items[1].strip())
                        if state:
                            return Location('united states', state, matchedString.split(',')[0], None, None, None, -1, False)
                        else:
                            co = self.extract_country(items[1].strip())
                            return Location(co, None, None, None, None, None, -1, False)
                    else:
                        co = self.extract_country(items[2].strip())
                        if co:
                            state = self.extract_state(items[1].strip())
                            if state:
                                return Location(co, state, items[0].strip(), None, None, None, -1, False)
                            else:
                                return Location(co, None, None, None, None, None, -1, False)
                        else:
                            state = self.extract_state(items[2].strip())
                            if state:
                                return Location('united states', state, None, None, None, None, -1, False)
        return None

    def getLocationForId(self, id):
        if self.idToLocation.has_key(id):
            return self.idToLocation[id]

    def loadLocationToIdFile(self, filename):
        map = dict()
        for line in open(filename).readlines():
            line = line.lower()
            splitString = line.split('\t')
            locationId = int(splitString[0].trim())
            for ii in range(len(splitString)):
                entry = splitString[ii].strip()
                if map.has_key(entry) and not map[entry] == locationId:
                    logger.warn('Duplicate location found: {}'.format(entry))
                map[entry] = locationId
        return map

    def loadLocationFile(self, filename):
        for line in open(filename).readlines():
            locationObj = json.loads(line)
            location = Location.parseLocationFromJsonObj(locationObj)
            aliases = locationObj['aliases']
            self.idToLocation[location.getId()] = location
            self.locationToId[location] = location.getId()
            justAddedAliases = []
            for alias in aliases:
                if alias in justAddedAliases:
                    continue
                if self.locationNameToLocation.has_key(alias):
                    logger.warn("Duplicate location name: {}".format(alias))
                else:
                    self.locationNameToLocation[alias] = location
                justAddedAliases.append(alias)
                var = re.sub("\\p{Punct}", " ", alias)
                newEntry = re.sub("\\s+", " ", var)
                if newEntry in justAddedAliases:
                    continue
                if newEntry != alias:
                    if self.locationNameToLocation.has_key(newEntry):
                        logger.warn("Duplicate location name: {}".format(newEntry))
                    else:
                        self.locationNameToLocation[newEntry] = location
                justAddedAliases.append(newEntry)

    def getLocationForPlace(self, country, state, county, city, url, id):
        location = Location(country, state, county, city, 0, 0, -1, False)
        if self.locationToId.has_key(location):
            return self.idToLocation[self.locationToId[location]]
        location.setUrl(url)
        location.setTwitterId(id)
        return location

    def registerNewLocation(self, location):
        index = self.newLocationIndex
        self.newLocationIndex += 1
        location.setId(index)
        self.locationToId[location] = index
        self.idToLocation[index] = location
        parent = self.createParentOfLocation(location)
        if parent:
            self.locationToParent[location] = parent
            if not self.locationToChildren.has_key(parent):
                self.locationToChildren[parent] = []
            self.locationToChildren[parent].append(location)

    def getParent(self, location):
        if self.locationToParent.has_key(location):
            return self.locationToParent[location]
        return None

    def getChildren(self, location):
        if self.locationToChildren.has_key(location):
            return self.locationToChildren[location]
        return None

    def lookupLocation(self, location):
        if self.locationToId.has_key(location):
            return self.idToLocation[self.locationToId[location]]
        self.registerNewLocation(location)
        return location


if __name__=='__main__':
    data = dict()
    data={'school':'UAlbany','address':'1400 Washington Ave, Albany, NY 12222', 'phone':'(518)4423300'}
    task1()
    task2()
    task3()
    task4(data)
    task5(data)
    task6(data)
    task7()
    task8()
    task9()
    task10()
    task11()
