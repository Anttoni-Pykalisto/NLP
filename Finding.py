import re
import nltk
from nltk.tokenize import RegexpTokenizer


class Finding:

    def __init__(self, id, text):
        self.id = id
        self.text = text
        self.tokens, self.sentences = self.creatingTokens();
        
    def creatingTokens(self):
        tokenizer = RegexpTokenizer(r'\w+')
        tokens=[]
        sentence=[]
        processedString = nltk.sent_tokenize(self.text);
        for sentences in processedString:

            tokens+=tokenizer.tokenize(sentences)
            sentence.append(tokenizer.tokenize(sentences))


        return [tokens,sentence]


    def cleanSentences(self):
        strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
        string = self.text.lower().replace("<br />", " ")
        return re.sub(strip_special_chars, "", string.lower())


class Potato:
    text = "potato"
