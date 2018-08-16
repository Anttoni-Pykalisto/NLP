from Finding import Finding
from Vocabulary import Vocabulary
from Context import Context
from Batches import BatchList
from Word2Vec_Model import Model
from os import listdir
from os.path import isfile, join
import numpy as np
import csv
import os

training_files = ['TrainingText/' + f for f in listdir('TrainingText/') if isfile(join('TrainingText/', f))]

all_finding = []
all_text = []
text = ''

#Create vocabulary
vocabulary = Vocabulary(min_frequency = 1, max_size = 100)

index = 0
for f in training_files:
	with open(f, "r", encoding="utf-8") as f:
		line = f.readline()
		text += line
		finding = Finding(index, text)
		vocabulary.appendSet(finding.tokens)
		all_finding.append(finding)
		all_text += finding.sentences
		index += 1

context = Context(all_text, 2)

vocabulary.buildDataSets()
vocabulary.saveToFile()

batch = BatchList(context.context, 30, len(vocabulary.word_list))
model = Model(batch_size = batch.batch_size, embedding_size = 10, vocabulary_size = len(vocabulary.word_list))

model.startTraining(batch)
print("success?")

#Generating a batch for the skipgram model

#Build model

# word2int={}
# int2word={}

# vocab_size=len(words) #give total number of unique words

# print(vocab_size)

# def write_dict_to_csv(filePath,data): #function to write fictionary to a csv file
# 	with open(filePath, 'w',newline='') as csvfile:
# 		writer=csv.writer(csvfile, dialect='excel',quoting=csv.QUOTE_NONNUMERIC)
# 		for d in data:
# 			writer.writerow(d)


# def read_csv_as_dict(filePath):
# 	with open(filePath) as csvfile:
# 		reader=csv.reader(csvfile,dialect='excel',quoting=csv.QUOTE_NONNUMERIC)
# 		datalist=[]
# 		datalist=list(reader)
# 		for data in datalist: #convert the number strings into integers
# 			data[0]=int(data[0])
# 		return(datalist)


# currentPath=os.getcwd()
# filePath=currentPath+"dict.csv"

# write_dict_to_csv(filePath,list(enumerate(words)))
# dictionary=read_csv_as_dict(filePath)

# #print(dictionary)

# for i,word in dictionary: #Generate word2int and int2word indexes
# 	word2int[word]=i
# 	int2word[i]=word
# 	print(int2word[i])

# # print(word2int['quick'])
# # print(int2word[2])

# trainingData=[]

# windowSize = 1

# data=[]

# for sentence in finding.sentences:
# 	for word_index,word in enumerate(sentence):
# 		for nb_word in sentence[max(word_index-windowSize,0):min(word_index+windowSize,len(sentence))+1]:
# 			if nb_word != word:
# 				data.append([word,nb_word])

# print(str(data))

# def to_one_hot (data_point_index,vocab_size):
# 	temp=np.zeros(vocab_size)
# 	temp[data_point_index]=1
# 	return temp

# x_train=[] #input words
# y_train=[] #output words

# for data_word in data:
# 	x_train.append(to_one_hot(word2int[data_word[0]],vocab_size))
# 	y_train.append(to_one_hot(word2int[data_word[1]],vocab_size))

# x_train=np.asarray(x_train) #convert list to array
# y_train=np.asarray(y_train) #convert list to array