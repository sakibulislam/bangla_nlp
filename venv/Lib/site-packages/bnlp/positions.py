def isPosition(text):
    return any(word in text for word in ["Acting", "Delegate", "General", "President", "Secretary", "Senator", "Spokesperson"])
