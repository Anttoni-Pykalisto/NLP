import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


class Finding:

    def __init__(self, id, text):
        self.id = id
        self.text = text
        self.tokens, self.sentences = self.creatingTokens();

    def creatingTokens(self):
        tokenizer = RegexpTokenizer(r'\w+')
        stop_words = set(stopwords.words('english'))
        tokens=[]
        sentence=[]
        processedString = nltk.sent_tokenize(self.text);
        for sentences in processedString:
            temp_tokens=tokenizer.tokenize(sentences)
            temp_tokens=[t for t in temp_tokens if not t in stop_words]
            tokens+=temp_tokens
            sentence.append(temp_tokens)

        return [tokens,sentence]


    def cleanSentences(self):
        strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
        string = self.text.lower().replace("<br />", " ")
        return re.sub(strip_special_chars, "", string.lower())


class Potato:
    text = "potato"
