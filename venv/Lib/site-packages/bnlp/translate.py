from os.path import abspath, dirname
from csv import reader as csv_reader
from requests import post
from sys import exit

global phrase_translation
phrase_translation = {}

filepath = dirname(abspath(__file__))


def loadDictionaryOfTranslationsIfNecessary():
    global phrase_translation
    if not phrase_translation:
        with open(filepath + '/data/translations.csv') as f:
            reader = csv_reader(f, delimiter=',', quotechar='"')
            for row in reader:
                phrase_translation[row[0]] = row[1]
            print "phrase_translation is", phrase_translation

def translate(api_key, text, original_language=None):
        loadDictionaryOfTranslationsIfNecessary()  
    #try:
        print "starting request_translation"
        if isinstance(text, str):
            text = text.decode('utf-8')
        headers = {'X-HTTP-Method-Override': 'GET'}
        params = {'format': 'text', 'key': api_key, 'target': 'en'}
        if original_language:
            params['source'] = original_language
        if len(text) < 3000:
            params['q'] = text
            r = post("https://www.googleapis.com/language/translate/v2", params=params, headers=headers)
            print "r.text is", r.text
            translation = r.json()['data']['translations'][0]['translatedText'] 
        else:
            chunks = []
            currentChunk = ""
            for sentence in [t+"." for t in text.split(".") if t]:
                if len(currentChunk) + len(sentence) >= 3000:
                    chunks.append(currentChunk.strip())
                    currentChunk = sentence
                else:
                    currentChunk += "  " + sentence 
            chunks.append(currentChunk.strip()) # add last chunk
            translation = ""
            for chunk in chunks:
                params['q'] = chunk
                r = post("https://www.googleapis.com/language/translate/v2", params=params, headers=headers)
                translation += "  " + r.json()['data']['translations'][0]['translatedText'] 
            translation = translation.strip()
   # except Exception as e:
   #     print "We caught this error when trying to translate.  You will have to try again." + str(e)
    
