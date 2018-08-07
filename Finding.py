import re

class Finding:

    def __init__(self, id, text):
        self.id = id
        self.text = text
        self.tokens, self.sentences = self.creatingTokens();
        
    def creatingTokens(self):
        sentences=[];
        processedString = self.cleanSentences()
        raw_sentences=self.text.split('.');
        for sentence in raw_sentences:
            sentences.append(sentence.split())
        sentences=[x for x in sentences if x!=[]]

        return [processedString.split(),sentences]

    def cleanSentences(self):
        strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
        string = self.text.lower().replace("<br />", " ")
        return re.sub(strip_special_chars, "", string.lower())


class Potato:
    text = "potato"