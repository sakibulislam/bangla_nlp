#download List of adjectival and demonymic forms for countries and nations
from bs4 import BeautifulSoup
from re import split, sub
from requests import get

response = get("https://en.wikipedia.org/wiki/List_of_adjectival_and_demonymic_forms_for_countries_and_nations")
soup = BeautifulSoup(response.text)
table = soup.select(".wikitable")[0]
#print "table is", table
rows = table.find_all("tr")
print "rows are", rows

f = open("data/demonyms.txt", "wb")
for row in rows[2:]:
  try:
    print "row is", type(row)
    cells = row.find_all("td")
    print "cells are", len(cells)
    print "cell[0] is", type(cells[0])
    name_verbose = cells[0].get_text().split("[")[0].split("(")[0].strip()
    name_short = name_verbose.split(",")[0].strip()
    keys = []    
    keys += split(", | or |/", cells[1].get_text().split("[")[0].split("(")[0].strip())
    keys += split(", | or |/", cells[2].get_text().split("[")[0].split("(")[0].strip())
    print "\nnames_verbose: ", name_verbose
    print "names_short: ", name_short
    print "keys: ", keys
    print "\n"
    f.write(",".join([name_short] + list(set(keys)))+"\n")
  except Exception as e:
    print e

f.write(",".join(['Italy', 'Italiana', 'Italiano']))

"""
response = get("https://it.wikipedia.org/wiki/Lista_di_etnici_nazionali")
soup = BeautifulSoup(response.text)
container = soup.select("#mw-content-text")[0]
lis = container.find_all("li")
for li in lis:
    text = li.text
    if u"^" not in text:
        text = text.lstrip(u"\u00a0").lstrip(u"\u00c2")
        text = sub(ur"\[.*\]","", text)
        text = sub(ur"\(.*\)","", text)
        words = text.strip().split(",")
        if len(words) > 1:
            country = words[0]
            print "country is", country
#            for word in words:
#                word = word.strip()
#                print word
"""


f.close()

