from re import match, MULTILINE

def getHeaderFromTextAsString(string):
    matchobj = match(r"(?:\r?\n?[A-Za-z, \d\.()]{4,40}){2,7}",string, MULTILINE)
    if matchobj:
        return matchobj.group(0)

def getHeaderFromTextAsList(string):
    headerFromTextAsString = getHeaderFromTextAsString(string)
    if headerFromTextAsString:
        headerFromTextAsList = [line.strip() for line in headerFromTextAsString.splitlines() if line != ""]
        return headerFromTextAsList
