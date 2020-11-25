def getStatementsFromTextArabic(text):
    statements = []

    d = {}
    d['\u0648\u0642\u0627\u0644\u062a'] = 'said'

#    for statement in finditer(ur"(?P<verb>\u0648\u0642\u0627\u0644)(?P<speaker>.*)(?:aannn)?(?P<quote>\"[^\"]*\")", text, MULTILINE):
#        statements.append({'speaker': statement.group('speaker'), 'verb': statement.group('verb'), 'quote': statement.group('quote')})

    #text = """ï»®ïº¼ï»ï»«ïº ïºï» ïºï»´ïº ïºï»¸ïºï»´ïº¿  ïºÙ"ïºï» ï»ïºïº­ïºïº ïºï» ïºï»®ï»³ïº ïºï» ï»¤ï»¤ï»´ïºïº""""
    # described
#    for statement in finditer(r"(?P<verb>\ufeee\ufebc\ufed4\ufeeb\ufe8d)(?P<speaker>.*)(?:ïºÙ)?(?P<quote>\"[^\"]*\")", text, rMULTILINE):
#    for statement in finditer(ur"(?P<verb>\
#        statements.append({'speaker': statement.group("speaker"), 'verb': statement.group("verb"), 'quote': statement.group("quote")})

    #Said wa/andthe agency for research and development (UNITAR) "statement "
    #note past tense
    #note: sometimes speaker will have acronymn in it like above, but sometimes won't have it at all
    for statement in finditer(ur"(?P<verb>\u0648\u0642\u0627\u0644\u062a) \u0648?(?P<speaker>[^\"]*) \"(?P<quote>[^\"]*)\"",text, MULTILINE):
        statements.append({'speaker': statement.group("speaker"), 'verb': statement.group("verb"), 'quote': statement.group("quote")})

    # this is like in Arabic news
    # "Angela Merkel": Bla blab bla
    # not sure this is their way of quoting or is actually more likely paraphrasing
    # commenting out for now just in case
    #for statement in re.findit("^[\"'](?P<speaker>[^\"']*)[\"']: ?(?P<quote>[^\.\n$]*)$", text, re.MULTILINE):
   #    statements.append({'speaker': statement.group("speaker"), 'verb': None, 'quote': statement.group("quote")})

    return statements
gsfta = getStatementsFromTextArabic

def getStatementTypeArabic(text):
    d = {}
    d[u'\u062a\u0635\u0631\u064a\u062d \u0635\u062d\u0641\u064a'] = "Press Release"
    result = re.search(ur'(?P<type>\u062a\u0635\u0631\u064a\u062d \u0635\u062d\u0641\u064a)', text)

def isPressRelease(text):
    return any(word in text for word in ["Address", "Adress", "Advisory", "Press", "Statement", "Communique", "Remarks", "Speech", "Comments", "Media", "Note", "Media Advisory", "Media Statement", "Media Stetment", "Media Note"])
