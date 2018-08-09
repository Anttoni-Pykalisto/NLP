from Finding import Finding
from os import listdir
from os.path import isfile, join
import numpy as np
import csv
import os

# positiveFiles = ['TrainingText/positiveReviews/' + f for f in listdir('TrainingText/positiveReviews/') if isfile(join('TrainingText/positiveReviews/', f))]

text = "The quick b'rown dbOpera_Warehouse jumped over the lazy dog nlp@gmail.com. There's also a cat-79. It is meowing meow"

#text="Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types of systems and systems of mixed types."

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

words=sorted(set(words),key=str.lower) #remove duplicate words

word2int={}
int2word={}

vocab_size=len(words) #give total number of unique words

print(vocab_size)

def write_dict_to_csv(filePath,data): #function to write fictionary to a csv file
	with open(filePath, 'w',newline='') as csvfile:
		writer=csv.writer(csvfile, dialect='excel',quoting=csv.QUOTE_NONNUMERIC)
		for d in data:
			writer.writerow(d)

def read_csv_as_dict(filePath):
	with open(filePath) as csvfile:
		reader=csv.reader(csvfile,dialect='excel',quoting=csv.QUOTE_NONNUMERIC)
		datalist=[]
		datalist=list(reader)
		for data in datalist: #convert the number strings into integers
			data[0]=int(data[0])
		return(datalist)


currentPath=os.getcwd()
filePath=currentPath+"dict.csv"

write_dict_to_csv(filePath,list(enumerate(words)))
dictionary=read_csv_as_dict(filePath)

#print(dictionary)

for i,word in dictionary: #Generate word2int and int2word indexes
	word2int[word]=i
	int2word[i]=word
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

def to_one_hot (data_point_index,vocab_size):
	temp=np.zeros(vocab_size)
	temp[data_point_index]=1
	return temp

x_train=[] #input words
y_train=[] #output words

for data_word in data:
	x_train.append(to_one_hot(word2int[data_word[0]],vocab_size))
	y_train.append(to_one_hot(word2int[data_word[1]],vocab_size))

x_train=np.asarray(x_train) #convert list to array
y_train=np.asarray(y_train) #convert list to array
