from Finding import Finding
from os import listdir
from os.path import isfile, join


# positiveFiles = ['TrainingText/positiveReviews/' + f for f in listdir('TrainingText/positiveReviews/') if isfile(join('TrainingText/positiveReviews/', f))]

text = "The quick b'rown fo.x jumped over the lazy dog. There is also a cat-79 it is meowing"

#with open(positiveFiles[0], "r", encoding="utf-8") as f:

#    line = f.readline()
#    text += line

finding = Finding(0, text)

print("Finding of ID: " + str(finding.id))
print("Has text: " + str(finding.tokens))
print('Sentences: '+str(finding.sentences))

words = []

for word in finding.tokens: #create dictionary
	words.append(word)

words=set(words) #remove duplicate words

word2int={}
int2word={}

vocab_size=len(words) #give total number of unique words

print(vocab_size)

for i,word in enumerate(words):
	word2int[word]=i
	int2word[i]=word

for i in range(0, vocab_size):
	print(int2word[i])

# print(word2int['quick'])
# print(int2word[2])

trainingData=[]

windowSize = 1

data=[]

for sentence in finding.sentences:
	for word_index,word in enumerate(sentence):
		for nb_word in sentence[max(word_index-windowSize,0):min(word_index+windowSize,len(sentence))+1]:
			if nb_word != word:
				data.append([word,nb_word])

print(str(data))
