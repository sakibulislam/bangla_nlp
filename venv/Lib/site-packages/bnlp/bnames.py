def getNameWithoutSuffix(name):

    romanNumerals = ",? (IX|X|VIII|VII|VI|IV|V|III|II|I)$"

    if " Sr." in name:
        if ", Sr." in name:
            return name.replace(", Sr.","")
        elif " Sr." in name:
            return name.replace(" Sr.", "")
    elif " Jr." in name:
        if ", Jr." in name:
            return name.replace(", Jr.","")
        elif " Jr." in name:
            return name.replace(" Jr.", "")
    elif re.search(romanNumerals, name):
        return name.sub(romanNumerals,"",name)
    else:
        return name


def getLastName(name):
    name_split = name.split(" ")
    if name_split[-1] in ["Jr.", "Sr.", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]:
        return name_split[-2].rstrip(",")
    else:
        return name_split[-1]


def getNickName(name):
    result = re.search("(?<= (\(|\"))[A-Za-z]{2,}(?=(\)|\") )", name)
    if result:
        return result.group(0)
