import re

class Finding:

    def __init__(self, id, text):
        self.id = id
        self.text = text
        self.tokens = self.creatingTokens()
        
    def creatingTokens(self):
        processedString = self.cleanSentences()
        return processedString.split()

    def cleanSentences(self):
        strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
        string = self.text.lower().replace("<br />", " ")
        return re.sub(strip_special_chars, "", string.lower())


class Potato:
    text = "potato"