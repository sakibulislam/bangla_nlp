from re import findall, IGNORECASE, MULTILINE
def getPaginationFromTextArabic(text):
    result = findall(ur"(?:\u0627\u0644\u0635\u0641\u062d\u0629|\ufe8e\ufee0\ufebc\ufed4\ufea3\ufe93) (?P<current_page>\d+) (?:\u0645\u0646|\ufee2\ufee7) (?P<total_pages>\d+)", text, MULTILINE)
    if result:
        return {'current_page': int(result[0][0]), 'total_pages': int(result[0][1])}

def getPaginationFromTextEnglish(text):
    result = findall(r"(?:Page|u'\ufe8e\ufee0\ufebc\ufed4\ufea3\ufe93) (?P<current_page>\d+) (?:of|u'\ufee2\ufee7) (?P<total_pages>\d+)", IGNORECASE|MULTILINE)
    if result:
        return {'current_page': result.group("current_page"), 'total_pages': result.group("total_pages")}
