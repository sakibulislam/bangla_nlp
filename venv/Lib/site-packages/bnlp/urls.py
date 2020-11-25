def isSlug(string):
    return string.count("-") > string.count(" ")

def isUrlToArticle(url):
    return url.count("-") >= 3
