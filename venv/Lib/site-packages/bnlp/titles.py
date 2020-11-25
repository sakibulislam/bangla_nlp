from titlecase import titlecase

# returns whether a string is a title, like to a webpage or a book
# basic string method isTitle will fail because unimportant words like "a", "and", and "of" aren't supposed to be titled
def isTitle(string):
    string_split = string.split()
    titled = 0
    uppered = 0
    lowered = 0
    for word in string_split:
        if string == titlecase(word):
            titled += 1
        elif word.isupper():
            uppered += 1
        elif word.islower():
            lowered += 1

    percentageTitled = float(titled) / float(len(string_split))
#    print "percentageTitled = ", percentageTitled
    if percentageTitled > .3:
        return True
    else:
        return False
