#-*- coding: utf-8 -*-
from sys import exit
#from variations import char_variations
from en_en import d as en_en
from re import IGNORECASE, UNICODE
from re import compile as re_compile

def get_variations_as_pattern_as_string(string):
    print '\nstarting get_variations_as_pattern with', string

    if isinstance(string, str):
        string = string.decode("utf-8")

    string = string.lower()

    pattern_as_string = ''
    for index, char in enumerate(string):

        if char in char_variations:
            pattern_as_string += '(?:' + '|'.join(char_variations[char]) + ')'
        else:
            pattern_as_string += char

    print "finishing get_variations_as_pattern with", pattern_as_string
    return pattern_as_string

v = get_variations_as_pattern_as_string

# take in anglicized arabic and return a pattern
def get_fuzzy_string(text):
    if isinstance(text, str):
        text = text.decode('utf-8')

    text = text.lower()

    p = "(?:"

    length = len(text)

    o = ""

    i = 0
    while i < length:

        if i + 3 <= length:
            trigram = text[i:i+3]
            if trigram in en_en:
                o += "(?:" + "|".join(en_en[trigram]) + ")"
                i += 3
                continue

        if i + 2 <= length:
            bigram = text[i:i+2]
            if bigram in en_en:
                o += "(?:" + "|".join(en_en[bigram]) + ")"
                i += 2
                continue

        char = text[i]
        if char in en_en:
            o += "(?:" + "|".join(en_en[char]) + ")"
        else:
            o += char
        i+= 1
    print "returning", o
    return o

         
def get_fuzzy_regexp(text):
    return re_compile(get_fuzzy_string(text), IGNORECASE|UNICODE)
