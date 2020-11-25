# basically add s or es at the end if don't have one
def pluralize(term):
    plurals = [term+"s", term+"es"]

    if term.endswith("fe"):
        plurals.append(term[:-2] + "ves")
    elif term.endswith("f"):
        plurals.append(term[:-1] + "ves")
    elif term.endswith("u"):
        plurals.append(term[:-2] + "i")
    elif term.endswith("y"):
        plurals.append(term[:-1] + "ies")
    elif term.endswith("on"):
        plurals.append(term[:-2] + "a")
#this creates more problems than helps
#    elif term.endswith("an"):
#        plurals.append(term[:-2] + "en")

    return plurals


def singularize(term):
    singulars = []
    if term.endswith("s"):
        singulars.append(term.rstrip("s"))
    if term.endswith("ies"):
        singulars.append(term.rstrip("ies") + "y")
    if term.endswith("ves"):
        term_rstrip_ves = term.rstrip("ves")
        singulars.append(term_rstrip_ves + "f")
        singulars.append(term_rstrip_ves + "fe")
    if term.endswith("i"):
        singulars.append(term.rstrip("i") + "u")
    if term.endswith("a"):
        singulars.append(term.rstrip("a") + "on")
#    if term.endswith("an"):
#        singulars.append(term.rstrip("en") + "an")

    return singulars
