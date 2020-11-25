#-*- coding: utf-8 -*-
from sys import exit
from variations import ar_en

# returns previous, item, next
def neighborhood(iterable):
    iterator = iter(iterable)
    prev = None
    item = iterator.next()
    for next in iterator:
        yield (prev,item,next)
        prev = item
        item = next
    yield (prev,item,None)

def get_variations_as_pattern(string):
    print '\nstarting get_variations_as_pattern with', string

    if isinstance(string, str):
        string = string.decode("utf-8")

    pattern_as_string = ''
    for index, char in enumerate(string):

        if char in char_variations:
            pattern_as_string += '(' + '|'.join(char_variations[char]) + ')'
        else:
            pattern_as_string += char
    return pattern_as_string

#v = get_variations_as_pattern

               


buck2uni = {"'":"ء", "|":"آ", "?":"أ", "&":"ؤ", "<":"إ", "}":"ئ", "A":"ا", "b":"ب", "p":"ة", "t":"ت", "v":"ث", "g":"ج", "H":"ح", "x":"خ", "d":"د", "*":"ذ", "r":"ر", "z":"ز", "s":"س", "$":"ش", "S":"ص", "D":"ض", "T":"ط", "Z":"ظ", "E":"ع", "G":"غ", "_":"ـ", "f":"ف", "q":"ق", "k":"ك", "l":"ل", "m":"م", "n":"ن", "h":"ه", "w":"و", "Y":"ى", "y":"ي", "F":"ً", "N":"ٌ", "K":"ٍ", "~":"ّ", "o":"ْ", "u":"ُ", "a":"َ", "i":"ِ"}    


def transString(string, reverse=0):
    '''Given a Unicode string, transliterate into Buckwalter. To go from
    Buckwalter back to Unicode, set reverse=1'''

    if not reverse:     
        for k,v in buck2uni.iteritems():
            string = string.replace(v.decode('utf-8'),k.decode('utf-8'))

    else:     
        for k,v in buck2uni.iteritems():
            string = string.replace(k.decode('utf-8'),v.decode('utf-8'))

    return string
