import os

class  Vocabulary:
    wordSet = set()
    count = {}
    word_to_index = {}
    word_list = []

    def __init__(self, min_frequency = None, max_size = None):
        self.min_frequency = min_frequency
        self.max_size = max_size

    def appendSet(self, token_set):
        #self.wordSet.update(token_set)
        for token in token_set:
            if self.count.get(token) is not None:
                value = self.count.get(token) + 1
                self.count.update({token: value})
            else:
                self.count.setdefault(token, 1)
            
    def buildDataSets(self):
        index = 0
        for key, value in sorted(self.count.items(), key = lambda kv: (kv[1], kv[0]), reverse = True):
            if (self.min_frequency is not None and value >= self.min_frequency) or self.min_frequency is None:
                self.word_list.append(key)
                self.word_to_index.setdefault(key, index)
                index += 1
                if self.max_size is not None and self.max_size == index:
                    break

    def getWord(self, index):
        return self.word_list[index]

    def getIndex(self, word):
        return self.word_to_index.get(word)

    def setMinFrequency(self, num):
        self.min_frequency = num

    def setMaxSize(self, num):
        self.max_size = num

    def getVocabSize(self):
        return len(self.word_list)

    def saveToFile(self):
        f = open("vocabulary.txt","w+")
        for word, count in self.count.items():
            f.write(word + ": " + str(count) + '\n')
        self.count.clear()
        f.close()
        f = open("word_list.txt","w+")
        for word in self.word_list:
            f.write(word + '\n')
        self.count.clear()
        f.close()
        f = open("index_to_word.txt","w+")
        for word, index in self.word_to_index.items():
            f.write(word + ": " + str(index) + '\n')
        self.count.clear()
        f.close()