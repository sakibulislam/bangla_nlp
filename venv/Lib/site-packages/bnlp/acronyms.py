from re import findall

# for National Basketball Association, would return NBA
def getAcronymForWordPhrase(text):
    return "".join(findall("[A-Z]", text))

def getAcronymFromListOfStrings(listOfStrings):
    for string in listOfStrings:
        if string.isupper():
            return string


def getAcronymsFromText(text):
    return findall(r"[A-Z]{2,}", text)
