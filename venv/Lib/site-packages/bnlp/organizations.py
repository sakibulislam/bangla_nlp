# -*- coding: utf-8 -*-
import os
from os.path import abspath, dirname, isfile
from re import findall, IGNORECASE, MULTILINE, sub, UNICODE
from re import compile as re_compile
from titlecase import titlecase


global stopwords
stopwords = None

global org_regex
org_regex = None

global orgRegex
orgRegex = None

global soup_regex
soup_regex = None

global keywords
keywords = None

global keywords_arabic
keywords_arabic = None

filepath = dirname(abspath(__file__))

def loadOrgKeywordsIfNecessary():
    global keywords
    if not keywords:
        with open(filepath + "/data/keywords/orgs.txt") as f:
            keywords = [k for k in f.read().decode('utf-8').split('\n') if k]
            keywords = sorted(keywords, key=lambda x: -1*len(x))
            #print "keywords are", keywords

def loadOrgKeywordsArabicIfNecessary():
    global keywords_arabic
    if not keywords_arabic:
        with open(filepath + "/data/keywords/orgs_arabic.txt") as f:
            keywords_arabic = [k for k in f.read().decode('utf-8').split('\n') if k]
            keywords_arabic = sorted(keywords_arabic, key=lambda x: -1*len(x))
            #print "keywords_arabic are", keywords_arabic



# returns a version of the name with org keywords removed
# e.g., University of Alabama will return Alabama
def trimOrgName(name, min_words=0):
    global keywords
    loadOrgKeywordsIfNecessary()
    loadOrgKeywordsArabicIfNecessary()

    for keyword in keywords + keywords_arabic:
        if name.count(" ") + 1 > min_words:
            name = name.replace(keyword,"").replace("  "," ").strip()
        else:
            return name
    if name.count(" ") + 1 > min_words:
        name = sub(r"( wal-|al-|')$", "", name, IGNORECASE)
        name = sub(r"^(of|the) ", "", name, IGNORECASE)
        name = sub(r"^(of|the) ", "", name, IGNORECASE)
        name = name.replace("  "," ").strip()
    return name

def trim_org_name(name, min_word_count=None):
    global keywords
    global keywords_arabic
    loadOrgKeywordsIfNecessary()
    loadOrgKeywordsArabicIfNecessary()
    keywords_all = keywords + keywords_arabic

    words = name.split()
    length = len(words)
    while len(words) >= min_word_count:
        if words[0] in keywords_all:
            words = words[1:]
        if len(words) >= min_word_count and words[-1] in keywords_all:
            words = words[:-1]
    return " ".join(words)
 
def createOrgRegexIfNecessary():
    global keywords
    loadOrgKeywordsIfNecessary()

    global org_regex
    if not org_regex:

        keyword_pattern = u"(?:" + u"|".join(keywords) + ")"

        titled_pattern = u"(?:\d*(?:st|nd|th)[ ])?(?:al-|ash-|ath-)?[A-Z][a-z(a'|'a)]{2,}(?:(?: |-i-)(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?[A-Z][a-z('a|a')]{2,})*"
        org_regex = re_compile(u"((?:"+titled_pattern+" )*" + keyword_pattern + "(?: "+titled_pattern+")*)")

def xGetOrgsFromText(text):
    global keywords
    loadOrgKeywordsIfNecessary()

    global orgRegex
    if not orgRegex:
        citation = u"(?: ?\[\d{1,3}\] ?)*"
        keyword = u"(?:" + u"|".join(keywords) + ")"
        seperator = u"(?:, |,|\u200E|\u200E | \u200E| \u200E | or |;|; ){1,3}"

        # accept a as uppercase because sometimes used in acronymns such as Jash al-... Ja...
        u = u"[^\W\d_b-z:]"
        l = u"(?:[^\W\d_A-Z:]|')"
        acronym = u+'{2,}'
        titled = u"(?:\d+(?:st|nd|th)[ ])?(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?" + u + l + "{2,}(?:(?: |-i-)(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?"+u+l+"{2,})*"
        alias = u"(?:(?:"+u+l+"{3,}: ?|meaning\")?" + "("+titled+")" + "|" + '('+acronym+')' +  ")"
        name = u"((?:"+titled+" )*" + keyword + "(?: "+titled+")*)" + citation
        aliases = "(?: ?\(" + alias + "(?: ?" + seperator + alias + ")*" + ")*"
        org = name + "(?: or " + name + ")?" + aliases
        #orgRegex = re_compile(org, MULTILINE|UNICODE)

    if isinstance(text, str):
        text = text.decode("utf-8")

#    return findall(orgRegex, text)
    return findall(org, text, UNICODE)
xg = xGetOrgsFromText
    
def createSoupRegexIfNecessary():
    global keywords
    loadOrgKeywordsIfNecessary()

    global soup_regex
    if not soup_regex:

        keyword_pattern = u"(?:" + u"|".join(keywords) + ")"

        titled_pattern = u"(?:\d*(?:st|nd|th)[ ])?(?:al|al-|al |ash|ash-|ash |at|at-|at |ath|ath-|ath )?[A-Z][a-z(a'|'a)]{2,}(?:(?: |-i-)(?:al|al-|al |ash|ash-|ash |at|at-|at |ath|ath-|ath |bin |of |of the |wal|wal-|wal |wa|wa-|wa )?[A-Z][a-z('a|a')]{2,})*"
        soup_regex = re_compile(u"^((?:"+titled_pattern+" )*" + keyword_pattern + "(?: "+titled_pattern+")*)$", IGNORECASE|UNICODE)
 
def return_soup_regex():
    global soup_regex
    createSoupRegexIfNecessary()
    return soup_regex

def getOrgsFromSoup(soup):
    global soup_regex
    createSoupRegexIfNecessary()

    try:
        print 'starting getOrgsFromSoup'
#        for elem in soup(text=org_regex):
#            print "    ", elem
        orgs = soup.find_all('a', text=soup_regex) + soup.find_all('li', text=soup_regex)
        return [org for org in orgs if isOrganization(org.text.strip())]

    except Exception as e:
        print e

def loadStopWordsIfNecessary():
    #print "starting loadStopWordsIfNecessary"
    global stopwords
    if not stopwords:
        filepath = os.path.dirname(os.path.abspath(__file__)) + "/data/stopwords/orgs.txt"
        print "filepath is", filepath
        if isfile(filepath):
            with open(filepath) as f:
                stopwords = [line.strip().lower() for line in f if line]

def isOrganization(text):
    global stopwords
    global keywords
    global keywords_arabic
    loadOrgKeywordsIfNecessary()
    loadOrgKeywordsArabicIfNecessary()
    loadStopWordsIfNecessary() 

    text = text.lower()

    if text.count(" ") == 0:
        return False
    if text in stopwords:
        return False
    if text.startswith("congressman"):
        return False
    if text.endswith("for"):
        return False
    if text.startswith("commander"):
        return False

    for wordphrase in ("foundation Donor", "unites", "donors", "guards", "councilman", "pgp public key block"):
        if wordphrase in text:
            return False

    #for word in ("army", "assembly", "battalion", "bloc", "brigade", "brotherhood", "bureau", "church", "clan", "coalition", "commission", "committee", "community", "companies", "congress", "corps", "council", "department", "division", "force", "foundation", "front", "government", "group", "guard", "haraka", "hezb", "hizb", "house", "institute", "jabhat", "jaish", "jaysh", "legion", "liwa", "ministry", "movement", "office", "org", "organization", "parliament", "party", "rally", "senate", "supporters", "squadron", "unit", "union", "university"):
    for word in keywords + keywords_arabic:
        if word.lower() in text.lower():
            return True

    return False

def isAmbiguousOrg(text):
    #print "starting isAmbiguousOrg with", text
    text = titlecase(text)
    return any(word == text or "The " + word == text for word in ["Army", "Assembly", "Battalion", "Bloc", "Brigade", "Brotherhood", "Bureau", "Church", "Coalition", "Commission", "Committee", "Community", "Council", "Department", "Force", "Foundation", "Front", "Government", "Group", "Haraka", "Hezb", "Hizb", "House", "Institute", "Ministry", "Movement", "Office", "Org", "Organization", "Parliament", "Party", "Rally", "Senate", "Congress", "Unit", "Union", "University"])
