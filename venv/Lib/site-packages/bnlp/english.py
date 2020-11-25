from numpy import mean
from random import choice

def getAverageCharacterNumber(text):
    return mean([ord(choice(text)) for n in range(100)])

def isEnglish(text):
    return getAverageCharacterNumber(text) < 110
