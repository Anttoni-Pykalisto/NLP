import os

class Lexicon:
    dirname = os.path.dirname(__file__)

    def __init__(self):
        self.wordSet = set()

    def append(self, token_set):
        self.wordSet.update(token_set)

    def sortSet(self):
        self.wordSet = sorted(self.wordSet)

    def saveToFile(self):
        f = open("lexicon.txt","w+")
        for word in self.wordSet:
            f.write(word + '\n')
        self.wordSet.clear()
        f.close()