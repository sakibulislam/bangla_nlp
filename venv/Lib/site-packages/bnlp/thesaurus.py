# returns a list of all words with the same meaning, including input word
# technically, these are not synonyms but synsets, but the distinction is not necessary for lay people
def getSynonymsForWord(word):
    #return list(set([synset.lemma_names() for synset in wordnet.synsets(word)]))
    synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemma_names():
            if lemma not in synonyms:
                synonyms.append(lemma)
    return synonyms
