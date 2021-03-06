import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


# from nltk.stem import WordNetLemmatizer

class Text:

    def __init__(self, id, text, remove_stopwords="on", stemming="on"):
        self.id = id
        self.text = text
        self.tokens, self.sentences = self.creatingTokens(remove_stopwords, stemming)

    def creatingTokens(self, remove_stopwords, stemming):
        tokenizer = RegexpTokenizer(r'\s+', gaps=True)
        stop_words = set(stopwords.words('english'))
        stemmer = SnowballStemmer("english", ignore_stopwords=True)
        # wordnet_lemmatizer = WordNetLemmatizer()
        tokens = []
        sentence = []
        processedString = nltk.sent_tokenize(self.text)
        for sentences in processedString:
            temp_tokens = tokenizer.tokenize(sentences)
            temp_tokens = [self.cleanTokens(t) for t in temp_tokens]
            if remove_stopwords == "on":
                temp_tokens = [t for t in temp_tokens if not t in stop_words]
            if stemming == "on":
                temp_tokens = [stemmer.stem(t) for t in temp_tokens]
            tokens += temp_tokens
            sentence.append(temp_tokens)
        return [tokens, sentence]

    def cleanTokens(self, token):
        strip_special_chars = re.compile("[^a-z]+")
        string = token.lower().replace("<br />", " ")
        return re.sub(strip_special_chars, "", string.lower())


class Potato:
    text = "potato"
