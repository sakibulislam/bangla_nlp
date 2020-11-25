from re import findall, finditer, IGNORECASE, MULTILINE, search, sub
import bdates, os
from bdates import extract_dates

global dictionary
dictionary = {}

global not_locations
not_locations = set()


def isLocation(text):
    global not_locations

    if not not_locations:
        print "if first time calling, initialize setOfNonLocations"
        with open(os.path.dirname(os.path.abspath(__file__)) + "/data/non-locations.txt") as f:
            not_locations = frozenset(f.read().splitlines())

    return not text in not_locations

def loadDemonymDictionary():
    with open(os.path.dirname(os.path.abspath(__file__)) + "/data/demonyms.txt","r") as f:
        for line in f:
            words = line.strip().split(",")
            country = words[0]
            for word in words[1:]:
                dictionary[word] = country

def getLocationsFromEnglishText(text):
    global dictionary
    if not dictionary:
        loadDemonymDictionary()

    #print "getting locations from ", type(text)
    if isinstance(text, str):
        text = text.decode("utf-8")
    #print "type(text) is", type(text)

    locations = []

    # location after keyword
    # todo: remove in -ish, in Spanish
    locations += findall(ur"(?:(?:cross the|in|entered|into|outside of|from|eastern|western|northern|southern|reached|countries|leaving|to) )([A-Z][a-z]+(?: [A-Z][a-z]+))", text, MULTILINE)

    # keyword after country as name or acronym
    locations += findall(ur"([A-Z][a-z]+|[A-Z]{2,}) (?:city|county|province)", text, MULTILINE)

    # keyword after country as name or acronym
    locations += findall(ur"([A-Z][a-z]+|[A-Z]{2,})'s (?:border|prime minister|southern|western|northern|eastern|defense minister)", text, MULTILINE)

    # Greece-Macedonia border
    locations += findall(ur"([A-Z][a-z]+)-([A-Z][a-z]+) border", text, MULTILINE)

    #countries, especially/like/ Italy, Greece and Hungary.
    locations += findall(ur"(?:countries|nations|places), [a-z]+ ([A-Z][a-z]+), ([A-Z][a-z]+) and ([A-Z][a-z]+)", text, MULTILINE)

    #islands of Kos, Chios, Lesvos and Samos 
    locations += findall(ur"(?:countries|islands|nations|places|states) of ([A-Z][a-z]+), ([A-Z][a-z]+), ([A-Z][a-z]+)+ and ([A-Z][a-z]+)", text, MULTILINE)

    #ignore demonyms for now, because accuracy is not that high
    #Eritreans, Syrian
    for demonym in findall(ur"([A-Z][a-z]{3,}ans?)", text, MULTILINE):
        if demonym in dictionary:
            country = dictionary[demonym]
            locations.append(country)

    locations = list(set(locations))

    locations = [location for location in locations if isLocation(location)]

    return locations

def trim_location(text):
    global dictionary
    if not dictionary:
        loadDemonymDictionary()

#    for term in ("The","Area","Islamic","Republic","of","Principality","Territory","Kingdom","Plurinational","State","Arab","Co-operative","Federal","Democratic","People's","Bailiwick","Repubblica","Hashemite","Union","Federation","Special Administrative","Region","United","Sultanate","Independent")
    result = sub("[^,]* (of|di) (the)?","",text, flags=IGNORECASE).strip()
    result = sub(ur"\(.*\)","", text, flags=IGNORECASE).strip()
    result = sub(" Area$", "", result, flags=IGNORECASE).strip()
    for word in result.split():
        if word in dictionary:
            return dictionary[word]
    return result
