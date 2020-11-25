def treeToString(tree):
    print "starting treeToString with", treeToString
    # if for some reason, you're accidentally passing in a unicode or byte string, just return what you passed in
    if isinstance(tree, unicode) or isinstance(tree, str):
        return tree
    else:
        listOfTokens = []
        for tup in tree.leaves():
            token = tup[0]
            tag = tup[1]
            listOfTokens.append(token)

        output = ' '.join(listOfTokens).strip('``').strip().strip("''").strip().strip(',').strip().strip('.').strip()
        return output
